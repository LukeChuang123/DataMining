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

#將root的html文件從網站抓取並存於soup變數，然後將soup傳給Html_content_scratcher
quote_page = "http://www.cpbl.com.tw/cpbl.html"
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")
Html_content_scratcher.__init__(Html_content_scratcher,quote_page[:-9],soup)

#啟動瀏覽器驅動程式
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)

#暫停python
time.sleep(rd.randint(50,100)/10)

#抓取各球隊網站連結列表
team_link_list = Html_content_scratcher.get_team_links(Html_content_scratcher)
print(team_link_list)

#error集
error = []

#遍歷各子網頁(抓歷年資料的連結、造訪、資料清洗、上傳db)
for team_link in team_link_list[3:]:
    driver.get(team_link[0])
    Html_content_scratcher.try_click(driver,'a','球員成績')
    soup = Html_content_scratcher.get_html(Html_content_scratcher,driver.page_source)
    #抓各球隊有資料的年度(供守備成績資料使用)
    year_list = Html_content_scratcher.get_year_links(Html_content_scratcher,soup)
    grade_list = Html_content_scratcher.get_grade_links(Html_content_scratcher,soup)
    for year in year_list:
        Html_content_scratcher.try_click(driver,'option',year)
        for grade in grade_list:      
            # grade = "打擊成績"
            Html_content_scratcher.try_click(driver,'option',grade)
            time.sleep(rd.randint(0,10)/10)
            whole_player_table = Html_content_scratcher.try_get_table(driver,0)
            # input("continue")
            time.sleep(rd.randint(0,10)/10)
            team_name = list(whole_player_table["TEAM"])[0]
            #將背號去掉得到name_list
            name_list = [list(whole_player_table["NAME"]),String_language_judgement.keep_only_chinese(list(whole_player_table["NAME"]))]
            print(whole_player_table)
            if(grade == "守備成績"):
                Data_processor.process_defense_dataframe(whole_player_table,year,name_list[1])
                print(whole_player_table)
                Database_uploader.upload_to_db(whole_player_table,grade)
            else:
                for name_index in range(len(name_list[0])):
                    Html_content_scratcher.try_click(driver,'a',name_list[0][name_index])
                    time.sleep(rd.randint(30,60)/10)
                    player_table = Html_content_scratcher.try_get_table(driver,1)
                    print(player_table)
                    # if(grade == "投球成績"):
                     #     player_table = pd.read_html(driver.page_source)[1]
                    # elif(grade == "打擊成績"):
                    #     player_table = pd.read_html(driver.page_source)[2]
                    time.sleep(rd.randint(0,10)/10)
                    print(team_name)
                    player_year_list = list(player_table[player_table["TEAM"]==team_name]["YEAR"])
                    print(player_year_list)
                    Html_content_scratcher.try_click(driver,'a','逐場成績表')
                    for player_year in player_year_list:
                        # 工程師耍智障沒更新網頁的時候則略過
                        try:
                            Html_content_scratcher.try_click(driver,'option',player_year)
                        except:
                            error.append("engineer forget update"+" "+name_list[1][name_index])
                            print("fail")
                            # continue
                        else:
                            print("click each player_year success")
                            player_byGame_table = Html_content_scratcher.try_get_table(driver,1)
                            time.sleep(rd.randint(0,10)/10)
                            #右移表格
                            Html_content_scratcher.try_click_img(driver,"http://cpbl-elta.cdn.hinet.net/web/images/icon_arrow5_right.png")
                            time.sleep(rd.randint(0,10)/10)
                            player_byGame_table_right = Html_content_scratcher.try_get_table(driver,1)
                            time.sleep(rd.randint(0,10)/10)
                            # 處理資料
                            try:
                                player_byGame_table = Data_processor.process_dataframe(player_byGame_table,player_byGame_table_right,player_year,name_list[1][name_index],team_link[1])
                            except:
                                error.append("data process fail"+" "+name_list[1][name_index])                                
                                print("data process fail")
                                continue
                            else:
                                #上傳資料(上傳前檢查是否已存在該表格)
                                print("data process success")
                                try:
                                    print(player_byGame_table)
                                    Database_uploader.upload_to_db(player_byGame_table,grade) 
                                    MySQL_table_connector.turn_on_table(MySQL_table_connector,grade)   
                                except:
                                    error.append("data upload fail"+" "+name_list[1][name_index])
                                    print("data upload fail")
                                    continue
                                else:
                                    #追蹤目前爬到哪裡
                                    print(player_byGame_table)
                                    print("hi4")
                    time.sleep(rd.randint(0,10)/10)
                    driver.get(team_link[0])
                    Html_content_scratcher.try_click(driver,'a','球員成績')
                    Html_content_scratcher.try_click(driver,'option',year)
                    Html_content_scratcher.try_click(driver,'option',grade)
    time.sleep(rd.randint(0,10)/10)
    input("go next team?")

driver.quit()

for item in error:
    print("error:",item)
























# #連線指定表格;如果還沒該表，則建立新表
# MySQL_table_connector.__init__(MySQL_table_connector,conn,cur,db_name,table_name)
# is_table_exists = MySQL_table_connector.table_exists(MySQL_table_connector)
# print(is_table_exists)
# if(is_table_exists == 0):
#     MySQL_table_connector.create_table(MySQL_table_connector)
#     print(table_name + " "+"created")
# else:
#     print("table is exist")




# #抓年份、選手名字和打擊數據(html)
# demand_data_title = soup.html.find("title")
# year = "\'"+re.findall("[1-2]{1}[0-9]{3}", demand_data_title.text.strip())[0]+"\',"
# demand_data_table = soup.html.find_all("table", attrs={"id": "table_id3"})[1]
# whole_data = demand_data_table.find_all("td", attrs={"valign": "middle"})

# #抓每個人有多少種數據(多少欄)，存成data_col_num，並同時將欄位名稱提取出來
# Data_cleaner.__init__(Data_cleaner,whole_data)
# data_col_num,col_name_list =  Data_cleaner.extract_col_name(Data_cleaner)
# whole_player_data = Data_cleaner.clean_data(Data_cleaner)

# # #將資料存進db
# db_uploader.__init__(db_uploader,year,data_col_num,table_name,whole_player_data)
# db_uploader.upload_to_db(db_uploader,cur,conn)




# #抓每個人有多少種數據(多少欄)，存成data_col_num，並同時將欄位名稱提取出來
# Data_cleaner.__init__(Data_cleaner,whole_data)
# data_col_num,col_name_list =  Data_cleaner.extract_col_name(Data_cleaner)
# whole_player_data = Data_cleaner.clean_data(Data_cleaner)
# data_col_num = 0
# col_name_list = []
# for data in whole_data:
#     if(String_language_judgement.check_contain_chinese(data.text.strip()) == False):
#        data_col_num += 1
#        col_name_list.append(data.text.strip())
#     else:
#         break
# # print("hello",data_col_num)

# #去除網頁上的表格欄位名稱後，剩下的資料(選手資料)存進whole_player_data
# whole_player_data = [data for data in whole_data[data_col_num:]]

# # 列印inserted_player_data、將資料從html變成str然後存成新的whole_player_data
# col_number = 1
# for data_index in range(len(whole_player_data)):
#     if(col_number <= 21):
#         player_data = whole_player_data[data_index].text.strip()
#         #因為平均那列的欄數只有21欄，不放入whole_player_data，所以跳出迴圈
#         if(player_data == "League AVG 聯盟平均"):
#             for average_data in whole_player_data[data_index:]:
#                 whole_player_data.remove(average_data)
#             break
#         else:
#             whole_player_data[data_index] = "\'"+player_data+"\'"
#             print(player_data,end = " ")
#             col_number += 1
#     else:
#         player_data = whole_player_data[data_index].text.strip()
#         whole_player_data[data_index] = "\'"+player_data+"\'"
#         # print(player_data,"\n")
#         col_number = 1

# #將資料存進db
# db_uploader.__init__(db_uploader,year,data_col_num,table_name,whole_player_data)
# db_uploader.upload_to_db(db_uploader,cur,conn)
# for player_data_index in range(0,len(whole_player_data),data_col_num):
#     player_data = whole_player_data[player_data_index:player_data_index+data_col_num]
#     id = "\'"+str(int(player_data_index/data_col_num+1))+"\',"
#     inserted_player_data = ",".join(player_data)
#     print(inserted_player_data)
#     sql = "INSERT INTO"+" "+table_name+"(id,YEAR,NAME,G,PA,AVG,OBP,SLG,OPS,OPS_plus,BABIP,SecA,BIP_per,RC,wRC,wRC_plus,wOBA,wRAA,EqA,EqR,BB_per,K_per,ABHR,GOFO)VALUES ("+id+year+inserted_player_data+");"
#     # print(sql)
#     try:
#         # 执行sql语句
#         cur.execute(sql)
#         # 提交到数据库执行
#         conn.commit()
#         print("commit ok!")
#     except:
#         # Rollback in case there is any error
#         conn.rollback()
#         print("rollback...")
        

#將資料存進db
# sql = "INSERT INTO"+" "+table_name+"(NAME,PA,\
#     AVG,OBP,SLG,OPS,OPS_plus,BABIP,BIP_per,RC,wRC,\
#     wRC_plus,wOBA,wRAA,EqA,EqR,BB_per,K_per,ABHR,GOFO\
#     VALUES ("+inserted_player_data+")"
# try:
#    # 执行sql语句
#    cur.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # Rollback in case there is any error
#    db.rollback()

