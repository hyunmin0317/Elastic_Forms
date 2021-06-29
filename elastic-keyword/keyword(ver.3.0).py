import csv
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from krwordrank.word import summarize_with_keywords

keyword_list = []
data = pd.read_csv('data.csv', names=['word', 'score'], encoding='UTF-8')

texts_data = data['word']
texts_val = texts_data.values
texts = texts_val.tolist()

# stopwords : 키워드에서 제거될 단어
stopwords = {'자료:', '10', '20', '그림', '따른', '수는', '경우', '-1', '주:', '것으로', '대한'}

keywords = summarize_with_keywords(texts, min_count=5, max_length=10,
    beta=0.85, max_iter=10, stopwords=stopwords)

#print(keywords)

for word, score in sorted(keywords.items(), key=lambda x:-x[1])[:50]:
    print('%8s:\t%.4f' % (word, score))
    keyword_list.append([word, score])

with open('keyword2.csv','w', newline='', encoding='utf-8-sig') as f:
    makewrite = csv.writer(f)
    for value in keyword_list:
        makewrite.writerow(value)

# Set your font path
font_path = './NanumFont/NanumBarunGothic.ttf'

krwordrank_cloud = WordCloud(
    font_path = font_path,
    width = 800,
    height = 800,
    background_color="white"
)

krwordrank_cloud = krwordrank_cloud.generate_from_frequencies(keywords)
fig = plt.figure(figsize=(10, 10))
plt.imshow(krwordrank_cloud, interpolation="bilinear")
plt.axis('off')
plt.show()
fig.savefig('./keyword2.png')




