import MySQLdb
import re

import pandas as pd

import urllib
from bs4 import BeautifulSoup

import random as rd
import time

import Html_content_scratcher
import All_html_visitor
import String_language_judgement
import Data_processor
import Database_uploader
import MySQL_table_connector 

from selenium import webdriver

#輸入要連線的資料庫和表格
db_name = input("Which database:").strip()
# # table_name = input("Which table:").strip()

#連線至MySQL5指定資料庫
conn = MySQLdb.Connect(host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = 'Lc-20332895-',
                       db = db_name,
                       charset='utf8')
cur = conn.cursor()

#取得中職24~30年的網站連結
year_link_list = Html_content_scratcher.get_year_links()
# print(year_link_list)

#啟動瀏覽器驅動程式
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

# 暫停python
time.sleep(rd.randint(50,100)/10)

#建立表格
is_table_exists = MySQL_table_connector.table_exists(MySQL_table_connector,conn,cur,"each_game_data")
if(is_table_exists == 0): 
    MySQL_table_connector.create_table(cur,conn,"each_game_data")

# 抓取各球隊網站連結列表
for year_link in year_link_list:
    driver.get(year_link)
    pages_per_year = Html_content_scratcher.get_pages_nums(Html_content_scratcher,year_link)
    for page in pages_per_year:
        Html_content_scratcher.try_click(driver,"option",page)
        soup = Html_content_scratcher.get_html_bydriver(Html_content_scratcher,driver.page_source)
        print(driver.page_source)
        whole_day_data = soup.find_all("tr")[3:24]
        for day_data_index in range(0,len(whole_day_data),2):
            # print(whole_day_data[day_data_index])
            day_data = ["\'"+whole_day_data[day_data_index].find_all("td")[0].text+"\'"]
            print("day_data",day_data)
            date_and_day = whole_day_data[day_data_index].find_all("td")[1].text.split("(")
            print("data_and_day",date_and_day)
            date = date_and_day[0]
            day = date_and_day[1][0]
            day_dict = {"一":'Mon',"二":'Tue',"三":'Wed',"四":'Thu',"五":'Fri',"六":'Sat',"日":'Sun'}
            for data in [date,day_dict[day]]:
                day_data.append("\'"+data+"\'")
            for data_html in whole_day_data[day_data_index].find_all("td")[2:5]:
                day_data.append("\'"+data_html.text+"\'")
            for hr_or_err in whole_day_data[day_data_index+1].find_all("td"):
                day_data.append("\'"+hr_or_err.text+"\'")
            scores = whole_day_data[day_data_index].find_all("td")[5].text.split(":")
            time = whole_day_data[day_data_index].find_all("td")[6].text
            box_office = whole_day_data[day_data_index].find_all("td")[7].text
            for data in [scores[0],scores[1],time,box_office]:
                day_data.append("\'"+data+"\'")
            Database_uploader.upload_to_db_byrow(day_data,"each_game_data",cur,conn)

driver.quit()

if(len(Html_content_scratcher.error) > 0):
    for error in Html_content_scratcher.error:
        print(error)
else:
    print("every thing fine")







# soup = Html_content_scratcher.get_html(Html_content_scratcher,year_link_list[6])
# one_day_data = soup.find_all("tr")[23]
# print(one_day_data)




#error集
error = []

#遍歷各子網頁(抓歷年資料的連結、造訪、資料清洗、上傳db)

























 
