import requests  # Imports of modules
import config  # Imports of modules

url = "https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}"  # URL to access OpenWeatherAPI


class Weather:  # Weather Class
    def __init__(self, city, country):  # Initialization of variables and running of first function
        self.country = country
        self.city = city

    def set_city(self, city):
        if len(city) == 0:
            print('Please enter a city')
        else:
            if not city.isalpha():
                print('Please enter a city in a string format')
            else:
                self.city = city

    def set_country(self, country):
        if len(country) == 0:
            print('Please enter a country')
        else:
            if not country.isalpha():
                print('Please enter a country in a string format')
            else:
                self.country = country

    def get_weather(self):
        res = requests.get(url.format(self.city, self.country, config.api_key))  # GET request to OpenWeatherAPI URL
        if res.status_code == 200:  # IF 200 OK Print Info
            self.display_weather(res)  # Runs print function
        elif res.status_code == 404:  # IF 404 print error saying country/city not found
            print("Error in getting weather data.  Please check your city & country entered")
        elif res.status_code == 401:  # IF 404 print error saying country/city not found
            print("Error in getting weather data.  Unauthorized")
        else:  # IF other error print issue with server
            print("Error in getting weather data.  Server may be having trouble")

    @staticmethod  # Utility Function
    def display_weather(res):  # Takes in response from the API
        weather_res = res.json()  # Converts it to JSON object
        current_temp = weather_res['main']['temp'] - 273.15  # Gets oC from Kelvin
        print("The weather in " + weather_res['name'] + ', ' + weather_res['sys']['country'] +  # Prints weather info
              "\nIt's currently: " + weather_res['weather'][0]['description'] +
              "\nCurrent Temp is: {:.1f}".format(current_temp) + " C" +
              "\nFeels like: {:.1f}".format(weather_res['main']['feels_like'] - 273.15) + " C" +
              "\nWind speed is: " + str(weather_res['wind']['speed']) + " Knots")


test = Weather('', '')
test.set_city('')
test.set_country('')
test.get_weather()
