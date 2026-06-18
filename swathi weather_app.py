import requests 
def get_weather():
	city = input("Enter city name:")
	api_key="a982d71035ecec7e5f9183a44691dda9"
	url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
	response = requests.get(url)
	data = response.json()
	if data["cod"] ==200: 
	    temp = data["main"]["temp"]
	    desc = data["weather"][0]["description"]
	    humidity = data["main"]["humidity"]
	    print(f"\nweather in{city}:")
	    print(f"Temperature :{temp}°c")
	    print(f"Condition :{desc}")
	    print(f"Humidity:{humidity}%")
	else :
		print("City not found . check spelling da !")
get_weather()