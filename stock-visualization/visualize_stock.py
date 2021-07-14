import sys
import matplotlib
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

yf.pdr_override()
code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

def get_code(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
    code = code.strip()
    code += '.KS'
    return code

def visualize_stock(name, start):
    code = get_code(code_df, name)
    if code == None:
        print(name+"는 주식 종목에 존재하지 않습니다.")
    else:
        stock = pdr.get_data_yahoo(code, start=start)
        plt.plot(stock.index, stock.Close, 'b', label=name)
        fig = plt.gcf()
        plt.title(name)
        plt.show()
        fig.savefig(name+'.png')

def main(argv):
    if len(argv) != 3:
        print("python [모듈이름] [주식 이름] [시작일]")
        return
    name = argv[1]
    start = argv[2]
    visualize_stock(name, start)

if __name__ == '__main__':
    code_df = code_df[['회사명', '종목코드']]
    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
    code_df.code = code_df.code.map('{:06d}'.format)
    matplotlib.rcParams['font.family'] = 'Malgun Gothic'
    matplotlib.rcParams['axes.unicode_minus'] = False
    main(sys.argv)