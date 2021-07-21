import requests
import cloudscraper
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://bournemouth.cylex-uk.co.uk/company/parkside-motor-company-26942573.html'


scraper = cloudscraper.CloudScraper()
# scraper = cloudscraper.create_scraper()
# req = requests.get(my_url)

# Grabbinbg the page despite it's security systems:
req = scraper.get(my_url)
# page_html = req.read()
req.close()
# page_soup = soup(page_html, 'html.parser')
# print(page_soup.h1)

soup_one = soup(req.content, 'html5lib')
# print(soup_one.h1) tests if it works

# print(soup_one.prettify())
# print(scraper.get(soup_one.prettify()))


container_address = soup_one.findAll('span', {'class':'cp-details-label'})
container_mobile = soup_one.findAll('div', {'class': 'cp-details-label'} )

print(len(container_address))
print(len(container_mobile))
