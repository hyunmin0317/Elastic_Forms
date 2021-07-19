from urllib import request
import wget
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

URL = 'https://github.com/jooeungen/coronaboard_kr/blob/master/kr_daily.csv'
data = []
columns = []


source_code_from_URL = urllib.request.urlopen(URL)
soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

for tr in soup.find_all('tr', class_='js-file-line'):
    th = tr.select('th')
    for column in th:
        columns.append(column.text)

    td = tr.select('td')
    tds = []
    for d in td:
        if (not d.has_attr('class')):
            if(d.text==''):
                tds.append(0)
            else:
                tds.append(int(d.text))
    tds.append(0)
    data.append(tds)
columns.append('today')
data[0] = [20200120,0,0,0,0,0,0,0]

# today = data[2][1] - data[1][1]

# i 는 1 부터 len(data)-1
for i in range(1, len(data)):
    today = data[i][1] - data[i-1][1]
    data[i][7] = today

df = pd.DataFrame(data, columns=columns)
df.to_csv('kr-daily.csv', index=False, encoding='cp949')
print('저장했습니다.\n')