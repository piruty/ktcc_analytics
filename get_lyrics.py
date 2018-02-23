import requests
from bs4 import BeautifulSoup
import time

base_url = 'https://www.uta-net.com'
ktcc_artist_link = 'artist/492/'
r = requests.get('{}/{}'.format(base_url, ktcc_artist_link))
soup = BeautifulSoup(r.text, 'html.parser')

with open('lyrics.txt', 'w') as f:
    for link in soup.find_all("td", attrs={"class": "side td1"}):
        r = requests.get('{}/{}'.format(base_url, link.find('a').get('href')))
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.title.text)
        f.write(soup.find('div', attrs={'id': 'kashi_area'}).text)
        f.write('\n')
        time.sleep(5)
