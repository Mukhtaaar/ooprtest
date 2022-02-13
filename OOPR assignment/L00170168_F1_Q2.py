import requests
from bs4 import BeutifulSoup
url = "http://192.168.196.128/"
resp = request.get(url)
soup = BeautifulSoup(resp. content, 'html.parser')
print(soup.prettify())