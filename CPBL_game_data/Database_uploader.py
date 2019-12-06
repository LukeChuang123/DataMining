#將資料存進db
from sqlalchemy import *

import MySQL_table_connector as table_connector

mysqlInfo = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": 'Lc-20332895-',
    "database": "cpbl_whole_data",
    "port": 3306,
    "charset": 'utf8'
}

# table.set_index(["YEAR","POS"])
engine = create_engine('mysql+pymysql://root:Lc-20332895-@localhost:3306/'+"cpbl_whole_data")
conn = engine.connect()

def __init__(self,year_assigned,data_col_num_assigned,table_name_assigned,whole_player_data_assigned):

    self.year = year_assigned
    self.data_col_num = data_col_num_assigned
    self.table_name = table_name_assigned
    self.whole_player_data = whole_player_data_assigned

def upload_to_db(table,dbtable_name):

    dtypedict = {}
    for col in table.columns:
        dtypedict[col] = NVARCHAR(length=255)

    #判斷表是否已被建立，若無則turn on，第一次上傳，設定聯合唯一約束
    # if(table_connector.is_batting_table_exist == False or table_connector.is_pitching_table_exist == False or table_connector.is_defense_table_exist == False):
    
    # table_connector.turn_on_table(table_connector, dbtable_name)
    table.to_sql(dbtable_name, engine, if_exists='append', index=False, dtype=dtypedict)
    # conn.execute("alter table "+dbtable_name+" "+"add constraint date_game_name unique(DATE,GAME_NO,NAME);")
    

    table.to_sql("temp_table", engine, if_exists='replace', index=False, dtype=dtypedict)

    # table.to_sql(dbtable_name, engine, if_exists='append', index=False, dtype=dtypedict)

    #若資料已存在則略過，否則插入
    with engine.begin() as cnx:
        insert_sql = "INSERT IGNORE INTO "+dbtable_name+" "+"(SELECT * FROM temp_table)"
        cnx.execute(insert_sql)

def upload_to_db_byrow(data,dbtable_name,cur,conn):
    inserted_day_data = ",".join(data)
    print(inserted_day_data)
    sql = "INSERT INTO"+" "+dbtable_name+"(GAME_NO,DATE,DAY,STADIUM,CLIENT,HOST,CLIENT_HR,CLIENT_ERR,HOST_HR,HOST_ERR,CLIENT_SCORE,HOST_SCORE,TIME,BOX_OFF)VALUES ("+inserted_day_data+");"
    # 执行sql语句
    cur.execute(sql)
    # 提交到数据库执行
    conn.commit()
    # print("commit ok!")