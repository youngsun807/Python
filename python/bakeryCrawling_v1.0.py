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
import pymongo
from pymongo import MongoClient
# 예외 처리를 위한 모듈
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/driver/chromedriver.exe")

def scrape_list_page(response, soup):
    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)
    boxItems = soup.select(".list_place_col1 .list_item_inner")
    for boxItem in boxItems:
        first_span = boxItem.select('div.info_area > div.tit > span')[0]
        url = first_span.find('a')['href']
        yield url



class TextExtractor(object):
    def __init__(self, root, response, soup):
        self.root = root
        self.response = response
        self.soup = soup


    def get_bakeray_info(self):
        print(3)
        bakery_info = {
            'url' : self.response.url,
            'title': self.get_title(),
            'review': self.get_review(),
            'Menus': self.get_menus(),
            'Address': self.get_address(),
            'Tell': self.get_tell(),
            'Opentime': self.get_open_time(),
            'Closetime': self.get_close_time()
        }
        print(4)
        return bakery_info

    def get_title(self):
        return self.root.cssselect("#content > div:nth-child(1) > div.biz_name_area > strong")[0].text_content()

    def get_review(self):
        try:
            return self.root.cssselect("#content > div:nth-child(1) > div.biz_name_area > div > div > a")[0].text_content()
        except Exception:
            return ''

    def get_menus(self):
        menus = {}
        try:
            length = self.root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_menu > div > ul > li")
            for i in range(len(length)-1):
                allMenu = (length[i].text_content()).split('원')
                menus[allMenu[1]] = allMenu[0]
            return menus
        except Exception:
            return menus

    def get_address(self):
        try:
            return self.root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_address > div > ul > li:nth-child(1) > span")[0].text_content()
        except Exception:
            return ''

    def get_tell(self): 
        try:
            return self.root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztel > div")[0].text_content()
        except Exception:
            return '' 


    def get_open_time(self):
        try:
            opentime = self.root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztime > div > div > div > div > span > span")[0].text_content()
            opentime = re.search(r'([0-9]+[:][0-9]+)\s[-]\s([0-9]+[:][0-9]+)', opentime).group(1)
            return opentime
        except Exception:
            return ''
   
    def get_close_time(self):
        try:
            closetime = self.root.cssselect("#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_biztime > div > div > div > div > span > span")[0].text_content()
            closetime = re.search(r'([0-9]+[:][0-9]+)\s[-]\s([0-9]+[:][0-9]+)', closetime).group(2)
            return closetime
        except Exception:
            return ''
                                    

def scrape_detail_page(response, count, soup):
    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)
    print(1)
    te = TextExtractor(root, response, soup)
    print(2)
    return te.get_bakeray_info()


def blog_url_scrape(response, session):
    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)

    first_a = root.cssselect('#content > div:nth-child(1) > div.biz_name_area > div > div > a')[0]
    url = first_a.get('href')
    response = session.get(url)

    root = lxml.html.fromstring(response.text)
    root.make_links_absolute(response.url)

    for a in root.cssselect('#panel03 > div > ul > li > div > div > div.tit > a'):
        blogURL = a.get('href')
        yield blogURL



def blog_scrape_review(blog, blog_response):
    content_Info = []
    driver.get(blog)
    driver.switch_to.frame('mainFrame')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    blog_ID = re.sub(r'.*?//.*?/.*?/', '', blog)
    blog_Tag = '#post-view' + blog_ID
    content_list = soup.select(blog_Tag)[0].select('p')
    contents = [i.text for i in content_list]
    
    for word in contents:
        word = word.strip()
        word = re.sub('[^ ㄱ-ㅣ가-힣]+','', word)
        content_Info.append(word)

    review_Info = {
        'blog_url':blog,
        'content':' '.join(content_Info)
    }
    return review_Info
        


def main():
    pagecount = 1
    try:
        while(True):
            url = 'https://store.naver.com/restaurants/list?filterId=s13479410&menu=%EB%B9%B5%EC%A7%91&page={}&query=%EC%84%9C%EC%B4%88%EC%97%AD%20%EB%A7%9B%EC%A7%91'.format(pagecount)
            driver.get(url)
        
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            session = requests.Session()
            response = session.get(url)


            urls = scrape_list_page(response, soup)

            count = 1
            Info = []
            cnt = []
            for url in urls:
                time.sleep(1)

                response = session.get(url)
                bakery_info = scrape_detail_page(response, count, soup)
                try:
                    blogs = blog_url_scrape(response, session)
                    review_all = []

                    for blog in blogs:
                        time.sleep(1)
                        if 'blog' in blog:
                            blog_response = session.get(blog)
                            review_Info = blog_scrape_review(blog, blog_response)
                            review_all.append(review_Info)
                        else:
                            pass
                except Exception:
                    review_all = []

                bakery_info['review_result'] = review_all
                Info.append(bakery_info)

                cnt.append(count)
                print(bakery_info)
                print(count,'번째  =====================================================')
                count += 1
            if("current" in str(soup.select("#container > div.placemap_area > div.list_wrapper > div > div.list_area > div > div.pagination_inner")[0])):
                pagecount +=1
            else:
                print("크롤링 끝********************************************************")
                break
    except Exception as e:
        print("페이지 파싱 에러", e)

    finally:
        time.sleep(3)
        driver.close()


if __name__ == '__main__':
    main()
    
    
    # 쥬피터 노트북에서 따로 실행
    # conn = MongoClient('localhost',27017)
    # db = conn['BakeryData']
    # collection = db['bakery_seocho']
    # collection.insert_many(df2.to_dict('records'))
