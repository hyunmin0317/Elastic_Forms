from urllib import request

def download(url, fname):
    mem = request.urlopen(url).read()
    with open(fname, mode="wb") as f:
        f.write(mem)
        print("저장되었습니다.")

if __name__ == '__main__':
    site = 'http://www.wfri.re.kr'
    src = '/inc/down.php?dir=BOARD&file_name=202106_162443873696514_2.pdf&rename=(20210624)%20Industry%20Watch%202021-06%20%EA%B5%AD%EB%82%B4%20%EA%B7%B8%EB%A6%B0%EC%8A%A4%ED%83%81(Green%20Stock)%20%EC%84%B1%EA%B3%BC%EC%99%80%20%EC%8B%9C%EC%82%AC%EC%A0%90.pdf' 
    fname = 'text.pdf'
    download(site+src, fname)
