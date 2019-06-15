import sys
from urllib.request import urlopen

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

# f의 타입, 상태 및 헤더 정보를 확인(200)
print(type(f))
print(f.status)
print(f.getheader('Content-Type'))

# HTTP 헤더 기반으로 인코딩 방식을 추출( 없을때는 utt-8을 기본으로)
encoding = f.info().get_content_charset(failobj = "utf-8")
print('encoding: ', encoding, file=sys.stderr)

# 추출한 인코딩 방식으로 디코딩
text = f.read().decode(encoding)

# text 를 redirection 하면 파일로 저장됨
print(text)