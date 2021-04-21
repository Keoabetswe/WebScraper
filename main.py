imports requests 
from bs4 import BeautifulSoup

# request to the page to be scrapped
mainContent = requests.get("https://takealot.com/")
    print(mainContent.text)