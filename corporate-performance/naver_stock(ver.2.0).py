import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

def get_code(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
    code = code.strip()
    return code


# 크롤링 함수
def save_data(code):
    URL = 'https://finance.naver.com/item/main.nhn?code='+code
    data = []
    columns = ['주요재무정보']
    source_code_from_URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(source_code_from_URL), 'lxml', from_encoding='UTF-8')
    table = soup.find('table', {'class': 'tb_type1 tb_num tb_type1_ifrs'})
    thead = table.select_one('thead')
    trs = thead.select('tr')
    for tr in trs:
        if (not tr.has_attr('class')):
            for i in range(10):
                th = tr.select('th')[i].text
                th = th.replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
                columns.append(th)

    tbody = table.select_one('tbody')
    trs = tbody.select('tr')
    for tr in trs:
        tds = tr.select('th')[0].text
        for i in range(10):
            td = tr.select('td')[i].text
            td = td.replace(u'\xa0', u'').replace(u'\t', u'').replace(u'\n', u'')
            tds += ('/' + td)
        data.append(tds.split('/'))
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('삼성전자.csv', index=False, encoding='cp949')


# 메인 함수
def main():
    code = get_code(code_df, '삼성전자')
    save_data(code)


if __name__ == '__main__':
    code_df = code_df[['회사명', '종목코드']]
    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    code_df.code = code_df.code.map('{:06d}'.format)
    main()