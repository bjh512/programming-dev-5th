import requests
import urllib, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import xmltodict
from django.forms import ValidationError
#from xml.etree.ElementTree import parse


SEARCH_ZIPCODE_URL = 'http://biz.epost.go.kr/KpostPortal/openapi'
SEARCH_ZIPCODE_KEY = 'da1560600eced7ff11469937540929'
 
def search_zipcode():
    values = dict(regkey=SEARCH_ZIPCODE_KEY, target='postNew', query=str('12345').encode('euc-kr'))
    '''
    params = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(SEARCH_ZIPCODE_URL, params)
    req.add_header('Accept-language', 'ko')
    req.add_header('User-agent', 'Mozilla/5.0')
    res = urllib.request.urlopen(req)
    #print(res)
    result_before = res.read()
    result = res.read().decode('utf-8')
    print(result_before)
    '''

    result = requests.get(SEARCH_ZIPCODE_URL, params=values).text
    #xmltodict
    response = xmltodict.parse(result)
    try:
        print(response['error'])
    except KeyError:
        pass
    else:
        raise ValidationError('[{error_code}] ')
'''
#뷰티플수프
    soup = BeautifulSoup(result,'html.parser')
    print(soup.prettify())
    for item_tag in soup.select('item postcd'):
        print(item_tag.text)
    addr = soup('address')
'''

'''
    parsed=[]
    for i in addr:
    	si=str(i)[18:]
    	parsed.append(si[:-13])
    
    #print(parsed)
    '''

search_zipcode()