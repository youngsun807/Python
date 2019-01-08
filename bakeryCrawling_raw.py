import time
import re
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #https://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements
import requests
import lxml.html
import re
import time
import numpy as np
import pandas as pd
# 예외 처리를 위한 모듈
from selenium.webdriver.support import expected_conditions as EC


# 드라이버 켠다
driver = webdriver.Chrome("C:/driver/chromedriver.exe")
url='https://store.naver.com/restaurants/list?filterId=s13479410&menu=%EB%B9%B5%EC%A7%91&query=%EC%84%9C%EC%B4%88%EC%97%AD%20%EB%A7%9B%EC%A7%91'
driver.get(url)


# 검색 로직
'''driver.find_element_by_id('query').send_keys("서초역 빵집")
time.sleep(1)
driver.find_element_by_id('search_btn').click() #검색 버튼 클릭
time.sleep(1)'''


def scrape_list_page(response):
    #print(response)
    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)
    boxItems = soup.select(".list_place_col1 .list_item_inner")
    for boxItem in boxItems:
        url = boxItem.select('div.info_area > div.tit > span')[0].find('a')['href'] #'div.info_area > div.tit > span > a'
        yield url  
   

def scrape_detail_page(response, count):
    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)
    length = root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_menu > div > ul > li")
    print(length)
    menus = {}
    for i in range(len(length)-1):
        print(length[i].text_content())
        allMenu = (length[i].text_content()).split('원')
        menus[allMenu[1]] = allMenu[0]

    if count!=9 and count!=19:
        bakeryInfo= {
            'URL' : response.url,
            'Title': root.cssselect("#content > div:nth-child(1) > div.biz_name_area > strong")[0].text_content(),
            'Review':root.cssselect("#content > div:nth-child(1) > div.biz_name_area > div > div > a")[0].text_content(),
            'Menus':menus,
            'Address':root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_address > div > ul > li:nth-child(1) > span")[0].text_content(),
            'Tell':root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztel > div")[0].text_content(),
            'Opentime':re.search('([0-9]+[:][0-9]+)\s[-]\s([0-9]+[:][0-9]+)', root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztime > div > div > div > div > span > span")[0].text_content()).group(1),
            'Closetime':re.search('([0-9]+[:][0-9]+)\s[-]\s([0-9]+[:][0-9]+)', root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztime > div > div > div > div > span > span")[0].text_content()).group(2),
        }
        return bakeryInfo
    elif count==9 and count!=19:
        bakeryInfo= {
            'URL' : response.url,
            'Title': root.cssselect("#content > div:nth-child(1) > div.biz_name_area > strong")[0].text_content(),
            'Review':root.cssselect("#content > div:nth-child(1) > div.biz_name_area > div > div > a")[0].text_content(),
            'Menus':menus,
            'Address':root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_address > div > ul > li:nth-child(1) > span")[0].text_content(),
            'Tell':root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztel > div")[0].text_content(),
            'Opentime':re.search('([0-9]+[:][0-9]+)\s[-]\s([0-9]+[:][0-9]+)', root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztime > div > a > div:nth-child(1) > div:nth-child(2) > span > span")[0].text_content()).group(1),
            'Closetime':re.search('([0-9]+[:][0-9]+)\s[-]\s([0-9]+[:][0-9]+)', root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztime > div > a > div:nth-child(1) > div:nth-child(2) > span > span")[0].text_content()).group(2)
        }
        return bakeryInfo
    else:
        bakeryInfo= {
            'URL' : response.url,
            'Title': root.cssselect("#content > div:nth-child(1) > div.biz_name_area > strong")[0].text_content(),
            'Review':root.cssselect("#content > div:nth-child(1) > div.biz_name_area > div > div > a")[0].text_content(),
            'Menus':menus,
            'Address':root.cssselect("#content > div:nth-child(2) > div > div > div.list_item.list_item_address > div > ul > li:nth-child(1) > span")[0].text_content(),
            'Tell':root.cssselect("#content > div:nth-child(2) > div > div > div.list_item.list_item_biztel > div")[0].text_content(),
            'Opentime':re.search('([0-9]+[:][0-9]+)\s[-]\s([0-9]+[:][0-9]+)', root.cssselect("#content > div:nth-child(2) > div > div > div.list_item.list_item_biztime > div > a > div:nth-child(1) > div:nth-child(1) > span.time.highlight > span")[0].text_content()).group(1),
            'Closetime':re.search('([0-9]+[:][0-9]+)\s[-]\s([0-9]+[:][0-9]+)', root.cssselect("#content > div:nth-child(2) > div > div > div.list_item.list_item_biztime > div > a > div:nth-child(1) > div:nth-child(1) > span.time.highlight > span")[0].text_content()).group(2)
        }
        return bakeryInfo

def blog_url_scrape(response):
    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)
    url = root.cssselect('#content > div:nth-child(1) > div.biz_name_area > div > div > a')[0].get('href')
    response = session.get(url)
   
    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)

    for a in root.cssselect('#panel03 > div > ul > li > div > div > div.tit > a'):
        blogURL = a.get('href')
        yield blogURL



def blog_scrape_review(blog, blog_response):
    contentInfo = []
    driver.get(blog)
    driver.switch_to.frame('mainFrame')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    blogID = re.sub(r'.*?//.*?/.*?/', '', blog)
    blogTag = '#post-view' + blogID
    content_list = soup.select(blogTag)[0].select('p')
    contents = [i.text for i in content_list]
    for word in contents:
        word = word.strip()
        word = re.sub('[^ ㄱ-ㅣ가-힣]+','', word)
        contentInfo.append(word)

    reviewInfo = {
        'blog_url':blog,
        'content':' '.join(contentInfo)
    }
    return reviewInfo



try:
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    session = requests.Session()
    response = session.get(url)
    #print(response)
    urls = scrape_list_page(response)
    count = 1
    print(count,'번째  =====================================================')
    for url in urls:
        time.sleep(1)
        #print(url)
        response = session.get(url)
        bakeryInfo = scrape_detail_page(response, count)
        blogs = blog_url_scrape(response)
        reviewAll = []
        
        for blog in blogs:
            time.sleep(1)
            if('blog' in blog):
                blog_response = session.get(blog)
                reviewInfo = blog_scrape_review(blog, blog_response)
                reviewAll.append(reviewInfo)
            else:
                pass

        bakeryInfo['ReviewList'] = reviewAll
        print(bakeryInfo)
        count +=1
        

except Exception as e:
    print("페이지 파싱 에러", e)
finally:
    time.sleep(3)
    driver.close()
