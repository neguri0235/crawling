# lxml 을 이용해서 스크레이핑 하기

import os
import lxml.html

path = os.getcwd()

tree = lxml.html.parse(path + '/web_crawling/full_book_list.html')
html = tree.getroot()

#  cssselect( ) 를 사용하여 a 요소릐 리스트를 추출하고 반복

for a in html.cssselect('a'):
    # href 속성과 글자를 추출
    print(a.get('href'), a.text)
