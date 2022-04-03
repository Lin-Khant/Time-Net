from tkinter import *
from tkinter import ttk
from program_manager import *
from ui import *

# Function to initiate the World Interface
def main(widgets_to_destroy):   
    world_button.config(bg="#ffffff", disabledforeground=THEME_COLORS["Blue"], state="disabled")
    convert_button.config(bg="#000000", fg="#ffffff", state="normal")
    profile_button.config(bg="#000000", fg="#ffffff", state="normal")

    main_canvas.pack()
    
    for widget in widgets_to_destroy:
        widget.pack_forget()

# Create the main canvas
main_canvas = Canvas(main_frame, bg=THEME_COLORS["Frm"], width=1050, height=450)

# Create a frame in which all widgets will contain
container = Frame(main_canvas, bg=THEME_COLORS["Frm"])

# Add the frame to the canvas
main_canvas.create_window((0, 0), anchor=NW, window=container)

# Search and Entry
search_button = Button(container, text="Search", font=(THEME_FONT, 18), bg="#000000", fg="#ffffff", width=10)
search_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
entry = Entry(container, font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=63)
entry.grid(row=0, column=1, padx=(0, 20), pady=(20, 20))
entry.focus()

# Clocks Display
# Create a subframe in which the clocks will contain
clocks_container = Frame(container, bg=THEME_COLORS["Frm"])
clocks_container.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(0, 20))

# Create a scrollable canvas in the subframe
scroll_canvas = Canvas(clocks_container, bg=THEME_COLORS["Frm"], width=990, height=340)
scroll_canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Create the scrollbar
scrollbar = ttk.Scrollbar(clocks_container, orient=VERTICAL, command=scroll_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the scroll_canvas
scroll_canvas.config(yscrollcommand=scrollbar.set)
scroll_canvas.bind("<Configure>", lambda event: scroll_canvas.config(scrollregion=scroll_canvas.bbox(ALL)))

# Create a scrollbox
scrollbox = Frame(scroll_canvas, bg=THEME_COLORS["Frm"])

# Add the scrollbox to the scroll_canvas
scroll_canvas.create_window((0, 0), anchor=NW, window=scrollbox)

# Display clocks
generate_clocks(scrollbox)
search_button.config(command=lambda : search(scrollbox, entry.get()))