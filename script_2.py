import requests
import cloudscraper
from bs4 import BeautifulSoup as soup


def get_data_one():
    my_url = 'https://bournemouth.cylex-uk.co.uk/company/parkside-motor-company-26942573.html'
    scraper = cloudscraper.CloudScraper()

# Grabbing the page despite it's security systems:
    req = scraper.get(my_url)
    req.close()

    soup_one = soup(req.content, 'html5lib')

    container_address = soup_one.findAll('span', {'class':'cp-details-label'})
    company = soup_one.find('span', {'id': 'cntct-name'})
    comp = company.text
    container_data = soup_one.findAll('div', {'class':'col-sm-8'})

    # Opening the .CSV file:
    # filename = 'data_three.csv'
    # f = open(filename, 'w')
    headers = "Data about the object we care: \n"
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
    # In case if you want to change 'mobile' layout to vertical, uncomment next two lanes:
    # mob = mobile[0:20]
    # f.write('\n\n' + mob + ', ' + '\n\n')
    mobille = mobile[0:7]
    number = mobile[8:20]
    f.write('\n\n' + mobille + ', ' + number + '\n\n')

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
    description_one =  soup_one.findAll('span', {'itemprop':'name'})
    f.write("\n "+ comp + ", Can be found in following Categories: \n ,")
    for descript in description_one:
        desc = descript.text
        f.write( desc + ', \n ,')


my_url = 'https://bournemouth.cylex-uk.co.uk/car%20dealers.html'

def get_objects(my_url):
    scraper = cloudscraper.CloudScraper()

# Grabbing the page despite it's security systems:
    req = scraper.get(my_url)
    req.close()

    soup_one = soup(req.content, 'html5lib')

    container_address = soup_one.findAll('div', {'class':'row address-with-medal'})
    container_field = soup_one.findAll('span', {'class':'block bold h4'})

    for container in container_field:
        field = container.text 
        f.write(field + '\n ')


    for address in container_address:
        addres = address.text 
        f.write(addres + ', ')

my_url_list = ['https://bournemouth.cylex-uk.co.uk/car%20dealers-2.html','https://bournemouth.cylex-uk.co.uk/car%20dealers-3.html', 'https://bournemouth.cylex-uk.co.uk/car%20dealers-4.html', 'https://bournemouth.cylex-uk.co.uk/car%20dealers-5.html', 'https://bournemouth.cylex-uk.co.uk/car%20dealers-6.html', 'https://bournemouth.cylex-uk.co.uk/car%20dealers-7.html', 'https://bournemouth.cylex-uk.co.uk/car%20dealers-8.html', 'https://bournemouth.cylex-uk.co.uk/car%20dealers-9.html', ]

def get_many_car_dealers():
    for my_url in my_url_list:
        get_objects(my_url)

bourne_list = ['https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=1&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=2&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=3&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=4&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=5&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=6&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=7&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=8&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=9&dst=&sUrl=&cUrl=bournemouth', 'https://www.cylex-uk.co.uk/s?q=&c=bournemouth&z=&p=10&dst=&sUrl=&cUrl=bournemouth' ]

def get_companies():
    for my_url in bourne_list:
        get_objects(my_url)


header = '\n\n Data about other car dealers in the area: \n\n'
header_two = '\n\n Data about other companies in the Bournemouth area: \n\n'

filename = 'data_three.csv'
f = open(filename, 'w')

get_data_one()
f.write(header)

get_many_car_dealers()
f.write(header_two)
get_companies()


f.close()