#!/usr/bin/python
#coding:utf-8

import requests
import urllib2
from bs4 import BeautifulSoup
import re
import time

new_book_html = urllib2.urlopen("http://10.1.18.2/cgi-bin/DispNewBook?v_file=2016.01.04.&v_pagenum=20000")
new_book_Obj = BeautifulSoup(new_book_html,"html.parser",from_encoding="GB18030")
for tr in new_book_Obj.find("table").tr.next_siblings:
        td= tr.findAll("td")
        print   u"题名:" + td[0].get_text() \
              + u" 作者:" + td[1].get_text() \
              + u" 索引号:" + td[2].get_text() \
              + u" 出版社:" + td[3].get_text() \
              + u" 页码:" + td[4].get_text() \
              + u" 价格:" + td[5].get_text() \
              + u" Book ID: " + re.findall(r", (.+?)[\)）]", str(td[6].a.attrs['href']))[0]
