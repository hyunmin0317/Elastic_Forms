from selenium import webdriver

# 접속할 웹 사이트 주소
url = 'http://www.hanaif.re.kr/boardDetail.do?hmpeSeqNo=34840'        
# 크롬 드라이버로 크롬 켜기
driver = webdriver.Chrome('.\chromedriver.exe')


element = find_element_by_class_name("javascript:downloadItem(34840, 101122)")
element.click()


# driver.get(url)                 # 저장한 url 주소로 이동
