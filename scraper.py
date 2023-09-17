import requests
from bs4 import BeautifulSoup
import csv

def scrapeData(location, type):

    # google map search 
    search = "https://www.google.com/maps/search/"
    searchUrl= search+ location + "+" + type
    response = requests.get(searchUrl)
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract business data
    businessData = []
    for input in soup.find_all('div', class_='section-result'):
        #class_ in HTML parsing is an attribute used to select elements based on their CSS classes and has nothing to do with python keyword class
        name = input.find('h3', class_='section-result-title').text
        address = input.find('span', class_='section-result-location').text
        phone = input.find('span', class_='section-result-phone-number').text
        emailAddress = input.find("span", class_="section-result-email").text
        businessData.append([name, address, phone, emailAddress])

    # store the scraped data in a CSV file
    with open('leads.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Address", "Phone", "Email ID"])
        writer.writerows(businessData)
    return businessData
