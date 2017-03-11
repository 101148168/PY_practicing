import requests
from bs4 import BeautifulSoup
import re

res_list = ['https://www.superdry.com/us/mens/hoodies/details/67283/nyc-hoodie--black',
            'http://www.superdry.com/mens/jackets/details/63532/mountain-mark-sherpa-coat-navy']

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def _only_money(l):
    m = re.split('>', l)
    n = re.split('<', m[1])
    return n[0]

def _get_jacket_name(url):  
    name = re.split('/', url)
    return name[-1]
    
for url in res_list:
    res = requests.get(url, headers = head)
    soup=BeautifulSoup(res.text, "html.parser")
    name = _get_jacket_name(url)
    for i in soup.find_all('div', class_="price-info spaced-v"):
        for l in i.find_all('span', class_="price font_bold"):
            money = _only_money(str(l))
            print(name,"=", money)

