import MySQLdb
import re

import pandas as pd

import urllib
from bs4 import BeautifulSoup

import random as rd
import time

import Html_content_scratcher

from selenium import webdriver
# import All_html_visitor


#輸入要連線的資料庫和表格
# db_name = input("Which database:").strip()
# table_name = input("Which table:").strip()

#連線至MySQL5指定資料庫
conn = MySQLdb.Connect(host = '127.0.0.1',
                       port = 3306,
                       user = 'root',
                       passwd = 'Lc-20332895-',
                       db = "cpbl_whole_data",
                       charset='utf8')
cur = conn.cursor()

#將root的html文件從網站抓取並存於soup變數，然後將soup傳給Html_content_scratcher
# quote_page = "http://www.cpbl.com.tw/web/team_playergrade.php?&gameno=01&team=E02&year=2019&grade=3&syear=2019"
# page = urllib.request.urlopen(quote_page)
# soup = BeautifulSoup(page, "html.parser")
# all_teams = (soup.find("ul",attrs = {"id":"menu-submenu2"}).contents)[3:13:2]
# team_link_list = []
# team_list = []
# for team in all_teams:
#     team_link = quote_page[:-9]+team.a.get("href")
#     team_link_list.append(team_link)
#     team_list.append(team.a.text) 
#     print(team_list)
# position_html = soup.find("select",id="sgrade").contents
# position_list = [position.text for position in position_html[1:len(position_html):2]]
# print(len(position_html))
# print(position_list)
# year_html = soup.find("select",id="syear").contents
# year_list = [year.text for year in year_html[-2:-len(year_html):-2]]
# print(year_list)
# driver = webdriver.Chrome('./chromedriver')
# driver.get(quote_page)
# driver.find_element_by_xpath("//option[contains(text(),'投球成績')]").click()
# time.sleep(3)
# table_name = "打擊成績"
# sql = "show tables;"
# cur.execute(sql)
# tables = [cur.fetchall()]
# print(str(tables))
# table_list = re.findall('(\'.*?\')',str(tables))
# table_list = [re.sub("'",'',each) for each in table_list]
# print("table_name:"+table_name)
# if table_name in table_list:
#         print(1)
# else:
#         print(0)
l = None
print(type(l))
for i in l:
        print(i)
# for i in l[-3:]:
#         print(i)
# driver.quit()
# driver.find_element_by_xpath("//option[contains(text(),'投球成績')]").click()
# time.sleep(4)
# print("pitching web ok")
# driver.find_element_by_xpath("//option[contains(text(),'守備成績')]").click()
# time.sleep(5)
# driver.quit()

# print(all_teams)
# Html_content_scratcher.__init__(Html_content_scratcher,quote_page,soup)

#暫停python
time.sleep(rd.randint(50,100)/10)

#遍歷各子網頁(抓歷年資料的連結、造訪、資料清洗、上傳db)
# Html_content_scratcher.getHyperLink(Html_content_scratcher)
# All_html_visitor.visit_each_link(All_html_visitor,cur,conn)





















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

