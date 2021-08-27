import unittest  # Imports of modules
import requests
import config

url = "https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}"  # URL to access OpenWeatherAPI


class TestWeather(unittest.TestCase):  # Test class initialized as test case

    @staticmethod  # Utility Function to get weather
    def fetchWebsite(city, country):
        return requests.get(url.format(city, country, config.api_key))

    def test_get_weather_200(self):  # Checks we get 200 OK when correct country & city entered
        res = self.fetchWebsite('Dublin', 'IE')
        self.assertEqual(res.status_code, 200)

    def test_get_weather_404(self):  # Checks we get 404 NOT FOUND when incorrect country & city entered
        res = self.fetchWebsite('Dublin', 'IR')
        self.assertEqual(res.status_code, 404)

    def test_get_weather_unauth(self):  # Checks we get 401 UNAUTHORIZED when incorrect API key is given
        res = requests.get(url.format('Dublin', 'IE', '233232'))
        self.assertEqual(res.status_code, 401)

    def test_get_weather_JSON(self):  # Checks we get JSON as content
        res = self.fetchWebsite('Dublin', 'IE')
        self.assertEqual(res.headers['Content-Type'].split()[0], 'application/json;')

    def test_get_weather_Data(self):  # Checks we get data and we get the correct data
        city = 'Dublin'
        res = self.fetchWebsite(city, 'IE')
        res_data = res.json()
        self.assertEqual(res_data['name'], city)


if __name__ == '__main__':
    unittest.main()
