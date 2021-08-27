import requests  # Imports of modules
import config  # Imports of modules

url = "https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}"  # URL to access OpenWeatherAPI


def get_weather(city, country):
    res = requests.get(url.format(city, country, config.api_key))  # GET request to OpenWeatherAPI URL
    if res.status_code == 200:  # IF 200 OK Print Info
        display_weather(res)  # Runs print function
    elif res.status_code == 404:  # IF 404 print error saying country/city not found
        print("Error in getting weather data.  Please check your city & country entered")
    else:  # IF other error print issue with server
        print("Error in getting weather data.  Server may be having trouble")


def display_weather(res):  # Takes in response from the API
    weather_res = res.json()  # Converts it to JSON object
    current_temp = weather_res['main']['temp'] - 273.15  # Gets oC from Kelvin
    print("The weather in " + weather_res['name'] + ', ' + weather_res['sys']['country'] +  # Prints weather info
          "\nIt's currently: " + weather_res['weather'][0]['description'] +
          "\nCurrent Temp is: {:.1f}".format(current_temp) + " C" +
          "\nFeels like: {:.1f}".format(weather_res['main']['feels_like'] - 273.15) + " C" +
          "\nWind speed is: " + str(weather_res['wind']['speed']) + " Knots")


def check_input(prompt_text):  # Function to check users input
    while True:
        try:
            user_input = str(input(prompt_text))  # Gets users input
        except ValueError as val_err:
            print(val_err)
            continue  # Starts loop again
        if user_input == "":  # If input is blank print message
            print("Input is blank.  Try again")
            continue  # Starts loop again
        else:
            if not user_input.isalpha():  # If input is not a string print message
                print("Please enter a string")
            else:
                break  # Break from while loop
    return user_input  # Return value


user_city = check_input('Please enter a city: ')
user_country = check_input('Please enter a country: ')
get_weather(user_city, user_country)