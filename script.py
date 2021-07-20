import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://bournemouth.cylex-uk.co.uk/company/parkside-motor-company-26942573.html'
req = requests.get(my_url)

soup_one = soup(req.content, 'html5lib')
print(soup_one.prettify())