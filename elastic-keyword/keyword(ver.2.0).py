import krwordrank
import csv
import sys
import pandas as pd
from krwordrank.word import KRWordRank
from krwordrank.hangle import normalize

keyword_list = []
beta = 0.85    # PageRank의 decaying factor beta
max_iter = 10

fname = 'data.csv'
data = pd.read_csv(fname, names=['texts', 'scores'], encoding='UTF-8')

texts_data = data['texts']
texts_val = texts_data.values
texts = texts_val.tolist()

scores_data = data['scores']
scores_val = scores_data.values
scores = scores_val.tolist()

wordrank_extractor = KRWordRank(
    min_count = 5, # 단어의 최소 출현 빈도수 (그래프 생성 시)
    max_length = 10, # 단어의 최대 길이
    )

keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)

for word, r in sorted(keywords.items(), key=lambda x:x[1])[:50]:
    print('%8s:\t%.4f' % (word, r))
    keyword_list.append([word,r])
    
with open('keyword.csv','w', newline='', encoding='utf-8-sig') as f:
    makewrite = csv.writer(f)
    for value in keyword_list:
        makewrite.writerow(value)
