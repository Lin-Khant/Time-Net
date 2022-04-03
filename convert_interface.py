from tkinter import *
from calendar import monthrange
from program_manager import *
from ui import *

years = [i for i in range(1970, now.year + 1)]
months = [i for i in range(1, 13)]
range24 = [i for i in range(24)]
range60 = [i for i in range(60)]

# Function to initiate the Convert Interface
def main(widgets_to_destroy):   
    convert_button.config(bg="#ffffff", disabledforeground=THEME_COLORS["Blue"], state="disabled")
    world_button.config(bg="#000000", fg="#ffffff", state="normal")
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

# Original widgets (not converted)
# Row 0
from_year = StringVar(value=now.year)
org_year_menu = OptionMenu(container, from_year, *years)
org_year_menu.config(font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=3, border=0)
org_year_menu.grid(row=0, column=0, padx=(40, 20), pady=(40, 30))
org_year_label = Label(container, text="Yr", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
org_year_label.grid(row=0, column=1, padx=(0, 20), pady=(40, 30))

from_month = StringVar(value=now.month)
org_month_menu = OptionMenu(container, from_month, *months)
org_month_menu.config(font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=3, border=0)
org_month_menu.grid(row=0, column=2, padx=(0, 20), pady=(40, 30))
org_month_label = Label(container, text="M", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
org_month_label.grid(row=0, column=3, padx=(0, 20), pady=(40, 30))

day_count = monthrange(int(from_year.get()), int(from_month.get()))[1]
days = [i for i in range(1, day_count + 1)]

from_day = StringVar(value=now.day)
org_day_menu = OptionMenu(container, from_day, *days)
org_day_menu.config(font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=3, border=0)
org_day_menu.grid(row=0, column=4, padx=(0, 20), pady=(40, 30))
org_day_label = Label(container, text="D", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
org_day_label.grid(row=0, column=5, padx=(0, 20), pady=(40, 30))

# Row 1
from_hr = StringVar(value=now.hour)
org_hr_menu = OptionMenu(container, from_hr, *range24)
org_hr_menu.config(font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=3, border=0)
org_hr_menu.grid(row=1, column=0, padx=(40, 20), pady=(0, 30))
org_hr_label = Label(container, text="Hr", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
org_hr_label.grid(row=1, column=1, padx=(0, 20), pady=(0, 30))

from_min = StringVar(value=now.minute)
org_min_menu = OptionMenu(container, from_min, *range60)
org_min_menu.config(font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=3, border=0)
org_min_menu.grid(row=1, column=2, padx=(0, 20), pady=(0, 30))
org_min_label = Label(container, text="Min", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
org_min_label.grid(row=1, column=3, padx=(0, 20), pady=(0, 30))

from_sec = StringVar(value=now.second)
org_sec_menu = OptionMenu(container, from_sec, *range60)
org_sec_menu.config(font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=3, border=0)
org_sec_menu.grid(row=1, column=4, padx=(0, 20), pady=(0, 30))
org_sec_label = Label(container, text="Sec", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
org_sec_label.grid(row=1, column=5, padx=(0, 20), pady=(0, 30))

# Text 'in' and From Timezone Menu
in_label1 = Label(container, text="in", font=(THEME_FONT, 24), bg=THEME_COLORS["Frm"], fg="#000000")
in_label1.grid(row=0, column=6, rowspan=2, padx=(0, 20), pady=(40, 30))
from_tz = StringVar(value="Asia/Yangon")
from_tz_menu = OptionMenu(container, from_tz, *zones)
from_tz_menu.config(font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=27, border=0)
from_tz_menu.grid(row=0, column=7, rowspan=2, padx=(0, 40), pady=(40, 30))

# Converted widgets
# Row 3
converted_year = Label(container, font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=6)
converted_year.grid(row=3, column=0, padx=(40, 20), pady=(0, 30))
converted_year_label = Label(container, text="Yr", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
converted_year_label.grid(row=3, column=1, padx=(0, 20), pady=(0, 30))

converted_month = Label(container, font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=6)
converted_month.grid(row=3, column=2, padx=(0, 20), pady=(0, 30))
converted_month_label = Label(container, text="M", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
converted_month_label.grid(row=3, column=3, padx=(0, 20), pady=(0, 30))

converted_day = Label(container, font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=6)
converted_day.grid(row=3, column=4, padx=(0, 20), pady=(0, 30))
converted_day_label = Label(container, text="D", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
converted_day_label.grid(row=3, column=5, padx=(0, 20), pady=(0, 30))

# Row 4
converted_hr = Label(container, font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=6)
converted_hr.grid(row=4, column=0, padx=(40, 20), pady=(0, 41))
converted_hr_label = Label(container, text="Hr", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
converted_hr_label.grid(row=4, column=1, padx=(0, 20), pady=(0, 41))

converted_min = Label(container, font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=6)
converted_min.grid(row=4, column=2, padx=(0, 20), pady=(0, 41))
converted_min_label = Label(container, text="Min", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
converted_min_label.grid(row=4, column=3, padx=(0, 20), pady=(0, 41))

converted_sec = Label(container, font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=6)
converted_sec.grid(row=4, column=4, padx=(0, 20), pady=(0, 41))
converted_sec_label = Label(container, text="Sec", font=(THEME_FONT, 24, "bold"), bg=THEME_COLORS["Frm"], fg="#000000")
converted_sec_label.grid(row=4, column=5, padx=(0, 20), pady=(0, 41))

# Text 'in' and To Timezone Menu
in_label2 = Label(container, text="in", font=(THEME_FONT, 24), bg=THEME_COLORS["Frm"], fg="#000000")
in_label2.grid(row=3, column=6, rowspan=2, padx=(0, 20), pady=(0, 41))
to_tz = StringVar(value="America/Los_Angeles")
to_tz_menu = OptionMenu(container, to_tz, *zones)
to_tz_menu.config(font=(THEME_FONT, 24), bg="#ffffff", fg=THEME_COLORS["Blue"], width=27, border=0)
to_tz_menu.grid(row=3, column=7, rowspan=2, padx=(0, 40), pady=(0, 41))

# Equals Button
equals_button = Button(container, text="Equals to", font=(THEME_FONT, 20), bg="#000000", fg="#ffffff", width=10)
equals_button.config(command=lambda : convert(from_year.get(), from_month.get(), from_day.get(), from_hr.get(), from_min.get(), from_sec.get(), from_tz.get(), to_tz.get(),
                    [converted_year, converted_month, converted_day, converted_hr, converted_min, converted_sec]))
equals_button.grid(row=2, column=5, columnspan=2, padx=(0, 20), pady=(0, 30))