import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html5lib')


for el in soup.find_all("h2", class_="story-heading"):
    print (el.get_text( strip = True))
    print ("\n")
