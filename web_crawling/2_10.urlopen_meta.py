import re
import sys
from urllib.request import urlopen

f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

# 우선 저장
byte_contents = f.read()

#정규식을이용하며 charset을 추출함

scanned_text = byte_contents[:1024].decode('ascii', errors = 'replace')

match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

# 정규식 표현에 맞으면, 그 charset으로. 그렇지 않으면 utf-8로
if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8'

print('encoding: ', encoding, file=sys.stderr)

text = byte_contents.decode(encoding)
print(text)