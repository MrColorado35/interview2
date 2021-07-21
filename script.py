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

container = soup_one.find('div', {'id': 'company-address-container'})
container_address = soup_one.findAll('span', {'class':'cp-details-label'})
container_mobile = soup_one.findAll('div', {'id': 'secondary-details'} )
# contain = container_address[0]
for contain in container_address:
    address = contain.text 
    address_item = address + ', '
    print(address_item)
#     address_title = container_address[0].text
#     address = container_address[1].text
#     address_text = container.div.div.div.text
#     print(address_title)
#     print(address_text)

# for conta in container_mobile:
#     mobille = conta.text
#     mob = mobille + ', '
#     print(mob)

# Getting mobile number:
mobile = container_mobile[0].text 
mobille = mobile[0:7]
number = mobile[8:20]
print(mobille)
print(number)


# print(container.div.div.div.text)
# print(container.prettify())
# print(len(container_address))
# print(len(container_mobile))


opening = soup_one.find('div', {'id': 'opening-hours-mini'})

# Getting days and hours of the working week:
opening_days =  soup_one.findAll('span', {'class':'long-oh-day'})
opening_hours = soup_one.findAll('div', {'class': 'interval-field'}, 'div.span')


for days  in opening_days[:7]:
    day = days.text 
    day_item = day + ': '
    print(day_item)
    if day == 'Saturday' or day == "Sunday":
        print('Closed')
    else:
        for hours in opening_hours[:1]:
            hour = hours.text
            print(hour)


