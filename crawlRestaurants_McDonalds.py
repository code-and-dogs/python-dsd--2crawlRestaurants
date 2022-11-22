from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv

driver = webdriver.Chrome() 
driver.get('https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/berlin');
sleep(10) 
restaurantList = driver.find_elements(By.CLASS_NAME, "ubsf_sitemap-location-address")

with open('Restaurants.csv', mode='a', newline='') as outputFile:
    restaurantCSV = csv.writer(outputFile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    restaurantCSV.writerow(['restaurant', 'street', 'zip', 'city', 'country'])
    restaurantName = 'McDonalds'
    country = 'Germany'
    for restaurant in restaurantList:
        restaurant = restaurant.get_attribute('innerHTML')
        street = restaurant.split(",")[0]
        zipCode = restaurant.split(",")[1][1:6]
        city = restaurant.split(",")[1][7:]
        restaurantCSV.writerow([restaurantName, street, zipCode, city, country])
        
driver.close()
