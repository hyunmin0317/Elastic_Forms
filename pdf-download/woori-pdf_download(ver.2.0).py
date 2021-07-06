import csv
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import sys
import os
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.request import Request, urlopen
from urllib import request

WOORI_URL = 'http://www.wfri.re.kr'
TARGET_URL = '/home/sub01_01.php?stxt3=&sse=&skind=TOTAL&sword='
download_links = []

# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(URL):
    
        source_code_from_URL = urllib.request.urlopen(URL)
        soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')

        for title in soup.find_all('td', {'class':'t_left tit'}):
            title_link = title.select('a')
            article_URL = WOORI_URL + title_link[0]['href']
            get_download_link(article_URL)


def get_download_link(URL):
    source_code_from_URL = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(source_code_from_URL), 'lxml', from_encoding='utf-8')
    for item in soup.find_all('div', {'class':'disk'}):
        link = item.select('a')
        download_link = WOORI_URL + link[0]['href']
    download_links.append(download_link)

    
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def download(url, fname):
    mem = request.urlopen(url).read()
    with open(fname, mode="wb") as f:
        f.write(mem)
        print("저장되었습니다.")


if __name__ == '__main__':
    keyword = '코로나'
    path = './'+keyword + '/'
    i = 0
    url = WOORI_URL + TARGET_URL + quote(keyword)
    get_link_from_news_title(url)
    createFolder(path)

    for link in download_links:
        i += 1
        download(link[:83], path+keyword+str(i)+'.pdf')
