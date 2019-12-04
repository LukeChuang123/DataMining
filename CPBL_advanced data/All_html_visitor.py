import urllib
from bs4 import BeautifulSoup
import re

import random as rd
import time

import MySQL_table_connector
import Data_cleaner
import Database_uploader as db_uploader

def __init__(self,batting_link_list_assigned,pitching__link_list_assigned):

    self.batting_link_list = batting_link_list_assigned
    self.pitching_link_list = pitching__link_list_assigned

def visit_each_link(self,cur_assigned,conn_assigned):

    self.cur = cur_assigned
    self.conn = conn_assigned
    
    print("visit ok")

    for link_list in [batting_link_list,pitching_link_list]:
        #初始化新資料的id
        db_uploader.id = 0

        #輸入要存入的表格
        table_name = input("which table:").strip()

        #連線指定表格;如果還沒該表，則建立新表
        MySQL_table_connector.__init__(MySQL_table_connector,conn,cur,table_name)
        is_table_exists = MySQL_table_connector.table_exists(MySQL_table_connector)
        # print(is_table_exists)
        if(is_table_exists == 0):
            print(table_name + " "+"yet existed")
            MySQL_table_connector.create_table(MySQL_table_connector)

            for link_index in range(len(link_list)):
                #造訪網頁
                quote_page = link_list[link_index]
                page = urllib.request.urlopen(quote_page)
                soup = BeautifulSoup(page, "html.parser")

                #抓年份、選手名字和打擊數據(html)
                demand_data_title = soup.html.find("title")
                year = "\'"+re.findall("[1-2]{1}[0-9]{3}", demand_data_title.text.strip())[0]+"\',"
                print("year:"+year)
                if(link_list == batting_link_list):
                    demand_data_table = soup.html.find_all("table", attrs={"id": "table_id3"})[1]
                else:
                    demand_data_table = soup.html.find_all("table", attrs={"id": "table_id3"})[2]
                whole_data = demand_data_table.find_all("td", attrs={"valign": "middle"})

                #清洗數據:抓每個人有多少種數據(多少欄)，存成data_col_num，並同時將欄位名稱提取出來;刪除平均資料
                Data_cleaner.__init__(Data_cleaner,whole_data)
                data_col_num,col_name_list =  Data_cleaner.extract_col_name(Data_cleaner)
                whole_player_data = Data_cleaner.clean_data(Data_cleaner)

                #將資料存進db
                db_uploader.__init__(db_uploader,year,data_col_num,table_name,whole_player_data)
                db_uploader.upload_to_db(db_uploader,cur,conn)

                if(link_list == batting_link_list):
                    print("batting enter in!",link_index)
                else:
                    print("pitching enter in!",link_index)

                #暫停python
                time.sleep(rd.randint(50,100)/10)
        else:
            print("table is exist")
            print("pass to the next data scratch")
























        # for link_index in range(len(link_list)):
        #     #造訪網頁
        #     quote_page = link_list[link_index]
        #     page = urllib.request.urlopen(quote_page)
        #     soup = BeautifulSoup(page, "html.parser")

        #     #抓年份、選手名字和打擊數據(html)
        #     demand_data_title = soup.html.find("title")
        #     year = "\'"+re.findall("[1-2]{1}[0-9]{3}", demand_data_title.text.strip())[0]+"\',"
        #     print("year:"+year)
        #     if(link_list == batting_link_list):
        #         demand_data_table = soup.html.find_all("table", attrs={"id": "table_id3"})[1]
        #     else:
        #         demand_data_table = soup.html.find_all("table", attrs={"id": "table_id3"})[2]
        #     whole_data = demand_data_table.find_all("td", attrs={"valign": "middle"})

        #     #清洗數據:抓每個人有多少種數據(多少欄)，存成data_col_num，並同時將欄位名稱提取出來;刪除平均資料
        #     Data_cleaner.__init__(Data_cleaner,whole_data)
        #     data_col_num,col_name_list =  Data_cleaner.extract_col_name(Data_cleaner)
        #     whole_player_data = Data_cleaner.clean_data(Data_cleaner)

        #     # #將資料存進db
        #     db_uploader.__init__(db_uploader,year,data_col_num,table_name,whole_player_data)
        #     db_uploader.upload_to_db(db_uploader,cur,conn)

        #     if(link_list == batting_link_list):
        #         print("batting enter in!",link_index)
        #     else:
        #         print("pitching enter in!",link_index)

        #     #暫停python
        #     time.sleep(rd.randint(50,100)/10)

    # for link_index in range(len(pitching_link_list)):
    #     quote_page = pitching_link_list[link_index]
    #     page = urllib.request.urlopen(quote_page)
    #     soup = BeautifulSoup(page, "html.parser")
    #     print("pitching enter in!",link_index)