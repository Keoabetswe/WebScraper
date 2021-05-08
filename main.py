import requests 
from bs4 import BeautifulSoup
# import csv

# request to the page to be scrapped
URL = "https://www.amazon.com/Winning-Moves-5027-Rubiks-Cube/dp/B004FG0ZWI/"
headers =  { 
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice")

print(title.strip())
print(price)

# write to csv
# with open('takealotscraper.csv','w') as csvfile:
#     writer = csv.writer(csvfile)
#     for item in title:
#         writer.writerow([item])