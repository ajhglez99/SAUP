import sys
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

def open_csv():
    """Open .csv file to write the reviews"""
    # default path to file to store data
    path_to_file = r'.\datasets\reviews.csv'

    # Open the file to save the review
    csvFile = open(path_to_file, 'a', encoding="utf-8")
    csv_output = csv.writer(csvFile, lineterminator='\n')

    return csv_output

def read_url_list():
    """Read URLs list to scrap from file"""
    # default tripadvisor website of restaurant
    filename = r'.\datasets\tripadvisor_urls.list'

    with open(filename) as file_object:
        urls = [line.rstrip() for line in file_object]

    return urls

def get_driver():
    """Create a driver for browsing access"""
    #pass the absolute path of the Firefox binary
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    options.headless = True 

    # Import the webdriver
    driver = webdriver.Firefox(
        executable_path = r'.\drivers\geckodriver.exe',
        options=options)

    return driver

def get_data(driver, csv_output, num_page):
    """scrap reviews data from urls"""

    for i in range(0, num_page):
            # expand the review 
            time.sleep(2)
            # Click the "expand review" link to reveal the entire review.
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

                csv_output.writerow([date, rating, title, opinion, 'Restaurant'])
            
            # change the page
            try:
                driver.find_element("xpath", './/a[@class="nav next ui_button primary"]').click()
            except:
                print('no "next" button found')
                break

def custom_scraper(num_page = 400):
    """restaurant review scraper from tripadvisor"""

    csv_output = open_csv()
    urls = read_url_list()
    driver = get_driver()

    for url in urls:
        driver.get(url)
        print(f"parcing {url}")
        
        get_data(driver, csv_output, num_page)

        time.sleep(2)

    driver.close()

if __name__ == "__main__":
    custom_scraper()