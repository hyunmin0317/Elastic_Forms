import csv
import pandas as pd
from krwordrank.word import summarize_with_keywords

keyword_list = []
data = pd.read_csv('data.csv', names=['texts', 'scores'], encoding='UTF-8')

texts_data = data['texts']
texts_val = texts_data.values
texts = texts_val.tolist()

# stopwords : 키워드에서 제거될 단어
#stopwords = {'자료:', '20', '따른', '수는', '경우', '-1', '주:', '것으로', '대한'}

keywords = summarize_with_keywords(texts, min_count=5, max_length=10,
    beta=0.85, max_iter=10)#, stopwords=stopwords)

#print(keywords)

for word, r in sorted(keywords.items(), key=lambda x:x[1])[:50]:
    print('%8s:\t%.4f' % (word, r))
    keyword_list.append([word,r])

with open('keyword.csv','w', newline='', encoding='utf-8-sig') as f:
    makewrite = csv.writer(f)
    for value in keyword_list:
        makewrite.writerow(value)
