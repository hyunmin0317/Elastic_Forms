from urllib import request
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

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
            if (d.text == ''):
                tds.append(0)
            else:
                tds.append(int(d.text))
    tds.append(0)
    data.append(tds)
columns.append('today')
data[0] = [20200120, 0, 0, 0, 0, 0, 0, 0]

# today = data[2][1] - data[1][1]

# i 는 1 부터 len(data)-1
for i in range(len(data)):
    if i != 0:
        today = data[i][1] - data[i - 1][1]
        data[i][7] = today
    data[i][0] = pd.to_datetime(data[i][0], format='%Y%m%d')

date = []
today = []

for i in range(len(data)):
    date.append(data[i][0])
    today.append(data[i][7])

name = 'covid19-KR'
plt.plot_date(date, today,linestyle ='solid')
plt.gcf().set_size_inches(8, 6)
plt.tight_layout()
fig = plt.gcf()
plt.title(name)
plt.show()
fig.savefig('./'+name+'.png')

# df = pd.DataFrame(data, columns=columns)
# df.to_csv('kr-daily.csv', index=False, encoding='cp949')
# print('저장했습니다.')