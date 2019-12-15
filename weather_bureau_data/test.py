# -*- coding: utf-8 -*
import pandas as pd

import urllib
from bs4 import BeautifulSoup

import random as rd
import time
import datetime

import Database_uploader  
import Html_content_scratcher
import Data_processor

from selenium import webdriver

stadium_and_station_tabel = pd.read_excel("各球場對應觀測站.xls")

#本研究所關注之期間(2013-03-23~2019-10-17)
start_date = datetime.datetime.strptime("2013-03-23", "%Y-%m-%d").date()
end_date = datetime.datetime.strptime("2019-10-17", "%Y-%m-%d").date()

stadium_city_dict = {"天母":"臺北市","新莊":"新北市","桃園":"桃園市","新竹":"新竹市","台灣國立體育":"臺中市","洲際":"臺中市","雲林":"雲林縣","嘉義市":"嘉義市","台南":"臺南市","澄清湖":"高雄市","屏東":"屏東縣","羅東":"宜蘭縣","花蓮":"花蓮縣"}
station_english_dict = {"斗六":"(Douliou)","鳳山":"(Fongshan)","屏東":"(Pingtung)","羅東":"(Luodong)"}

station_list = list(stadium_and_station_tabel["觀測站"])

#將觀測站設為索引
stadium_and_station_tabel.set_index("觀測站", inplace = True)

#登入各觀測站資料
for station in station_list[19:]:
    #啟動瀏覽器驅動程式
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(3)

    driver.get("https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp")
    time.sleep(3)

    #選擇縣市和觀測站
    driver.find_element_by_xpath("//option[contains(text(),'"+stadium_city_dict[stadium_and_station_tabel.loc[station,"球場"]]+"')]").click()
    if(station[-5:] == "(撤銷站)"):
        driver.find_element_by_xpath("//option[contains(text(),'"+station[0:2]+" "+station_english_dict[station[0:2]]+" "+station[2:]+"')]").click()
    else:
        driver.find_element_by_xpath("//option[contains(text(),'"+station+"')]").click()

    #選擇從哪天的資料開始抓
    station_start_date = datetime.datetime.strptime(stadium_and_station_tabel.loc[station,"資料起始日期"], "%Y-%m-%d").date()
    if(station_start_date < start_date):
        driver.find_elements_by_tag_name('input')[0].send_keys("2013-03-23")
    else:
        driver.find_elements_by_tag_name('input')[0].send_keys(str(station_start_date))
    
    driver.find_element_by_id("doquery").click()
    driver.switch_to.window(driver.window_handles[1])

    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")

    #把每天的表格抓下來並上傳
    root_page = driver.current_url[:-10]
    scratch_date = datetime.datetime.strptime(driver.current_url[-10:], "%Y-%m-%d").date()

    #如果被拒絕連線就再試一次
    while(scratch_date <= end_date):
        quote_page = root_page+str(scratch_date)
        try:
            page = urllib.request.urlopen(quote_page)
        except:
            time.sleep(rd.randint(20,100))
            try:
                page = urllib.request.urlopen(quote_page)    
            except:
                    print("connection fail")
        soup = BeautifulSoup(page, "html.parser")
        table = Html_content_scratcher.get_table(soup)
        #處理資料
        table = Data_processor.process_dataframe(table,[str(scratch_date),stadium_and_station_tabel.loc[station,"球場"],station])
        #將表格上傳資料庫
        Database_uploader.upload_to_db(table,"testing")
        scratch_date += +datetime.timedelta(days=1)
    input("continue?")
    driver.quit()


    






#將root的html文件從網站抓取並存於soup變數，然後將soup傳給Html_content_scratcher


# driver.get("https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp")
# time.sleep(3)
# page = driver.page_source
# soup = BeautifulSoup(page, "html.parser")
# soup = str(soup)

# driver.find_element_by_xpath("//option[contains(text(),'雲林縣')]").click()

# driver.find_element_by_xpath("//option[contains(text(),'虎尾 (Huwei)')]").click()
# driver.find_elements_by_tag_name('input')[0].send_keys("2013-03-23")

# driver.find_element_by_id("doquery").click()
# driver.switch_to.window(driver.window_handles[1])
# # print(driver.current_url)

# # quote_page = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=C0K330&stname=%25E8%2599%258E%25E5%25B0%25BE&datepicker=2013-03-23"
# # page = urllib.request.urlopen(quote_page)
# page = driver.page_source
# soup = BeautifulSoup(page, "html.parser")
# print(soup)




# Database_uploader.upload_to_db(table,"testing")


 





