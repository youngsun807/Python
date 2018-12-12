import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #https://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost',27017)
db = conn['ysDB']
collection = db['books']

main_url = "https://www.thinkcontest.com/"
driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
driver.implicitly_wait(10)


partDict = {}
for i in range(1,21):
    partKey = driver.find_element_by_css_selector("div.cate-box > ul.cate-list.col-2.cate-list-1.on > li:nth-child({}) > a".format(i)).text
    partDict[partKey] = i

print("*****찾을 수 있는 분야 목록*****")
cnt = 0
for key, value in partDict.items():
    cnt +=1
    if(cnt%4 == 0):
        print(value, ".", key, end='\n')
        print("-----------------------------------------------------------------------------------------------------------------")
    else:
        print(value, ".", key, end=' || ')
print('\n')
part = int(input("어떤 분야를 선택하시겠습니까? 원하시는 분야의 번호를 입력해주세요."))

if((part<=20) and (0<part)):
    driver.find_element_by_css_selector("div.cate-box > ul.cate-list.col-2.cate-list-1.on > li:nth-child({}) > a".format(part)).click()
else:
    print("해당 분야는 없습니다. 다시 시작하세요.")
    SystemExit


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "all-contest"))
    )
except Exception as e:
    print("검색 page 로드시 class 속성이 all-contest를 얻으려는 중 예외 발생 : ", e)


driver.implicitly_wait(10) # seconds
collection.drop()
print("현재 DB 내의 테이블 목록은 다음과 같습니다", db.list_collection_names())


def scrapePart():
    try:
        startpage = int(input("시작하고 싶은 페이지는? "))
        lastpage = int(input("끝나는 페이지는? "))

        if(startpage%5!=0):
            if(5<startpage):
                for i in range(0,startpage//5):
                    pageSelector(8).click()
                if(startpage%5==1):
                    pass
                else:
                    for i in range(1,startpage%5):
                        pageSelector(i+3).click()
            elif((startpage<=5) and (0<startpage)):
                if(startpage%5==1):
                    pass
                else:
                    for i in range(1,startpage%5):
                        pageSelector(i+3).click()
            else:
                print("해당 페이지는 없습니다. 다시 시작해주세요.")
                SystemExit
        else:
            if(startpage==5):
                pageSelector(4).click()
                pageSelector(5).click()
                pageSelector(6).click()
                pageSelector(7).click()
            else:
                for i in range(0,(startpage//5)-1):
                    pageSelector(8).click()

                pageSelector(4).click()
                pageSelector(5).click()
                pageSelector(6).click()
                pageSelector(7).click()

        books=[]    
        for page in range(startpage, lastpage+1): 
            print("======================================================================================================================== ")
            print("{} 페이지로 이동!!!".format(page))

            soup = BeautifulSoup(driver.page_source, "lxml" )
            boxItems = soup.select("#main .all-contest tbody tr")
            count = 0
            
            for boxItem in boxItems:
                title = boxItem.select("a")[0].text
                url = boxItem.find("a")['href']
                url = "https://www.thinkcontest.com" + url
                host = boxItem.select("td")[1].string
                state = boxItem.select("td")[2].text
                state = state.replace(" ", "")
                state = state.replace("\n", "")    
                period = boxItem.select("td")[3].text

                print("공모명 : ", title)
                print("링크 : ", url)
                print("주최 : ", host)
                print("진행사항 : ", state)
                print("진행기간 : ", period)
                print("============================== ")

                books.append({"title":title, "url":url, "host":host, "state":state, "period":period})
                collection.insert({"title":title, "url":url, "host":host, "state":state, "period":period})
 
            pageNum = driver.find_element_by_css_selector("div.paging-wrap > div > a:nth-child({})".format((page%5)+3))

            if('#' not in str(pageNum)):
                if(page%5!=0):
                    pageNum.click()
                else:
                    pageSelector(8).click()
            elif('#' in str(pageNum)):
                break
            else:
                break

    except Exception:
        pass
        
    finally:
        print('\n')
        wishList = int(input("어떤 종류의 공모전을 보고 싶습니까? 1.마감  2.마감임박  3.접수중  4.접수예정"))
        if(wishList==1):
            print("마감 공모전 목록입니다.")
            end = collection.find({"state":{"$regex":"마감$", "$options":"x"}})
            count = 0
            for i in end:
                print(i)
                count +=1
            print("총 {}개의 공모전이 있습니다.".format(count))
            print("\n")
        elif(wishList==2):
            print("마감 임박 공모전 목록입니다.")
            end = collection.find({"state":{"$regex":"임박", "$options":"x"}})
            count = 0
            for i in end:
                print(i)
                count +=1
            print("총 {}개의 공모전이 있습니다.".format(count))
            print("\n")
        elif(wishList==3):
            print("접수중인 공모전 목록입니다.")
            end = collection.find({"state":{"$regex":"접수중$", "$options":"x"}})
            count = 0
            for i in end:
                print(i)
                count +=1
            print("총 {}개의 공모전이 있습니다.".format(count))
            print("\n")
        elif(wishList==4):
            print("접수예정인 공모전 목록입니다.")
            end = collection.find({"state":{"$regex":"예정", "$options":"x"}})
            count = 0
            for i in end:
                print(i)
                count +=1
            print("총 {}개의 공모전이 있습니다.".format(count))
            print("\n")
        else:
            print("해당 종류는 없습니다. 다시 시작하세요.")
        time.sleep(3)
        driver.close()


def pageSelector(num):
    if(num<=3):
        print("해당 페이지로는 넘길 수 없습니다.")
    else:
        return driver.find_element_by_css_selector("div.paging-wrap > div > a:nth-child({})".format(num))


if __name__=="__main__":
    scrapePart()