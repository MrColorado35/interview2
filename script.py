import requests
import cloudscraper
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://bournemouth.cylex-uk.co.uk/company/parkside-motor-company-26942573.html'

scraper = cloudscraper.CloudScraper()
# scraper = cloudscraper.create_scraper()
# req = requests.get(my_url)
req = scraper.get(my_url)

soup_one = soup(req.content, 'html5lib')
print(soup_one.prettify())

# print(scraper.get(soup_one.prettify()))
