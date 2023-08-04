import tkinter as tk
import requests

# Light-wear and Transitional Outfit Inventories (Replace with your actual outfits data)
lightwear_inventory = ["Light-wear Outfit 1", "Light-wear Outfit 2", "Light-wear Outfit 3"]
transitional_inventory = ["Transitional Outfit 1", "Transitional Outfit 2", "Transitional Outfit 3"]

def recommend_outfit(temperature, humidity):
    if temperature > 25 and humidity > 60:
        if lightwear_inventory:
            recommended_outfit = lightwear_inventory[0]
            outfit_label.config(text=f"Recommended Light-wear Outfit: {recommended_outfit}")
        else:
            outfit_label.config(text="No Light-wear outfit available in inventory")
    else:
        if transitional_inventory:
            recommended_outfit = transitional_inventory[0]
            outfit_label.config(text=f"Recommended Transitional Outfit: {recommended_outfit}")
        else:
            outfit_label.config(text="No Transitional outfit available in inventory")


# Function to fetch weather data from ThingSpeak API
def fetch_weather():
    # Replace <YOUR_API_KEY> with your actual API key from ThingSpeak
    api_key = "<YOUR_API_KEY>"

    # Replace <CHANNEL_ID> with the actual channel ID from ThingSpeak
    channel_id = "<CHANNEL_ID>"

    # URL for the ThingSpeak API
    url = f"https://api.thingspeak.com/channels/2155023/feeds.json?api_key=LNI9QZ1XW9KZ0W8K&results=1"

    try:
        response = requests.get(url)
        data = response.json()

        if "feeds" in data and len(data["feeds"]) > 0:
            feed = data["feeds"][0]

            # Extract weather data fields (replace with your field names)
            temperature = float(feed.get("field1"))
            humidity = float(feed.get("field2"))

            # Update the weather label text
            weather_label.config(text=f"Temperature: {temperature}°C, Humidity: {humidity}%")

            # Call the recommend_outfit function with weather data
            recommend_outfit(temperature, humidity)
        else:
            weather_label.config(text="Weather data not available")
    except requests.RequestException:
        weather_label.config(text="Failed to fetch weather data")


# Create the main window
window = tk.Tk()
window.title("Smart Wardrobe")

# Create a label widget for the title
title_label = tk.Label(window, text="Smart Wardrobe", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Create a label widget for the weather
weather_label = tk.Label(window, text="Weather: ", font=("Helvetica", 12))
weather_label.pack(pady=10)

# Create a button widget to fetch weather data
fetch_button = tk.Button(window, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

# Create a label widget for the recommended outfit
outfit_label = tk.Label(window, text="Recommended Outfit: ", font=("Helvetica", 12))
outfit_label.pack()

# Run the main event loop
window.mainloop()