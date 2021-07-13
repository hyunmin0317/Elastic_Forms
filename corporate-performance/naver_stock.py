"""네이버 뉴스 기사 웹 크롤러 모듈"""
 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# 긁어 올 URL
URL = 'https://finance.naver.com/item/main.nhn?code=005930'
 
 
# 크롤링 함수
def get_text(URL):
    source_code_from_URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})    
    soup = BeautifulSoup(urlopen(source_code_from_URL), 'lxml', from_encoding='UTF-8')
    table = soup.find('table', {'class': 'tb_type1 tb_num tb_type1_ifrs'}):
    tbody = table.select('tbody')
    print(tbody)


# 메인 함수
def main():
    get_text(URL)

if __name__ == '__main__':
    main()

