from tkinter import *
from ui import *

# Function to initiate the Profile Interface
def main(widgets_to_destroy):   
    profile_button.config(bg="#ffffff", disabledforeground=THEME_COLORS["Blue"], state="disabled")
    convert_button.config(bg="#000000", fg="#ffffff", state="normal")
    world_button.config(bg="#000000", fg="#ffffff", state="normal")

    main_canvas.pack()
    
    for widget in widgets_to_destroy:
        widget.pack_forget()

# Create the main canvas
main_canvas = Canvas(main_frame, bg=THEME_COLORS["Frm"], width=1050, height=450)

# Create a frame in which all widgets will contain
container = Frame(main_canvas, bg=THEME_COLORS["Frm"])

# Add the frame to the canvas
main_canvas.create_window((0, 0), anchor=NW, window=container)

# Add labels inside the container
username_label = Label(container, font=("Times New Roman", 30, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
username_label.grid(row=0, column=0, padx=(20, 400), pady=(130, 20), sticky=W)
pwd_label = Label(container, font=("Times New Roman", 30, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
pwd_label.grid(row=1, column=0, padx=(20, 400), pady=(0, 20), sticky=W)
email_label = Label(container, font=("Times New Roman", 30, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
email_label.grid(row=2, column=0, padx=(20, 400), pady=(0, 130), sticky=W)