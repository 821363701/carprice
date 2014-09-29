__author__ = 'yuxizhou'

import requests
from bs4 import BeautifulSoup

fp = open('carking001', 'w')

for page in range(1, 98):
    try:
        r = requests.get('http://www.carking001.com/car/list.aspx?page=' + str(page))
        r.encoding = 'utf-8'

        soup = BeautifulSoup(r.text)
        items = soup.find('ul', class_='carList').find_all('li')

        for i in items:
            price = i.contents[3].contents[5].contents[7].text.strip()
            if price == u'':
                price = i.contents[3].contents[5].contents[5].text.strip()
            car = i['title'] + u'\t' + price + u'\t' + \
                  i.contents[3].contents[3].contents[1].text.strip().split('.........................')[1].strip() + u'\t' + \
                  i.contents[3].contents[3].contents[3].text.strip().split('.................................')[1].strip() + u'\n'
            fp.write(car.encode('utf-8'))
    except Exception, e:
        print e
        print page

fp.close()
