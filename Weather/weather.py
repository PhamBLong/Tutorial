from datetime import datetime
from tkinter import *
import requests
import pytz
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        
        if location is None:
            raise ValueError("City not found")

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3b37417ce48a8b15b689c6013eb2e3b9"
        json_data = requests.get(api).json()

        if json_data.get("cod") != 200:
            raise ValueError("Invalid city name or API key")

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)  # Convert Kelvin to Celsius
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(f"{temp} °C"))
        c.config(text=(f"{condition} | FEELS LIKE {temp} °C"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", str(e))

# Search components
Search_image = PhotoImage(file="search.png")
myimage = Label(root, image=Search_image)
myimage.place(x=20, y=20)

textfield = Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(root, image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
logo_image = PhotoImage(file="logo.png")
logo = Label(root, image=logo_image)
logo.place(x=490, y=130)

# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_image = Label(root, image=Frame_image)
frame_image.pack(padx=5, pady=5, side=BOTTOM)

# Time and Labels
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 15, "bold"))
clock.place(x=30, y=130)

label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="TEMPERATURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Display data
t = Label(root, font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(root, font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)

h = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)

d = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)

p = Label(root, text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
