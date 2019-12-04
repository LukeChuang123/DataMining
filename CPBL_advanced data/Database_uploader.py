#將資料存進db

def __init__(self,year_assigned,data_col_num_assigned,table_name_assigned,whole_player_data_assigned):

    self.year = year_assigned
    self.data_col_num = data_col_num_assigned
    self.table_name = table_name_assigned
    self.whole_player_data = whole_player_data_assigned

def upload_to_db(self,cur_assigned,conn_assigned):
    
    global id
    self.cur = cur_assigned
    self.conn = conn_assigned
    
    for player_data_index in range(0,len(whole_player_data),data_col_num):

        print("data_col_num",data_col_num)
        player_data = whole_player_data[player_data_index:player_data_index+data_col_num]

        #如果選手數據量(欄數)!=data_col_num，則不上傳資料庫
        if(len(player_data) != data_col_num):
            print("incompatible data_col_num",player_data[0],year)
            continue

        #資料id
        id += 1
        id_str = "\'"+str(id)+"\'," 
        # id = "\'"+str(int(player_data_index/data_col_num+1))+"\',"

        inserted_player_data = ",".join(player_data)
        print(inserted_player_data)
        if(table_name == "cpbl_batting_data"):
            sql = "INSERT INTO"+" "+table_name+"(id,YEAR,NAME,G,PA,AVG,OBP,SLG,OPS,OPS_plus,BABIP,SecA,BIP_per,RC,wRC,wRC_plus,wOBA,wRAA,EqA,EqR,BB_per,K_per,ABHR,GOFO)VALUES ("+id_str+year+inserted_player_data+");"
        else:
             sql = "INSERT INTO"+" "+table_name+"(id,YEAR,NAME,G,GS,GR,IP,ERA,WHIP,FIP,ERA_plus,BB_per,K_per,BABIP,LOB_per,DER,DIP,DIPS_ERA,DIPS_WHIP,WAR)VALUES ("+id_str+year+inserted_player_data+");"
        # print(sql)
        # try:
            # 执行sql语句
        cur.execute(sql)
            # 提交到数据库执行
        conn.commit()
        print("commit ok!")
        # except:
        #     # Rollback in case there is any error
        #     conn.rollback()
        #     print("rollback...")
    