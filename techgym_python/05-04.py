#**************************************************************************
#05-04
#**************************************************************************

import requests

url = 'https://news.yahoo.co.jp/'

res = requests.get(url)

print(res.text)

