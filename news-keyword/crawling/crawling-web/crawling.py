"""네이버 뉴스 기사 웹 크롤러 모듈"""
 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
 
# 출력 파일 명
OUTPUT_FILE_NAME = 'output.txt'
# 긁어 올 URL
URL = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=421&aid=0005443600'
 
 
# 크롤링 함수
def get_text(URL):
    source_code_from_URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})    
    soup = BeautifulSoup(urlopen(source_code_from_URL), 'lxml', from_encoding='UTF-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    return text
 
 
# 메인 함수
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w', encoding='UTF-8')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()

    
if __name__ == '__main__':
    main()
