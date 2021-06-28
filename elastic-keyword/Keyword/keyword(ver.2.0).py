from krwordrank.word import summarize_with_keywords
import pandas as pd

csv = pd.read_csv('data.csv', names=['data', 'weight'], encoding='UTF-8')
data = csv['data']

data_val = data.values
texts = data_val.tolist()

# stopwords : 키워드에서 제거될 단어
stopwords = {'자료:', '20', '따른', '수는', '경우', '-1', '주:', '것으로', '대한'}

keywords = summarize_with_keywords(texts, min_count=5, max_length=10,
    beta=0.85, max_iter=10, stopwords=stopwords)

#print(keywords)

for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
    print('%8s:\t%.4f' % (word, r))
