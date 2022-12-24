from tkinter import *
import tkinter as tk
import pytz
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
from tkinter import messagebox
root = Tk()
root.geometry('850x500+0+0')
root.resizable(0,0)
root.title('Weather Tracker')

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(city)
        finder = TimezoneFinder()
        result = finder.timezone_at(lng=location.longitude, lat=location.latitude)
        current_time = datetime.now(pytz.timezone(result)).strftime('%I:%M %p')
        current_date = datetime.now(pytz.timezone(result)).strftime('%d-%b-%Y')
        time.config(text=current_time)
        date.config(text=('|',current_date))

        api = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=646824f2b7b86caffec1d0b16ea77f79'
        json_data = requests.get(api).json()
        temperature_deg = int(json_data['main']['temp']-273.15)
        temperature_fah = int(json_data['main']['temp'])

        condition = json_data['weather'][0]['main']
        wind = json_data['wind']['speed']
        humidity = json_data['main']['humidity']
        description = json_data['weather'][0]['description']
        pressure = json_data['main']['pressure']

        t.config(text=(temperature_deg, '°C', '/', temperature_fah, '°F'))
        c.config(text=(condition, '|', 'feels', 'like', temperature_deg, '°C', '/', temperature_fah, '°F'))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        label_peach.config(text='  Make the most of this nice weather that\n I generated for you. Or else...')

    except:
        messagebox.showerror('Weather Tracker', 'No such city/country. Please try again! :3')

search_box = PhotoImage(file='search_box.png')
Label(image=search_box).place(x=40, y=20)

textfield = tk.Entry(root, justify='left', width=15, font=('cooper black', 18), border=0, bg='#404040', fg='white', insertbackground='white')
textfield.place(x=65, y=27)
textfield.focus()

search_icon = PhotoImage(file='search_icon.png')
Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#404040', activebackground="#404040", command=getWeather).place(x=695, y=29)

logo = PhotoImage(file='logo.png')
Label(image=logo).place(x=40, y=104)

bottom_box = PhotoImage(file='bottom_box.png')
Label(image=bottom_box).pack(padx=5, pady=15, side=BOTTOM)

name = Label(root, font=('arial', 15, 'bold'))
name.place(x=300, y=100)

time = Label(root, font=('arial', 15, 'bold'))
time.place(x=325, y=120)

date = Label(root, font=('arial', 15, 'bold'))
date.place(x=420, y=120)

peach = PhotoImage(file='peach.png')
Label(image=peach).place(x=325, y=275)

label_peach = Label(root, text='', font=('arial', 15, 'bold'), fg='#843c0c', bg='#f8cbad')
label_peach.place(x=360, y=290)

label1 = Label(root, text='WIND', font=('cooper black', 15, 'bold'), fg='white', bg='#843c0c')
label1.place(x=80, y=405)

label2 = Label(root, text='HUMIDITY', font=('cooper black', 15, 'bold'), fg='white', bg='#843c0c')
label2.place(x=220, y=405)

label3 = Label(root, text='DESCRIPTION', font=('cooper black', 15, 'bold'), fg='white', bg='#843c0c')
label3.place(x=410, y=405)

label4 = Label(root, text='PRESSURE', font=('cooper black', 15, 'bold'), fg='white', bg='#843c0c')
label4.place(x=630, y=405)

t = Label(font=('arial', 50, 'bold'), fg='#873e23')
t.place(x=325, y=155)

c = Label(font=('arial', 15, 'bold'), fg='#873e23')
c.place(x=325, y=235)

w = Label(root, text='m/s', font=('Helvetica', 15, 'bold'), fg='white', bg='#843c0c')
w.place(x=80, y=430)

h = Label(root, text='%', font=('Helvetica', 15, 'bold'), fg='white', bg='#843c0c')
h.place(x=220, y=430)

d = Label(root, text='---', font=('Helvetica', 15, 'bold'), fg='white', bg='#843c0c')
d.place(x=410, y=430)

p = Label(root, text='hPa', font=('Helvetica', 15, 'bold'), fg='white', bg='#843c0c')
p.place(x=630, y=430)

root.mainloop()