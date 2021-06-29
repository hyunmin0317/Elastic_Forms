""" 네이버 뉴스 특정 키워드를 포함하는, 특정 날짜 이전 기사 내용 크롤러(정확도순 검색)
    python [모듈 이름] [키워드] [가져올 페이지 숫자] [결과 파일명]
    한 페이지에 기사 15개
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


TARGET_URL_BEFORE_PAGE_NUM = "https://search.naver.com/search.naver?"
TARGET_URL_BEFORE_KEWORD = 'where=news&query='
TARGET_URL_REST = '&start='

texts = []

# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL):
    for i in range(page_num):
        current_page_num = 1 + i * 10

        URL_with_page_num = URL[:] + str(current_page_num)
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        for title in soup.find_all('div', 'news_wrap api_ani_send'):
            title_link = title.select('a')
            article_URL = title_link[4]['href']

        get_text(article_URL)

# 기사 본문 내용 긁어오기 (위 함수 내부에서 기사 본문 주소 받아 사용되는 함수)
def get_text(URL):
    source_code_from_URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(source_code_from_URL), 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    texts.append(text)

# 키워드를 찾는 함수
def find_keyword(file_name):
    font_path = './NanumFont/NanumBarunGothic.ttf'
    stopwords = {"\',", "함수", "_flash_removeCallback()", "flash", "//", "\'\\n", "\'\\","10", "11", "17", "20", "30", "29일", "위한", "것으로", "있다."}
    keywords = summarize_with_keywords(texts, min_count=5, max_length=10,
                                       beta=0.85, max_iter=10, stopwords=stopwords)

    krwordrank_cloud = WordCloud(
        font_path=font_path,
        width=800,
        height=800,
        background_color="white"
    )

    krwordrank_cloud = krwordrank_cloud.generate_from_frequencies(keywords)
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(krwordrank_cloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()
    fig.savefig(file_name)

    for word, score in sorted(keywords.items(), key=lambda x: -x[1])[:30]:
        print('%8s:\t%.4f' % (word, score))

# 메인함수
def main(argv):
    if len(argv) != 3:
        print("python [모듈이름] [키워드] [가져올 페이지 숫자]")
        return
    keyword = argv[1]
    page_num = int(argv[2])
    file_name = keyword + '_keyword.png'
    target_URL = TARGET_URL_BEFORE_PAGE_NUM + TARGET_URL_BEFORE_KEWORD \
                 + quote(keyword) + TARGET_URL_REST

    get_link_from_news_title(page_num, target_URL)
    find_keyword(file_name)

if __name__ == '__main__':
    main(sys.argv)