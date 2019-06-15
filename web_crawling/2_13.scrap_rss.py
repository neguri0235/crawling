import os
from xml.etree import ElementTree
path = os.getcwd()

# parse 함수를 ElementTree 객체를 만듬
tree = ElementTree.parse( path + '/web_crawling/rss.xml')

# getroot( )를 통해 root를 가지고 옴
root = tree.getroot()

# findall() 로 요소를 추출하고 태그를 찾음

for item in root.findall('channel/item/description/body/location/data'):
    tm_ef = item.find('tmEf').text
    tmn = item.find('tmn').text
    tmx = item.find('tmx').text
    wf = item.find('wf').text
    print(tm_ef, tmx, wf)
