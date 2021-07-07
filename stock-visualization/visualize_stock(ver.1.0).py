from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()
samsung = pdr.get_data_yahoo('005930.KS', start='2021-01-01')

#print(samsung)
#print(samsung.index)
#print(samsung.columns)

plt.plot(samsung.index, samsung.Close, 'b', label='Samsung Electronics')
plt.show()