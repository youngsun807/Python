import time
import re
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #https://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_url = "https://www.thinkcontest.com/"


driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
driver.implicitly_wait(10) # seconds

elem = driver.find_element_by_name("sw")
elem.clear()
elem.send_keys(input("검색하고 싶은 공모전을 입력하시오 : "))

btn_search = driver.find_element_by_css_selector("button.btn-search")
btn_search.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result-section"))
    )
except Exception as e:
    print("검색 page 로드시 class 속성이 result-section를 얻으려는 중 예외 발생 : ", e)

driver.find_element_by_css_selector("section.result-section > a").click()
driver.implicitly_wait(10) # seconds


def scrapeKeyword():
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
                print("잘못된 페이지를 입력하였습니다. 다시 시작해주세요.")
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
        a=[]    
        for page in range(startpage, lastpage+1): 
            print("======================================================================================================================== ")
            
            driver.implicitly_wait(5)
            print("{} 페이지로 이동!!!".format(page))
            soup = BeautifulSoup(driver.page_source, "lxml" )
            boxItems = soup.select("#main .all-contest tbody tr")
           
            for boxItem in boxItems: 
                title = boxItem.select("a")[0].text
                url = boxItem.find("a")['href']
                url = "https://www.thinkcontest.com" + url
                host = boxItem.select("td")[1].string

                term = boxItem.select("td")[2].text
                term = term.replace(" ", "")
                term = term.replace("\n", "")
                
                term2 = boxItem.select("td")[3].text

            
                print("공모명 : ", title)
                print("링크 : ", url)
                print("주최 : ", host)
                print("진행사항 : ", term)
                print("진행기간 : ", term2)
                print("============================== ")
                                
                a.append({'title':title, 'url':url, 'host':host , 'term':term, 'term2':term2})
                save('a.db', a)    
                      
            pageNum = driver.find_element_by_css_selector("div.paging-wrap > div > a:nth-child({})".format((page%5)+3))

            if('#' not in str(pageNum)):
                if(page%5!=0):
                    pageNum.click()
                else:
                    driver.find_element_by_css_selector("div.paging-wrap > div > a:nth-child({})".format(8)).click()
            elif('#' in str(pageNum)):
                break
            else:
                SystemExit
        
    except Exception:
        pass
    finally:
        print("\n")
        wishList = int(input("어떤 종류의 공모전을 보고 싶습니까? 1.마감  2.마감임박  3.접수중  4.접수예정"))
        print("\n")
        if(wishList==1):
            print("마감 공모전 목록입니다.")
            conn = sqlite3.connect('a.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM a where term="마감"')
            count = 0
            for row in cur:
                print(row)
                count +=1
            print("총 {}개의 공모전이 있습니다.".format(count))
            print("\n")
        elif(wishList==2):
            print("마감 임박 공모전 목록입니다.")
            conn = sqlite3.connect('a.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM a where term like "마감임박%"')
            count = 0
            for row in cur:
                print(row)
                count +=1
            print("총 {}개의 공모전이 있습니다.".format(count))
            print("\n")
        elif(wishList==3):
            print("접수중인 공모전 목록입니다.")
            conn = sqlite3.connect('a.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM a where term like "접수중%"')
            count = 0
            for row in cur:
                print(row)
                count +=1
            print("총 {}개의 공모전이 있습니다.".format(count))
            print("\n")
        elif(wishList==4):
            print("접수예정인 공모전 목록입니다.")
            conn = sqlite3.connect('a.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM a where term="접수예정"')
            count = 0
            for row in cur:
                print(row)
                count +=1
            print("총 {}개의 공모전이 있습니다.".format(count))
            print("\n")
        else:
            print("해당 종류는 없습니다. 다시 시작하세요.")
        time.sleep(3)
        driver.close()
        


def save(db_path, a):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS a')
    

    c.execute('''
        CREATE TABLE a(
            title VARCHAR2(20),
            url VARCHAR2(20),
            host VARCHAR2(20),
            term VARCHAR2(20),
            term2 VARCHAR2(20)
        )
    ''')
    c.executemany('INSERT INTO a VALUES (:title, :url, :host, :term, :term2)', a)
    conn.commit()
    conn.close()


def pageSelector(num):
    if(num<=3):
        print("해당 페이지로는 넘길 수 없습니다.")
    else:
        return driver.find_element_by_css_selector("div.paging-wrap > div > a:nth-child({})".format(num))


if __name__ == '__main__':
    scrapeKeyword()