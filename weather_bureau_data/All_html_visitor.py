import urllib
from bs4 import BeautifulSoup
import re

import random as rd
import time

import MySQL_table_connector
import Data_processor
# import Database_uploader as db_uploader

import pymysql
import pandas as pd
from sqlalchemy import create_engine

def __init__(self,hyper_link_list_assigned):

    self.link_list = hyper_link_list_assigned

def visit_each_link(self,cur_assigned,conn_assigned,db_name_assigned):

    self.cur = cur_assigned
    self.conn = conn_assigned
    self.db_name = db_name_assigned
    
    print("visit ok")

    #輸入要存入的表格
    table_name = input("which table:").strip()

    #連線指定表格;如果還沒該表，則建立新表
    # MySQL_table_connector.__init__(MySQL_table_connector,conn,cur,table_name)
    # is_table_exists = MySQL_table_connector.table_exists(MySQL_table_connector)
    is_table_exists = 0
    # print(is_table_exists)
    if(is_table_exists == 0):
        print(table_name + " "+"yet existed")
        # MySQL_table_connector.create_table(MySQL_table_connector)

        for link_index in range(len(link_list)-1,-1,-1):
            #造訪網頁
            quote_page = link_list[link_index]
            page = urllib.request.urlopen(quote_page)
            soup = BeautifulSoup(page, "html.parser")

            #抓歷年全壘打資料表格存成dataframe
            table = pd.read_html(quote_page)[0]

            #將#字欄刪掉
            table = table.drop("#",axis = 1)

            #將資料存進db
            print(table)
            # db_name = DataMining.db_name
            mysqlInfo = {
                "host": '127.0.0.1',
                "user": 'root',
                "password": 'Lc-20332895-',
                "database": db_name,
                "port": 3306,
                "charset": 'utf8'
            }
            engine = create_engine('mysql+pymysql://root:Lc-20332895-@localhost:3306/'+db_name)
            table.to_sql(table_name, engine, if_exists='append', index=False)
            # table.to_sql(name=table_name, con=conn, if_exists='append', index=True)

            #暫停python
            time.sleep(rd.randint(50,100)/10)
            
            print("annual hr data uploaded successfully",(str)(2019-link_index))
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