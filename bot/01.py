import sys
import io
import requests
from bs4 import BeautifulSoup

# 한글 깨짐 문제
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 주소를 통해 전체 페이지를 저장한다.
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190612&screencodes=&screenratingcode=&regioncode='
html = requests.get(url)

# 디버깅 목적의 프린트. html 안에 어떤 것이 들어 있는지 확인
#print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

# 개발자 도구를 통해서 html 페이지내에 어떤 정보를 가지고 올것인지.
#print(soup.select_one('body > div > div.sect-showtimes > ul > li:nth-child(1) > div > div.info-movie > a > strong'))


title_liset = soup.select('div.info-movie')
for i in title_liset:
    print(i.select_one('a > strong').text.strip())

