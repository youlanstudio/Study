# -*- coding: utf-8 -*-

import requests

guess_url = 'http://www.heibanke.com/lesson/crawler_ex01/'
wrong_info = '您输入的密码错误, 请重新输入'

for i in range(30):
    guess_info = {'username':'God', 'password':str(i)}

    result = requests.post(guess_url, data=guess_info).text
    if wrong_info in result:
        print('Wrong password : %d' % i)
    else:
        print("password is %d" % i)
        break
