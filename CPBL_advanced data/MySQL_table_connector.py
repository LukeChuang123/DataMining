import MySQLdb
import re

#初始化要確認是否存在，若不存在則創立的表格
def __init__(self,conn_assigned,cur_assigned,table_name_assigned):
    self.conn = conn_assigned
    self.cur = cur_assigned
    self.table_name = table_name_assigned
#判斷表是否存在
def table_exists(self):
    sql = "show tables;"
    cur.execute(sql)
    tables = [cur.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    print("table_name:"+table_name)
    if table_name in table_list:
        return 1
    else:
        return 0
def create_table(self):
    if(table_name == "cpbl_batting_data"):
        sql = "create table"+" "+table_name+" "+"(id INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(255),YEAR VARCHAR(255),G VARCHAR(255),PA VARCHAR(255),AVG VARCHAR(225),OBP VARCHAR(225),SLG VARCHAR(225),OPS VARCHAR(225),OPS_plus VARCHAR(225),BABIP VARCHAR(225),SecA VARCHAR(225),BIP_per VARCHAR(225),RC VARCHAR(225),wRC VARCHAR(225),wRC_plus VARCHAR(225),wOBA VARCHAR(225),wRAA VARCHAR(225),EqA VARCHAR(225),EqR VARCHAR(225),BB_per VARCHAR(225),K_per VARCHAR(225),ABHR VARCHAR(225),GOFO VARCHAR(225))"
        cur.execute(sql)
        conn.commit()
        print(table_name + " "+"created successfully!")
    elif(table_name == "cpbl_pitching_data"):
        sql = "create table"+" "+table_name+" "+"(id INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(255),YEAR VARCHAR(255),G VARCHAR(255),GS VARCHAR(255),GR VARCHAR(225),IP VARCHAR(225),ERA VARCHAR(225),WHIP VARCHAR(225),FIP VARCHAR(225),ERA_plus VARCHAR(225),BB_per VARCHAR(225),K_per VARCHAR(225),BABIP VARCHAR(225),LOB_per VARCHAR(225),DER VARCHAR(225),DIP VARCHAR(225),DIPS_ERA VARCHAR(225),DIPS_WHIP VARCHAR(225),WAR VARCHAR(225))"
        cur.execute(sql)
        conn.commit()
        print(table_name + " "+"created successfully!")

# 欄位要不要有id?
# id INT AUTO_INCREMENT PRIMARY KEY,