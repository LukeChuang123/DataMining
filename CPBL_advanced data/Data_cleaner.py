import String_language_judgement
import re

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
def clean_data(self):

    #去除網頁上的表格欄位名稱後，剩下的資料(選手資料)存進whole_player_data
    whole_player_data = [data for data in whole_data[data_col_num:]]

    col_number = 1
    for data_index in range(len(whole_player_data)):
        if(col_number <= 21):
            player_data = whole_player_data[data_index].text.strip().replace(" ","")
            #因為平均那列的欄數只有21欄，不放入whole_player_data，所以跳出迴圈
            if(player_data == "LeagueAVG聯盟平均"):
                for average_data in whole_player_data[data_index:]:
                    whole_player_data.remove(average_data)
                break
            else:
                whole_player_data[data_index] = "\'"+player_data+"\'"
                # print(player_data,end = " ")
                col_number += 1
        else:
            player_data = whole_player_data[data_index].text.strip()
            whole_player_data[data_index] = "\'"+player_data+"\'"
            # print(player_data,"\n")
            col_number = 1
    
    return whole_player_data