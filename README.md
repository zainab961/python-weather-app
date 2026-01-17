# python-weather-app
This is a weather app made using Python. It gets weather data from the OpenWeather API and shows the temperature and weather condition for a city entered by the user. The app also displays today’s highest and lowest temperatures and uses a simple GUI Tkinter.
Features
Search weather by city name
Displays temperature and weather description
Handles invalid city names
Simple and user-friendly GUI
Technologies Used
Python
Tkinter (GUI)
Requests (API requests)
OpenWeather API
Error Handling
Shows warning if city field is empty
Displays an error if the city is not found
Prevents crashes due to invalid input
How to Run
Install Python 3.x
OpenWeather API key (free)
### Install Required Packages
Run the following command in your project directory:
pip install requests python-dotenv
API Key Setup
Create a file named .env in the project folder
Add your OpenWeather API key inside the file:
write:
OPENWEATHER_API_KEY=your_api_key_here
Run the Application
Execute the Python script:
write in command prompt python weather.py
Enter a city name
Click Get Weather
View the current temperature, weather condition, and today’s high and low
Install dependencies:
pip install requests python-dotenv
Run the app:
python weather.py
