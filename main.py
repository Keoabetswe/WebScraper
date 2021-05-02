import requests 
from bs4 import BeautifulSoup
import csv

# request to the page to be scrapped
URL = "https://www.takealot.com/rubiks-3x3-cube-new-version/PLID41679453/"
headers =  { 
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="").get_text()
price = soup.find(id="").get_text()

print(price.strip())

# write to csv
with open('takealotscraper.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    for item in title:
        writer.writerow([item])