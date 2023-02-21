import os
import sys
import urllib.request
import requests 
from collections import Counter
import numpy as np 
import pandas as pd
import re
import datetime
import streamlit as st


### 세팅 

st.title('하이퍼링크 삽입')
st.write('네이버 기사 api 활용해서 기사 링크 삽입하기')




    
###### api사용해서 불러오기 

client_id = "7BluQlzfnBbWg8ALRkpq"
client_secret = "ZTCPVEwdLc"
url = 'https://openapi.naver.com/v1/search/news.json'



# display_num : 한 번에 표시할 검색 결과 개수(기본값: 10, 최댓값: 100)
def Keword( key, display_num):
      # keyword = key
      headers = { 'X-Naver-Client-Id': client_id
                , 'X-Naver-Client-Secret': client_secret}
      params = {'query': key
                , 'display':display_num
                ,'sort': 'sim' }

      r = requests.get(url, params = params, headers = headers).json()['items']

      return r 


## 데이터프레임에 나눠담기
def info(places):
    PubDate = []
    Title = []
    Link = [] 
    Description = []

    for place in places:

        PubDate.append(place['pubDate'])
        Title.append(place['title'])
        Link.append(place['originallink'])      
        Description.append(place['description'])
         

    ar = np.array([PubDate, Title, Link, Description ]).T
    dtf = pd.DataFrame(ar, columns=['PubDate', 'Title', 'Link', 'Description' ])

    return dtf


####가져오기 

search = Keword('streamlit',100)
news = info(search) 


# 기본 정제 
def basic_clear(text):
    for i in range(len(text)) : 
        text[i] = text[i].replace('<b>', '')
        text[i] = text[i].replace('</b>', '')
        text[i] = text[i].replace('&apos;', '') 
        text[i] = text[i].replace('&quot;', '') 
    return text

basic_clear(news['Title'])
basic_clear(news['Description'])


# 날짜형으로 형변환

news['PubDate'] = pd.to_datetime(news['PubDate'], format='%a, %d %b %Y  %H:%M:%S', exact=False) # 수정완료!

# news['PubDate'] = 
news['PubDate'] = news['PubDate'].dt.strftime('%y.%m.%d') 

news = news.sort_values(by='PubDate', ascending = False)
st.write("   ")



for i in range(len(news['Title'])):
    txt='{d} [{txt}]({link})'.format(d =  news['PubDate'].iloc[i], txt = news['Title'].iloc[i], link = news['Link'].iloc[i])
    st.write(txt) 

    
    

