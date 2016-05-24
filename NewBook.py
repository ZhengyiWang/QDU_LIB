#!/usr/bin/python
# coding:utf-8

import requests
import urllib2
from bs4 import BeautifulSoup
import re
import time

LIB_HOST = 'http://10.1.18.2/'

API = '/cgi-bin/IlasNewBook'

new_book_date_html = urllib2.urlopen(LIB_HOST + API)
new_book_date_Obj = BeautifulSoup(new_book_date_html, "html.parser", from_encoding="GB18030")
date_Obj = new_book_date_Obj.find("table", {"width": "90%"}).findAll("td")

for date in date_Obj:
    print u"新书通报目录:" + date.b.get_text() + u" Date_Link:" + date.a.attrs['href'][24:34]
