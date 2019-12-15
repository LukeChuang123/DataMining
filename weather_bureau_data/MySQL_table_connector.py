import MySQLdb
import re

is_table_exist = True


#初始化要確認是否存在，若不存在則創立的表格
# def __init__(self):
    # self.conn = conn_assigned
    # self.cur = cur_assigned
    # self.table_name = table_name_assigned
#判斷表是否存在
def table_exists(self,conn,cur,table_name):
    sql = "show tables;"
    cur.execute(sql)
    tables = [cur.fetchall()]
    print(str(tables))
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    print("table_list:",table_list)
    print("table_name:"+table_name)
    if table_name in table_list:
        print("inside exist")
        return 1
    else:
        print("inside not exist")
        return 0
def turn_on_table(self,table_name):
    self.is_table_exist = True
    if(table_name == "打擊成績"):
        self.is_batting_table_exist = True
    elif(table_name == "投球成績"):
        self.is_pitching_table_exist = True
    else:
        is_defense_table_exist = True
def create_table(cur,conn,table_name):
    sql = "create table"+" "+table_name+" "+"(GAME_NO VARCHAR(255),DATE VARCHAR(255),DAY VARCHAR(255),STADIUM VARCHAR(255),CLIENT VARCHAR(255),HOST VARCHAR(255),CLIENT_HR VARCHAR(255),CLIENT_ERR VARCHAR(225),HOST_HR VARCHAR(225),HOST_ERR VARCHAR(225),CLIENT_SCORE VARCHAR(225),HOST_SCORE VARCHAR(225),TIME VARCHAR(225),BOX_OFF VARCHAR(225))"
    cur.execute(sql)
    conn.commit()
    print(table_name + " "+"created successfully!")

    if(table_name == "cpbl_annual_homerun"):
        sql = "create table"+" "+table_name+" "+"(id INT AUTO_INCREMENT PRIMARY KEY,YEAR VARCHAR(255),GAME_NO VARCHAR(255),GAME VARCHAR(255),STADIUM VARCHAR(225),PLAYER VARCHAR(225),PLAYER_TEAM VARCHAR(225),PITCHER VARCHAR(225),PITCHER_TEAM VARCHAR(225),RBI VARCHAR(225),REMARK VARCHAR(225))"
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