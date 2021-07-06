import matplotlib.pyplot as plt
import urllib.request
import sys
import os
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.request import Request, urlopen
from urllib import request
from tika import parser
from krwordrank.word import summarize_with_keywords
from wordcloud import WordCloud

WOORI_URL = 'http://www.wfri.re.kr'
TARGET_URL = '/home/sub01_01.php?stxt3=&sse=&skind=TOTAL&sword='
font_path = './NanumFont/NanumBarunGothic.ttf'
stopwords = {'0.','1.','2.','3.','4.','5.','10','20','주:','자료:'}
download_links = []
texts = []

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
    if os.path.exists(fname):
        print("이미 존재하는 파일입니다.")
    else:
        with open(fname, mode="wb") as f:
            f.write(mem)
            print("저장되었습니다.")

# PDF 파일에서 텍스트를 추출
def get_text(path):
    raw_pdf = parser.from_file(path)
    contents = raw_pdf['content']
    contents = contents.strip()
    text = contents.split('\n')
    texts[len(texts):len(texts)] = text

# 키워드를 찾는 함수
def find_keyword(fname):
    keywords = summarize_with_keywords(texts, min_count=5, max_length=10,
                                       beta=0.85, max_iter=10, stopwords=stopwords)

    print('\n\n ' + fname + '키워드 분석 결과')
    for word, score in sorted(keywords.items(), key=lambda x: -x[1])[:30]:
        print('%8s:\t%.4f' % (word, score))

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
    fig.savefig(fname+'.png')

# 메인함수
def main(argv):
    if len(argv) != 2:
        print("python [모듈이름] [키워드]")
        return
    keyword = argv[1]
    path = './' + keyword + '/'
    i = 0
    url = WOORI_URL + TARGET_URL + quote(keyword)
    get_link_from_news_title(url)
    createFolder(path)

    for link in download_links:
        i += 1
        download(link[:83], path + keyword + str(i) + '.pdf')
    for j in range(1, i + 1):
        get_text(path + keyword + str(j) + '.pdf')

    if (texts != []):
        find_keyword(keyword)
    else:
        print(" 검색 결과가 없습니다.")


if __name__ == '__main__':
    main(sys.argv)
