from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv

driver = webdriver.Chrome() 
driver.get('https://restaurants.subway.com/de/deutschland/be/berlin');
sleep(10) 
restaurantList = driver.find_elements(By.CLASS_NAME, "Directory-listTeaser")
print(type(restaurantList))
print(restaurantList[0].find_element(By.CLASS_NAME, 'c-address-street-1').get_attribute('innerHTML'))
print(restaurantList[0].find_element(By.CLASS_NAME, 'c-address-postal-code').get_attribute('innerHTML'))
print(restaurantList[0].find_element(By.CLASS_NAME, 'c-address-city').get_attribute('innerHTML'))

with open('Restaurants.csv', mode='a', newline='') as outputFile:
    restaurantCSV = csv.writer(outputFile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    #restaurantCSV.writerow(['restaurant', 'street', 'zip', 'city', 'country'])
    restaurantName = 'Subway'
    country = 'Germany'
    for restaurant in restaurantList:
        #restaurant = restaurant.get_attribute('innerHTML')
        street = restaurant.find_element(By.CLASS_NAME, 'c-address-street-1').get_attribute('innerHTML')
        zipCode = restaurant.find_element(By.CLASS_NAME, 'c-address-postal-code').get_attribute('innerHTML')
        city = restaurant.find_element(By.CLASS_NAME, 'c-address-city').get_attribute('innerHTML')
        restaurantCSV.writerow([restaurantName, street, zipCode, city, country])

driver.close()

