""" 네이버 뉴스 특정 키워드를 포함하는, 특정 날짜 이전 기사 내용 크롤러(정확도순 검색)
    python [모듈 이름] [키워드] [가져올 페이지 숫자]
    한 페이지에 기사 10개
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import sys
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.request import Request, urlopen
from wordcloud import WordCloud
from krwordrank.word import summarize_with_keywords


TARGET_URL_BEFORE_PAGE_NUM = "http://www.hanaif.re.kr/search.do?"
TARGET_URL_BEFORE_KEWORD = 'menuId=MN1000&tabMenuId=N&srchKey='
TARGET_URL_REST = '&pageNo='

texts = []

# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL):
    for i in range(page_num):
        current_page_num = 1 + i

        URL_with_page_num = URL[:] + str(current_page_num)
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        for title in soup.find_all('div', 'news_wrap api_ani_send'):
            title_link = title.select('a')
            article_URL = title_link[4]['href']
        print(article_URL)


# 메인함수
def main(argv):
    if len(argv) != 2:
        print("python [모듈이름] [키워드]")
        return
    keyword = argv[1]
    #page_num = int(argv[2])
    file_name = keyword + '_keyword.png'
    target_URL = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEWORD \
                 + quote(keyword) + TARGET_URL_REST
    get_link_from_news_title(1, target_URL)

if __name__ == '__main__':
    main(sys.argv)
