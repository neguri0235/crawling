# urllib 로 다운 받은 다음에 . 다운받은 곳에서 encoding 을 가지고 옴

import re
import sys
from urllib.request import urlopen

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

# 우선 저장
byte_contents = f.read()

#정규식을이용하며 charset을 추출함

scanned_text = byte_contents[:1024].decode('ascii', errors = 'replace')
# r 을 넣는 이유는 raw 문자열로 처리하면 백슬래시를 사용하지 않아도 됨
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

# 정규식 표현에 맞으면, 그 charset으로. 그렇지 않으면 utf-8로
if match:
    #group(1)을 한다는 것은 정규식에서 ( ) 로 감싼 부분을 리턴한다는 뜻
    encoding = match.group(1)
else:
    encoding = 'utf-8'

print('encoding: ', encoding, file=sys.stderr)

text = byte_contents.decode(encoding)
print(text)