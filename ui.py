# Base UI file of all other interfaces

from tkinter import *

THEME_FONT = "Agency FB"
THEME_COLORS = {
    "BG" : "#a2a2a2",
    "Frm" : "#616161",
    "Blue" : "#1d4992",
}

# Initiate the welcome interface
def start(widgets_to_destroy=None):
    login_page_btn.grid(row=0, column=0, padx=(20, 20), pady=(220, 220))
    or_text.grid(row=0, column=1, padx=(0, 20), pady=(220, 220))
    regis_page_btn.grid(row=0, column=2, padx=(0, 20), pady=(220, 220))

    title.config(text="Welcome to Time Net!")

    if widgets_to_destroy is not None:
        entries = [login_user_entry, login_pass_entry, regis_user_entry, regis_pass_entry, regis_email_entry, code_entry]
        for widget in widgets_to_destroy:
            widget.grid_forget()
        for entry in entries:
            entry.delete(0, END)

        login_back_btn.grid_forget()
        regis_back_btn.grid_forget()

# Initiate the login page
def login_page():
    login_page_btn.grid_forget()
    or_text.grid_forget()
    regis_page_btn.grid_forget()
    title.config(text="Log in")
    login_user_label.grid(row=0, column=0, padx=(20, 20), pady=(100, 20), sticky=W)
    login_user_entry.grid(row=0, column=1, padx=(0, 20), pady=(100, 20))
    login_user_entry.focus()
    login_pass_label.grid(row=1, column=0, padx=(20, 20), pady=(0, 20), sticky=W)
    login_pass_entry.grid(row=1, column=1, padx=(0, 20), pady=(0, 20))
    login_btn.grid(row=2, column=0, columnspan=2, pady=(0, 20))
    login_back_btn.grid(row=3, column=0, columnspan=2, pady=(0, 20))

# Initiate the register page
def register_page():
    login_page_btn.grid_forget()
    or_text.grid_forget()
    regis_page_btn.grid_forget()
    title.config(text="Create an Account")
    regis_user_label.grid(row=0, column=0, padx=(20, 20), pady=(50, 20), sticky=W)
    regis_user_entry.grid(row=0, column=1, padx=(0, 20), pady=(50, 20))
    regis_user_entry.focus()
    regis_pass_label.grid(row=1, column=0, padx=(20, 20), pady=(0, 20), sticky=W)
    regis_pass_entry.grid(row=1, column=1, padx=(0, 20), pady=(0, 20))
    regis_email_label.grid(row=2, column=0, padx=(20, 20), pady=(0, 20), sticky=W)
    regis_email_entry.grid(row=2, column=1, padx=(0, 20), pady=(0, 20))
    continue_btn.grid(row=3, column=0, columnspan=2, pady=(0, 20))
    continue_btn.config(state="normal")
    regis_back_btn.grid(row=6, column=0, columnspan=2, pady=(0, 20))

# Initiate the main interface
def home():
    wel_interface.pack_forget()
    title.config(text="Time Net")
    main_frame.pack(pady=(0, 20))
    menu.pack()

# Create the main window
window = Tk()
window.title("Time Net")
window.config(bg=THEME_COLORS["BG"], padx=20, pady=20)
window.geometry("1090x750")

# Create the title
title = Label(window, text="Welcome to Time Net!", font=(THEME_FONT, 60, "bold"), bg=THEME_COLORS["BG"], fg=THEME_COLORS["Blue"])
title.pack(pady=(0, 20))

# Create the welcome frame
wel_interface = Frame(window, bg=THEME_COLORS["BG"])
wel_interface.pack()

# ---Create and initiate the Welcome Interface---
# Create 2 buttons (log in and register)
login_page_btn = Button(wel_interface, text="Log in", font=(THEME_FONT, 30, "bold"), bg="#ffffff", fg=THEME_COLORS["Blue"], width=10,
                        command=login_page)
or_text = Label(wel_interface, text="or", font=(THEME_FONT, 36), bg=THEME_COLORS["BG"], fg="#000000")
regis_page_btn = Button(wel_interface, text="Register", font=(THEME_FONT, 30, "bold"), bg="#ffffff", fg=THEME_COLORS["Blue"], width=10,
                        command=register_page)
start()

# ---Create login page--- (Haven't initiated)
login_user_label = Label(wel_interface, text="Username", font=(THEME_FONT, 30, "bold"), bg=THEME_COLORS["BG"], fg=THEME_COLORS["Blue"])
login_user_entry = Entry(wel_interface, font=("Times New Roman", 30), bg="#ffffff", fg="#000000", width=30)
login_pass_label = Label(wel_interface, text="Password", font=(THEME_FONT, 30, "bold"), bg=THEME_COLORS["BG"], fg=THEME_COLORS["Blue"])
login_pass_entry = Entry(wel_interface, font=("Times New Roman", 30), bg="#ffffff", fg="#000000", width=30)
login_btn = Button(wel_interface, text="Log in", font=(THEME_FONT, 24, "bold"), bg="#000000", fg="#ffffff", width=10)

# All main widgets in login page
login_widgets = [login_user_label, login_user_entry, login_pass_label, login_pass_entry, login_btn]

# Back Button
login_back_btn = Button(wel_interface, text="Back", font=(THEME_FONT, 18, "bold"), bg="#000000", fg="#ffffff", width=10,
                        command=lambda : start(login_widgets))

# ---Create register page--- (Haven't initiated)
# Section 1
regis_user_label = Label(wel_interface, text="Username", font=(THEME_FONT, 30, "bold"), bg=THEME_COLORS["BG"], fg=THEME_COLORS["Blue"])
regis_user_entry = Entry(wel_interface, font=("Times New Roman", 24), bg="#ffffff", fg="#000000", width=30)
regis_pass_label = Label(wel_interface, text="Password", font=(THEME_FONT, 30, "bold"), bg=THEME_COLORS["BG"], fg=THEME_COLORS["Blue"])
regis_pass_entry = Entry(wel_interface, font=("Times New Roman", 24), bg="#ffffff", fg="#000000", width=30)
regis_email_label = Label(wel_interface, text="Email", font=(THEME_FONT, 30, "bold"), bg=THEME_COLORS["BG"], fg=THEME_COLORS["Blue"])
regis_email_entry = Entry(wel_interface, font=("Times New Roman", 24), bg="#ffffff", fg="#000000", width=30)
continue_btn = Button(wel_interface, text="Continue", font=(THEME_FONT, 24, "bold"), bg="#000000", fg="#ffffff", width=10)

# Section 2
label_txt = "A verification code has been sent to your email."
code_label = Label(wel_interface, text=label_txt, font=(THEME_FONT, 30, "bold"), bg=THEME_COLORS["BG"], fg=THEME_COLORS["Blue"])
code_entry = Entry(wel_interface, font=("Times New Roman", 30), bg="#ffffff", fg="#000000", width=30)
verify_btn = Button(wel_interface, text="Verify", font=(THEME_FONT, 18, "bold"), bg="#000000", fg="#ffffff", width=10)

# All main widgets in register page
regis_widgets = [regis_user_label, regis_user_entry, regis_pass_label, regis_pass_entry, regis_email_label, regis_email_entry, 
                 continue_btn, code_label, code_entry, verify_btn]

# Back Button
regis_back_btn = Button(wel_interface, text="Back", font=(THEME_FONT, 18, "bold"), bg="#000000", fg="#ffffff", width=10,
                        command=lambda : start(regis_widgets))

# ---Create the Main Interface--- (Haven't initiated)
# Create the main frame
main_frame = Frame(window, bg=THEME_COLORS["BG"])

# Create the menu
menu = Frame(window, bg=THEME_COLORS["Blue"])
convert_button = Button(menu, text="Convert", font=(THEME_FONT, 26, "bold"), bg="#000000", fg="#ffffff", width=23)
convert_button.grid(row=0, column=0, padx=(15, 15), pady=(15, 15))
world_button = Button(menu, text="World", font=(THEME_FONT, 26, "bold"), bg="#000000", fg="#ffffff", width=23)
world_button.grid(row=0, column=1, padx=(0, 15), pady=(15, 15))
profile_button = Button(menu, text="Profile", font=(THEME_FONT, 26, "bold"), bg="#000000", fg="#ffffff", width=23)
profile_button.grid(row=0, column=2, padx=(0, 15), pady=(15, 15))