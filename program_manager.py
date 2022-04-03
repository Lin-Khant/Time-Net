from datetime import datetime
from tkinter import Label
from tkinter import messagebox
from ui import *
import pytz
import requests
import os

now = datetime.now()
clocks = {}

# Environment Var (Required an api key in Time Zone DB API)
TIMEZONEDB_API_KEY = os.environ.get("TIMEZONEDB_API_KEY")

# Get all available timezones from Timezone DB API
try:
    response = requests.get(f"http://api.timezonedb.com/v2.1/list-time-zone?key={TIMEZONEDB_API_KEY}&format=json")
    response.raise_for_status()
    zones = [zone["zoneName"] for zone in response.json()["zones"]]
except requests.exceptions.ConnectionError:
    messagebox.showerror("Network connection failed!", "Check your network connection and try again.")
    window.quit()

# Convert a specific timestamp of a timezone to another timezone using timezonedb api
def convert(year, month, day, hr, min, sec, from_tz, to_tz, labels):
    from_dt = datetime(int(year), int(month), int(day), int(hr), int(min), int(sec))
    tstamp = round(from_dt.timestamp())

    parameters = {
    "key": f"{TIMEZONEDB_API_KEY}",
    "format": "json",
    "from": from_tz,
    "to": to_tz,
    "time": tstamp,
    }

    try:
        response = requests.get("http://api.timezonedb.com/v2.1/convert-time-zone", params=parameters)
        response.raise_for_status()
        converted_tstamp = response.json()["toTimestamp"]
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Network connection failed!", "Check your network connection and try again.")
        window.quit()
    else:
        converted_dt = datetime.fromtimestamp(converted_tstamp)
        label_texts = ["%Y", "%#m", "%#d", "%#H", "%#M", "%#S"]
        for i in range(len(labels)):
            labels[i].config(text=converted_dt.strftime(label_texts[i]))

# Display clocks
def generate_clocks(container, zone_list=zones):
    for i in range(len(zone_list)):
        tz = pytz.timezone(zone_list[i])
        dtime = datetime.now(tz)
        clock_txt = f"{zone_list[i]} : " + dtime.strftime("%Y-%#m-%#d | %#H:%M:%S")
        clock = Label(container, text=clock_txt, font=(THEME_FONT, 30), bg="#ffffff", fg=THEME_COLORS["Blue"], width=67)
        clock.grid(row=i, column=0, pady=(0, 20))
        clocks[zone_list[i]] = clock

# Update all clocks
def update_clocks():
    if clocks != {}:
        for clock in clocks:
            tz = pytz.timezone(clock)
            dtime = datetime.now(tz)
            clock_txt = f"{clock} : " + dtime.strftime("%Y-%#m-%#d | %#H:%M:%S")
            clocks[clock].config(text=clock_txt)

# Search for a clock
def search(container, input):
    for clock in clocks:
        clocks[clock].destroy()
    
    clocks.clear()

    searched_zones = [zone for zone in zones if input.lower().strip() in zone.lower()]
    generate_clocks(container, searched_zones)

    if searched_zones == []:
        messagebox.showinfo("Oops!", f"The timezone you searched, '{input}' isn't available.")