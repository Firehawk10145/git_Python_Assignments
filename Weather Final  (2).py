import json #importing JSON module is used to trasmit data in web applications, pulling data from Openweather servers to display forecast/requested data
import requests #importing the requests module allows us to send HTTP requests using Python such as pulling information from Openweather

def display_Intro(): #display welcome message to inform user what application they are using and how they can request it
  print('Welcome to the Weather Forecast Grabber. Here you can request the weather forecast for a zip code or city') 

def weather_Question(): #function used to ask user question to setup application waether forecast search by either zip code or city 
  weather_Question = '' #sets function to nothing to fill in when answering the input question
  while weather_Question != '1' and weather_Question !='2': #sets question loop to only equal 1 or 2
    weather_Question = input(str('Would you like to request the weather forecast by zip code or city name?\nType 1 - Zip Cod\nType 1 - City Name') #question for user to select to lookup weather forecast by zip code or city name
	  if weather_Question not in ("1", "2"): #if statement to provide error message if 1 or 2 are not input for the question 
		  print("Please select 1 or 2, try again.")
	break

def weather_zip(): #function used to enable user to lookup weather forcast by zip code
  api_key = 'd6b8d93ff31fcb6c452e79a30916a33d' #API key provide by Openweather 
  base_url = 'http://api.openweathermap.org/data/2.5/forecast'#base URL for to complete the URL for GET request
  country_codeQuestion = True
  while country_codeQuestion: #while loop to ask user for country code input, if user puts in anything but integers then an error occurs
    country_code = input(str('Please type in a county code.'))
    if country_code != int:
      print("Country code can only be numbers. Please try again") 
    else:
    break
  zip_codeQuestion = True
  while zip_codeQuestion: #while loop to ask user for zip code input, if user puts in anything but integers then an error occurs
    zip_code = input(str("Pleas type in a zip code."))
    if country_code != int:
      print("Zip code can only be numbers. Please try again") 
    else:
    break
  zip_url = base_url + '?zip=' + zip_code + ',' + country_code + '&appid=' + api_key) #user inputs for country and zip code complete the zip URL for the GET request, the GET request will pull the weather forecast information from Openweather's server/website
  zip_response = request.get(zip_url)
  y = zip_response.json()
  if["cod"] !='404': #if statement that prints requested weather information as long as the connection is established and not returning an error else a response is provided to tell the user the connections was not established or the zip code does not exists
    print(response.status_code)
    v =y["main"]
    date_list = y[f"list.dt"]
    main_list = y[f"list.main"]
    weather_list = y[f"list.weather"]
    city_name = y[f"city"]
    print (date_list + main_list + weather_list + city name)
  else:
    print("'Response was unsuccessful or zip code was not found'")
  

def weather_city(): #function used to enable user to lookup weather forcast by city name
  api_key = 'd6b8d93ff31fcb6c452e79a30916a33d'
  base_url = 'http://api.openweathermap.org/data/2.5/forecast'
  weather_city = True 
  while weather_city: #while loop to ask user for city name input
    city_name = input(str('Please type in the city name.'))
    city_url = base_url + '?q=' + city_name + '&appid=' + api_key)
    city_response = request.get(city_url) #user inputs for city name complete the zip URL for the GET request, the GET request will pull the weather forecast information from Openweather's server/website
    x = city_response.json()
    if["cod"] !='404': #if statement that prints requested weather information as long as the connection is established and not returning an error else a response is provided to tell the user the connections was not established or the zip code does not exists
      print(city_name)
      print(response.status_code)
      w =x["main"]
      date_list = x[f"list.dt"]
      main_list = x[f"list.main"]
      weather_list = x[f"list.weather"]
      city_name = x[f"city"]
      print (date_list + main_list + weather_list + city name)
    else:
      print('Response was not successful or city does not exist.')

def main(): #the main function consolidates all other functions for execution   
  playAgain = True 
  while playAgain: #set while loop for play again feature to enable user to continue looking up forecast as long as the user inputs yes. 
    display_Intro() #calls and executes display_intro function 
    weather_Question() #calls and executes weather_Question function
    if weather_Question = 1: #if statement to return the define functions based on the input of the user, 1 for zip code and 2 for city name
      return weather_zip()
    else:
      return weather_city()
    print('\nDo you want to lookup another forecast? (yes or no)')
	  playAgain = input()
	  if playAgain not in ("yes", "y"):
		  print("Thanks for playing")
		  break

if __name__ == "__main__": #Conditional statement that evaluates to true executing the main function
  main()