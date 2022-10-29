import sys
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# default path to file to store data
path_to_file = r'.\datasets\reviews.csv'

# default number of scraped pages
num_page = 400

# default tripadvisor website of restaurant
filename = r'.\datasets\tripadvisor_urls.list'

# open the file to save the review
csv_file = open(path_to_file, 'a', encoding="utf-8")
csv_writer = csv.writer(csv_file, lineterminator='\n')

# open the file with the url list to scrap
with open(filename) as file_object:
    urls = [line.rstrip() for line in file_object]

# pass the absolute path of the Firefox binary
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.headless = True 

# Import the webdriver
driver = webdriver.Firefox(
    executable_path = r'.\drivers\geckodriver.exe',
    options=options)

for url in urls:
    driver.get(url)

    print(f"parcing {url}")

    for i in range(0, num_page):
        # expand the review 
        time.sleep(2)
        # click the "expand review" link to reveal the entire review.
        try:
            driver.find_element("xpath", "//span[@class='taLnk ulBlueLinks']").click()
        except:
            print('no "expand comment" button found')
        
        container = driver.find_elements("xpath", ".//div[@class='review-container']")

        for j in range(len(container)):
            title = container[j].find_element("xpath", ".//span[@class='noQuotes']").text
            date = container[j].find_element("xpath", ".//span[contains(@class, 'ratingDate')]").get_attribute("title")
            rating = container[j].find_element("xpath", ".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
            opinion = container[j].find_element("xpath", ".//p[@class='partial_entry']").text.replace("\n", " ")

            csv_writer.writerow([date, rating, title, opinion, 'Restaurant'])
        
        # change the page
        try:
            driver.find_element("xpath", './/a[@class="nav next ui_button primary"]').click()
        except:
            print('no "next" button found')
            break
    
    time.sleep(2)

driver.close()