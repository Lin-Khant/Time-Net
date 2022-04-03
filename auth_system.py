import os
import smtplib

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from tkinter import messagebox
from random import randint
from ui import *

# Variable to check if authentication was successful
authenticated = False

# User data
user_data = {}

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Database Spreadsheet
DATA_BASE_ID = "1VOclUGVG6sZtKOhTDWLDBl-5EuzkidHPQ92JJlzWzuM"
DATA_BASE = "Users Data"

# Environment Vars (replace with your own email and password)
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_EMAIL_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")

# Log in with Google
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        except FileNotFoundError:
            messagebox.showerror("Credentials missing!", "Credentials file is missing. Couldn't log into the app.")
            window.quit()
        else:
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

# Read data
def read_data(creds):
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        batch = sheet.values().get(spreadsheetId=DATA_BASE_ID, range=f"{DATA_BASE}")
        result = batch.execute()
        return result['values']
    
    except HttpError as err:
        print(err)

# Log into the app
def log_in(user_input):
    global authenticated, user_data

    # Check if the username and password matches with any data in database
    data = read_data(creds)
    for i in range(1, len(data)):
        row = [data[i][0], data[i][1]]
        if user_input == row:
            authenticated = True
            user_data["Username"] = data[i][0]
            user_data["Password"] = data[i][1]
            user_data["Email"] = data[i][2]
            break
        elif user_input != row:
            authenticated = False

    if authenticated is not True:
        messagebox.showinfo("Oops!", "Incorrect username or password.")

# Register
def register(code):
    # Check if the verification code is incorrect
    if code_entry.get() != code:
        messagebox.showinfo("Incorrect Verification Code", "The code you entered is incorrect. Please try again.")
        code_entry.delete(0, END)
        code_entry.focus()
        return

    new_acc_data = [
        [
            regis_user_entry.get(),
            regis_pass_entry.get(),
            regis_email_entry.get()
        ]
    ]

    # Write the new data into database
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()

        body = {
            "values" : new_acc_data
        }

        batch = sheet.values().append(spreadsheetId=DATA_BASE_ID, range=DATA_BASE, valueInputOption="RAW", body=body)
        batch.execute()

        log_in([new_acc_data[0][0], new_acc_data[0][1]])

    except HttpError as err:
        print(err)

# Verification to register
def verify():
    username = regis_user_entry.get()
    pwd = regis_pass_entry.get()
    email = regis_email_entry.get()

    # Check if all input fields are filled
    if username == "" or pwd == "" or email == "":
        messagebox.showinfo("Oops!", "Make sure no input field is empty.")
        return

    # Check if the username already exists
    data = read_data(creds)
    for row in data:
        if username == row[0]:
            messagebox.showinfo("Oops!", "This username already exists. Try another one.")
            regis_user_entry.delete(0, END)
            regis_user_entry.focus()
            return

    # Send verification code
    v_code = "".join([str(randint(0, 9)) for i in range(6)])
    message = f"Here's your verification code to register an account for Time Net.\n{v_code}"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(MY_EMAIL, MY_EMAIL_PASSWORD)
            server.sendmail(MY_EMAIL, email, f"Subject:Verify your email address\n\n{message}")
    except:
        messagebox.showerror("Invalid Email", "Your email address is invalid. Please try again.")
        regis_email_entry.delete(0, END)
        regis_email_entry.focus()
        return

    # Display code input field and label
    continue_btn.config(state="disabled")
    code_label.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(0, 20))
    verify_btn.config(command=lambda : register(v_code))
    verify_btn.grid(row=5, column=0, padx=(20, 20), pady=(0, 20))
    code_entry.grid(row=5, column=1, padx=(0, 20), pady=(0, 20))
    code_entry.focus()