# 웹 페이지를 다운로드 받고
# 스크레이핑
# sqlite3에 저장

import re
import sqlite3
import os
from urllib.request import urlopen
from html import unescape

def main():
    path = os.getcwd()
    # 전체를 처리하는 메인 함수
    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
    books = scrape(html)
    save(path + '/web_crawling/books.db', books)

def fetch(url):
    # url 을 따라가서 다운 받고, HTTP 헤더 기반으로 인코딩 형식을 추출
    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj = 'utf-8')
    html = f.read().decode(encoding)
    return html

def scrape(html):

    # 정규식을 이용하여 도서 정보를 추출
    books = []

    for partial_html in re.findall(r'<td class="left"><a.*?</td>',html,re.DOTALL):
        # 도서의 url 을 추출
        url = re.search(r'<a href="(.*?)">',partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url

        # 태그를 제거해서 도서의 제목만 추출
        title = re.sub(r'<.*?>','',partial_html)
        title = unescape(title) # unescape을 쓰면 특수 문자같은 것이 제거된다.
        books.append({'url' : url, 'title' : title})
    
    return books

def save(db_path, books):
    #sqlite 에 저장

    conn = sqlite3.connect(db_path)

    # 커서를 추출
    c = conn.cursor()
    # execute( )로 sql을 실행
    c.execute('DROP TABLE IF EXISTS books')

    #books 테이블 생성
    c.execute(''' CREATE TABLE books (title text, url text) ''')

    # executemany( )를 사용해서 매개변수로 리스트를 지정
    c.executemany('INSERT INTO books VALUES (:title, :url)', books)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()