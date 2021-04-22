import requests 
from bs4 import BeautifulSoup

# request to the page to be scrapped
mainContent = requests.get("https://takealot.com/")
print(mainContent.text)

soup = BeautifulSoup(mainContent.text, 'lxml')
title = soup.find('h1', class_='cell auto').get_text()
print(title)

published = soup.find('small', class_='currency plus currency-module_currency_29IIm').get_text.strip()
print(published)