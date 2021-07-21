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

soup_one = soup(req.content, 'html5lib')
# print(soup_one.h1) tests if it works

# print(scraper.get(soup_one.prettify()))

container = soup_one.find('div', {'id': 'company-address-container'})
container_address = soup_one.findAll('span', {'class':'cp-details-label'})
company = soup_one.find('span', {'id': 'cntct-name'})
comp = company.text
container_data = soup_one.findAll('div', {'class':'col-sm-8'})

filename = 'data_three.csv'
f = open(filename, 'w')
headers = "Our data: \n"
f.write(headers)

# contain = container_address[0]
for contain in container_address:
    address = contain.text 
    # address_item = address + ': '
    f.write(address + ', ')
    # print(address_item)
f.write('\n' + comp + ', ')
for conts in container_data[:3]:
    con_data = conts.text
    f.write( con_data + ', ')
    # f.write('\n')
    # print(con_data)
#     address_title = container_address[0].text
#     address = container_address[1].text
#     address_text = container.div.div.div.text




# Getting mobile number:
container_mobile = soup_one.findAll('div', {'id': 'secondary-details'} )
mobile = container_mobile[0].text 

# mob = mobile[0:20]
# f.write('\n' + mob + ', ' + '\n')
mobille = mobile[0:7]
number = mobile[8:20]
f.write('\n' + mobille + ', ' + number + '\n')


opening = soup_one.find('div', {'id': 'opening-hours-mini'})

# Getting days and hours of the working week:
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
f.close()

