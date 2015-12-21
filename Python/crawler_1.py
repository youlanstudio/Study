import requests
from bs4 import BeautifulSoup

start_url = 'http://www.heibanke.com/lesson/crawler_ex00/'
next_url = start_url
pages = 0
while True:
    pages += 1
    print('Read Url : %s' % next_url)
    r = requests.get(next_url)
    soup = BeautifulSoup(r.text, 'lxml')

    tips_string = soup.h3.string
    print('Tips : %s' % tips_string)
    next_num = "".join(list(filter(lambda x: x.isdigit(), tips_string)))
    if len(next_num) > 0:
        next_url = start_url + next_num
    else:
        print('Read %d pages' % pages)
        break
