from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

def visualize_stock(name, code, start):

    stock = pdr.get_data_yahoo(code, start=start)
    plt.plot(stock.index, stock.Close, 'b', label=name)
    plt.show()

if __name__ == '__main__':
    yf.pdr_override()
    visualize_stock('Samsung Electronics', '005930.KS', '2021-01-01')