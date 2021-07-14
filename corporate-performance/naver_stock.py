import sys
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

def get_code(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
    code = code.strip()

    if(code == 'Series([], )'):
        return -1
    else:
        return code


# 크롤링 함수
def save_data(stock):
    code = get_code(code_df, stock)
    if(code==-1):
        print('상장된 법인이 아닙니다.\n')
        return

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
    df.to_csv(stock+'.csv', index=False, encoding='cp949')
    print(stock+'의 기업실적분석 데이터를 저장했습니다.\n')


# 메인 함수
def main(argv):
    if len(argv) != 2:
        print("python [모듈이름] [주식 이름]")
        return
    name = argv[1]
    save_data(name)


if __name__ == '__main__':
    code_df = code_df[['회사명', '종목코드']]
    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    code_df.code = code_df.code.map('{:06d}'.format)
    main(sys.argv)