#!/usr/bin/python
#coding:utf-8

import requests
import urllib2
from bs4 import BeautifulSoup
import re
import time

LIB_HOST = 'http://10.1.18.2/'

# 题名
TITLE = 'a'

# 显示数量

PageNum = 20

# 书目查询
API = '/cgi-bin/IlaswebBib?v_index=TITLE&v_value=' + TITLE + '&FLD_DAT_BEG=&FLD_DAT_END=&v_pagenum=' + unicode(PageNum) + '&v_seldatabase=0&v_LogicSrch=0'


new_book_html = urllib2.urlopen(LIB_HOST+API)
new_book_Obj = BeautifulSoup(new_book_html,"html.parser",from_encoding="GB18030")

for tr in new_book_Obj.find("table",{"bgcolor":"#008080"}).tr.next_siblings:
	try:
		td= tr.find_all("td")
		print   u"题名:" + td[0].get_text() \
					+ u" 作者:" + td[1].get_text() \
					+ u" 出版社:" + td[2].get_text() \
					+ u" 页码:" + td[3].get_text() \
					+ u" 价格:" + td[4].get_text() \
					+ u" 索引号:" + td[5].get_text() \
					+ u" Book_Link: " + td[6].a.attrs['href']
	except: 
		pass
