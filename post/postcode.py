import urllib, urllib.parse, urllib.request
from bs4 import BeautifulSoup
from post.models import Address
import re
#from xml.etree.ElementTree import parse

def search_zipcode(values):
    SEARCH_ZIPCODE_URL = 'http://biz.epost.go.kr/KpostPortal/openapi'
    SEARCH_ZIPCODE_KEY = 'da1560600eced7ff11469937540929'
 
    values = dict(regkey=SEARCH_ZIPCODE_KEY, target='postNew', query=str(values).encode('euc-kr'))
    params = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(SEARCH_ZIPCODE_URL, params)
    req.add_header('Accept-language', 'ko')
    req.add_header('User-agent', 'Mozilla/5.0')
    res = urllib.request.urlopen(req)
    result = res.read().decode('utf-8')
    soup = BeautifulSoup(result,'html.parser')
    addr = soup('address')
    parsed=[]

    for i in addr:
    	si=str(i)[18:]
    	parsed.append(si[:-13])

    return parsed