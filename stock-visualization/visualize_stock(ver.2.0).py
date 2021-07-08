import csv
import sys

import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

stocks = {}

def save_stock(path):
    f = open(path, 'r', encoding='utf-8')
    reader = csv.reader(f)
    stock_csv = {row[0]:(row[1]+'.KS') for row in reader}
    f.close()
    return stock_csv

def visualize_stock(name, start):
    code = stocks.get(name)
    if code == None:
        print(name+"는 주식 종목에 존재하지 않습니다.")
    else:
        stock = pdr.get_data_yahoo(code, start=start)
        plt.plot(stock.index, stock.Close, 'b', label=name)
        fig = plt.gcf()
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
    stocks = save_stock('KR-Stock.csv')
    yf.pdr_override()
    main(sys.argv)