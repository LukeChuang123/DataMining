import String_language_judgement
import re

import pandas as pd
data_col_num = 0

def __init__(self,whole_data_assigned):
    self.whole_data = whole_data_assigned
def extract_col_name(self):
    #每跑完一年份(一個網頁)的資料要歸零
    global data_col_num 
    data_col_num = 0
    # global data_col_num
    col_name_list = []
    for data in whole_data:
        if(
            String_language_judgement.is_contain_chinese(data.text.strip()) == False): 
            # print(String_language_judgement.check_contain_chinese(data.text.strip()))
            data_col_num += 1
            col_name_list.append(data.text.strip())
        else:
            break

    #將欄位名稱印出以供使用者確認    
    print(col_name_list)
    # for col in col_name_list:
    #     print(col,end = " ")
    #     # 換行
    #     print()

    return data_col_num,col_name_list
def process_dataframe(player_byGame_table,player_byGame_table_right,year,name,team_name):
    #先處理player_byGame_table
    date_game_list = list(player_byGame_table["DATE(GAME)"])
    date_and_game = pd.DataFrame([[year+"/"+date_game[0:5], date_game[6:len(date_game)-1]] for date_game in date_game_list],columns = ["DATE","GAME NO."])
    player_byGame_table.drop("DATE(GAME)",axis=1,inplace=True) 
    player_byGame_table.insert(0,column="DATE",value=date_and_game["DATE"]) 
    player_byGame_table.insert(1,column="GAME_NO",value=date_and_game["GAME NO."]) 
    player_byGame_table.insert(2,column="NAME",value=name) 
    player_byGame_table.insert(3,column="TEAM",value=team_name)

    #後處理player_byGame_table_right
    player_byGame_table_right.drop("DATE(GAME)",axis=1,inplace=True)
    player_byGame_table_right.drop("OPP",axis=1,inplace=True)

    #將兩個dataframe合併
    final_df = player_byGame_table.join(player_byGame_table_right,lsuffix='_1',rsuffix='_2')

    return final_df
def process_defense_dataframe(whole_player_table,year,name_list):
    whole_player_table.drop("NAME",axis=1,inplace=True) 
    whole_player_table.insert(0,column="NAME",value=pd.Series(name_list)) 
    whole_player_table.insert(1,column="YEAR",value=year) 
# def process_right_dataframe(player_byGame_table_right,)
