from urllib import request
import wget
from bs4 import BeautifulSoup
import urllib.request



URL = 'https://github.com/jooeungen/coronaboard_kr/blob/master/kr_daily.csv'

source_code_from_URL = urllib.request.urlopen(URL)
soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

for tr in soup.find_all('tr', class_='js-file-line'):
    td = tr.select('td')
    print(td)
