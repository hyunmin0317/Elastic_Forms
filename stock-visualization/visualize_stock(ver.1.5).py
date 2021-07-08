import csv

stock = {}

def save_stock(path):
    f = open(path, 'r', encoding='utf-8')
    reader = csv.reader(f)
    stock_csv = {row[0]:(row[1]+'.KS') for row in reader}
    f.close()
    return stock_csv

def search_stock(name):
    if name in stock:
        print(stock[name])
    else:
        print('Key not exist!')

if __name__ == '__main__':
    stock = save_stock('KR-Stock.csv')
    search_stock('카카오')
    search_stock('상명')
