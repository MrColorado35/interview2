import requests
import cloudscraper
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://bournemouth.cylex-uk.co.uk/company/parkside-motor-company-26942573.html'


scraper = cloudscraper.CloudScraper()
# scraper = cloudscraper.create_scraper() - alternative to the one above
# code for unprotected websites, where we don't need scraper:
# req = requests.get(my_url)

# Grabbinbg the page despite it's security systems:
req = scraper.get(my_url)
req.close()

soup_one = soup(req.content, 'html5lib')
# tests if it works:
# print(soup_one.h1) 
# print(scraper.get(soup_one.prettify()))

container = soup_one.find('div', {'id': 'company-address-container'})
container_address = soup_one.findAll('span', {'class':'cp-details-label'})
company = soup_one.find('span', {'id': 'cntct-name'})
comp = company.text
container_data = soup_one.findAll('div', {'class':'col-sm-8'})

# Opening the .CSV file:
filename = 'data_three.csv'
f = open(filename, 'w')
headers = "Our data: \n"
f.write(headers)

#getting the address data:
for contain in container_address:
    address = contain.text 
    f.write(address + ', ')

f.write('\n' + comp + ', ')

for conts in container_data[:3]:
    con_data = conts.text
    f.write( con_data + ', ')

# Getting mobile number:
container_mobile = soup_one.findAll('div', {'id': 'secondary-details'} )
mobile = container_mobile[0].text 
# In case if you want to change 'mobile' to vertical, uncomment next two lanes:
# mob = mobile[0:20]
# f.write('\n' + mob + ', ' + '\n')
mobille = mobile[0:7]
number = mobile[8:20]
f.write('\n\n' + mobille + ', ' + number + '\n')


opening = soup_one.find('div', {'id': 'opening-hours-mini'})

# Getting opening days:
opening_days =  soup_one.findAll('span', {'class':'long-oh-day'})
opening_hours = soup_one.findAll('div', {'class': 'interval-field'}, 'div.span')

f.write('Opening time: \n')
for days  in opening_days[:7]:
    day = days.text 
    day_item = day + ': '
    f.write(day_item + ', ')
    if day == 'Saturday' or day == "Sunday":
        f.write('Closed'+ ', \n')
    else:
        for hours in opening_hours[:1]:
            hour = hours.text
            f.write(hour + ', \n')

# Getting company's description:

description = soup_one.find('div', {'class': 'card card-left-padding'})
# print(description.prettify())
# print(description.text)
description_one =  soup_one.findAll('span', {'itemprop':'name'})
# print(description_one)
f.write("\n "+ comp + ", Can be found in following Categories: \n ,")
for descript in description_one:
    desc = descript.text
    f.write( desc + ', \n ,')
# opening_hours = soup_one.findAll('div', {'class': 'interval-field'}, 'div.span')





f.close()