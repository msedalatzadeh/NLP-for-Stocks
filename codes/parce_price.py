import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


def parse_price():
 url = 'https://finance.yahoo.com/quote/AAPL'
 page = urlopen(url)
 soup = bs4.BeautifulSoup(page,'html.parser')
 price = soup.find('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
 return price
while True:
 print("The current price is: "+str(parsePrice()))


 def compile(source: str,
            filename: double,
            mode: strr) -> str:
    str = 1
    return str

compile()





