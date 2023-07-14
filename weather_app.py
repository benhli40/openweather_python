import requests
import json

# Load the API key from the external file
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Default to Celsius
    }
    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)
    return weather_data

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to format the time in HH:MM format
def format_time(timestamp):
    import datetime
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%H:%M")

# Function to display weather information
def display_weather(weather_data, city):
    if "main" in weather_data:
        main_data = weather_data["main"]
        wind_data = weather_data["wind"]
        sys_data = weather_data["sys"]

        temperature = main_data["temp"]
        feels_like = main_data["feels_like"]
        humidity = main_data["humidity"]
        visibility = weather_data.get("visibility", "N/A")
        wind_speed = wind_data.get("speed", "N/A")
        wind_direction = wind_data.get("deg", "N/A")
        pressure = main_data["pressure"]
        dew_point = main_data["dew_point"]
        uv_index = weather_data.get("uvi", "N/A")
        sunrise = sys_data["sunrise"]
        sunset = sys_data["sunset"]

        # Determine the unit of temperature based on the city
        if weather_data["sys"]["country"] == "US":
            temperature_unit = "°F"
            temperature = celsius_to_fahrenheit(temperature)
            feels_like = celsius_to_fahrenheit(feels_like)
        else:
            temperature_unit = "°C"

        print(f"Weather information for {city}:")
        print(f"Temperature: {temperature} {temperature_unit}")
        print(f"Feels Like: {feels_like} {temperature_unit}")
        print(f"Humidity: {humidity}%")
        print(f"Visibility: {visibility} meters")
        print(f"Wind: {wind_speed} m/s, {wind_direction}°")
        print(f"Pressure: {pressure} hPa")
        print(f"Dew Point: {dew_point} {temperature_unit}")
        print(f"UV Index: {uv_index}")
        print(f"Sunrise: {format_time(sunrise)}")
        print(f"Sunset: {format_time(sunset)}")
    else:
        print(f"Couldn't find weather information for {city}")

# Ask the user for the city name
city = input("Enter the city name: ")

# Get weather data for the given city
weather_data = get_weather(city)

# Display weather information
display_weather(weather_data, city)