import requests
from bs4 import BeautifulSoup


url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html5lib')


for el in soup.find_all(class_="content-section"):
    print (el.get_text( strip = True))
    print ("\n")

