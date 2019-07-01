# 정규식을 이용해서 주소를 찾는 법

import re
import os
from html import unescape
path = os.getcwd()
# 2.10에서 다운받은 html을 그대로 사용함
with open(path + '/web_crawling/dp.html') as f:
    html = f.read()

# re.findall() 을 사용해서 도서 하나에 해당하는 html을 추출
for partial_html in re.findall(r'<td class="left"><a.*?</td>',html,re.DOTALL):
    # 도서의 url 을 추출
    url = re.search(r'<a href="(.*?)">',partial_html).group(1)
    url = 'http://www.hanbit.co.kr' + url

    # 태그를 제거해서 도서의 제목만 추출
    title = re.sub(r'<.*?>','',partial_html)
    title = unescape(title) # unescape을 쓰면 특수 문자같은 것이 제거된다.
    print('url: ',url)
    print('title:', title)
    print('----')


