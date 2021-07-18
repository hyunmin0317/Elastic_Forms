import pandas as pd

covid19 = pd.read_html('https://github.com/jooeungen/coronaboard_kr/blob/master/kr_daily.csv', header=0, encoding='utf-8')
print(covid19)