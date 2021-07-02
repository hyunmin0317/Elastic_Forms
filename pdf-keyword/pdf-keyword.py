import csv
import matplotlib.pyplot as plt
from tika import parser
from krwordrank.word import summarize_with_keywords
from wordcloud import WordCloud

pdf_path = "input.pdf"
font_path = './NanumFont/NanumBarunGothic.ttf'
stopwords = {'자료:', '주1:'}


# PDF 파일에서 텍스트를 추출
raw_pdf = parser.from_file(pdf_path)
contents = raw_pdf['content']
contents = contents.strip()
texts = contents.split('\n')

# 키워드 추출
keywords = summarize_with_keywords(texts, min_count=5, max_length=10,
    beta=0.85, max_iter=10, stopwords=stopwords)

# 키워드 시각화
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
fig.savefig('output.png')

# 키워드 결과 출력
for word, r in sorted(keywords.items(), key=lambda x:x[1])[:50]:
    print('%8s:\t%.4f' % (word, r))
