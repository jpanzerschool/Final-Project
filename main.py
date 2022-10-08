#import Modules
import json, requests

#Set variables
response = "y"
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "6a124073e077b092a6ed00ec193fba98"

#Function for asking city/zip 
def city():
  return input("What's your city or zip code?")

#Function for verifying connection and getting temp information
def data(user_city):
  url = f"{base_url}?q={user_city}&units=imperial&APPID={appid}"
  try:
    response = requests.get(url)
    print("Successful connection!")
  except:
    print("Connection Failed")
  rough_data = response.json()
  #print(rough_data)
  return rough_data

#Function for making sure data is valid
def valid_data(information):
  while information["cod"] == "404":
    print("Invalid city or zip code")
    information = data(city())
  temp = information["main"]["temp"]
  temp_max = information["main"]["temp_max"]
  name = information["name"]
  return temp, temp_max, name

#Function to print temperatures
def temperatures(temp, temp_max, name):
  print(f"City: {name}")
  print(f"The current temp is: {temp}")
  print(f"The current max temp is: {temp_max}")
  


#Function to re-run the program
def user_response():
  return input("Do you want to run the program again? y or n")

#Function combining all functions
def main(response):
  while response == "y" or "yes":
    rough_information = data(city())
    temp, temp_max, name = valid_data(rough_information)
    temperatures(temp, temp_max, name)
    response = user_response()
  print("Have a great day!")

#Starting the program
main(response)