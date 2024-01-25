from bs4 import BeautifulSoup
import requests

page = requests.get('https://w2.leisurelink.lcsd.gov.hk/leisurelink/application/checkCode.do?flowId=2&lang=EN')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

a = soup.find_all('a')
print(a)
