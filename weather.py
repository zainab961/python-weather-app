import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = 'a4cee5d4a8644b232c1005b1aeaf80eb'

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != "200":
        messagebox.showerror("Error", "City not found")
        return

    today_list = data["list"][:8]      # first 24 hours (3hr intervals)
    temps = [item["main"]["temp"] for item in today_list]
    descriptions = [item["weather"][0]["description"] for item in today_list]

    current_temp = today_list[0]["main"]["temp"]
    today_high = max(temps)
    today_low = min(temps)
    description = descriptions[0]

    result = (f"City: {city}\n"
              f"Current Temp: {current_temp}°C\n"
              f"Weather: {description}\n"
              f"Today High: {today_high}°C\n"
              f"Today Low: {today_low}°C")

    result_label.config(text=result)


root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")

tk.Label(root, text="Enter City Name").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack()

root.mainloop()
