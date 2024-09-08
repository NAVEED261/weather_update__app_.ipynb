import requests
import streamlit as st

# Step 3: Function to fetch weather data from OpenWeatherMap API
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    try:
        # Fetch the weather data
        response = requests.get(complete_url)
        data = response.json()

        # Print the entire response to understand if there is an issue
        st.write("API Response:", data)  # Debug line to check the response from the API

        # Check if the response contains 'main' data
        if data["cod"] != "404":
            if "main" in data:
                main = data["main"]
                weather = data["weather"][0]
                
                # Extract required weather details
                temperature = main["temp"]
                pressure = main["pressure"]
                humidity = main["humidity"]
                weather_description = weather["description"].capitalize()
                
                # Displaying weather details with better formatting
                st.markdown(f"<h4 style='color:blue;'>Weather in {city_name.capitalize()}:</h4>", unsafe_allow_html=True)
                st.write(f"**Temperature**: {temperature}°C")
                st.write(f"**Pressure**: {pressure} hPa")
                st.write(f"**Humidity**: {humidity}%")
                st.write(f"**Description**: {weather_description}")
            else:
                st.error("Weather data unavailable for this city.")
        else:
            st.error(f"City {city_name} not found.")
    except Exception as e:
        st.error(f"Error fetching weather data. Please try again later. Error: {e}")

# Step 4: Create UI components (input box and button)
st.title("Weather Update App")
city_name = st.text_input("Enter city name", "Karachi")
api_key = "4b29d1631fbb006dd4253cc228c93468"  # Replace with your API key

# Step 5: Button to get weather
if st.button("Get Weather"):
    get_weather(city_name, api_key)
