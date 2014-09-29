__author__ = 'yuxizhou'

import requests
from bs4 import BeautifulSoup

fp = open('renrenche', 'w')

for page in range(1, 12):
    r = requests.get('http://www.renrenche.com/bj/ershouche/p' + str(page))
    r.encoding = 'utf-8'

    soup = BeautifulSoup(r.text)
    items = soup.find_all('li', class_='list-item')

    for i in items:
        car = i.contents[3].contents[0] + u'\t' + i.contents[5].contents[0].text + u'\t' + \
              i.contents[7].contents[0] + u'\t' + i.contents[7].contents[2] + u'\n'
        fp.write(car.encode('utf-8'))

fp.close()