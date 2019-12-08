# import MySQLdb
# import re

# import pandas as pd

# import urllib
# from bs4 import BeautifulSoup

# import random as rd
# import time
# import geocoder
# from math import radians, cos, sin, asin, sqrt  

# import Html_content_scratcher

# from selenium import webdriver

# def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）  
#     '''
#     Calculate the great circle distance between two points  
#     on the earth (specified in decimal degrees) 
#     ''' 
#     # 将十进制度数转化为弧度  
#     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
  
#     # haversine公式  
#     dlon = lon2 - lon1   
#     dlat = lat2 - lat1   
#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
#     c = 2 * asin(sqrt(a))   
#     r = 6371 # 地球平均半径，单位为公里  
#     return c * r * 1000 
# #輸入要連線的資料庫和表格
# # db_name = input("Which database:").strip()
# # table_name = input("Which table:").strip()

# #連線至MySQL5指定資料庫
# conn = MySQLdb.Connect(host = '127.0.0.1',
#                        port = 3306,
#                        user = 'root',
#                        passwd = 'Lc-20332895-',
#                        db = "cpbl_whole_data",
#                        charset='utf8')
# cur = conn.cursor()

# #將root的html文件從網站抓取並存於soup變數，然後將soup傳給Html_content_scratcher
# quote_page = "http://www.cpbl.com.tw/footer/stadium/"
# page = urllib.request.urlopen(quote_page)
# soup = BeautifulSoup(page, "html.parser")

# latitude_and_longitude = ["經度","緯度"]
# stadiums = ["天母","新莊","桃園","新竹","台灣國立體育","洲際","雲林","嘉義市","台南","澄清湖","屏東","羅東","花蓮"]
# stadium_location  = pd.DataFrame(index = stadiums, columns = latitude_and_longitude)
# print(stadium_location)

# stadium_link_list = []
# for stadium in stadiums:
#     stadium_link_list.append("http://www.cpbl.com.tw"+soup.find("a", text = re.compile(stadium+"[\u4e00-\u9fa5]*棒球場")).get("href"))
# print(stadium_link_list)

# #取得棒球場地址
# address_list = []
# for stadium_link in stadium_link_list:
#     quote_page = stadium_link
#     page = urllib.request.urlopen(quote_page)
#     soup = BeautifulSoup(page, "html.parser")
#     address_list.append(soup.find("table").find_all("tr")[2].find_all("td")[1].text)
#     time.sleep(rd.randint(50,100)/10)
# print(address_list)

# #取得各天氣觀測站資訊
# quote_page = "https://e-service.cwb.gov.tw/wdps/obs/state.htm"
# page = urllib.request.urlopen(quote_page)
# soup = BeautifulSoup(page, "html.parser")
# all_observe_station_data_list = []
# col_name_list = []
# for observe_station_row in soup.find_all("tr"):
#     observe_station_data_list = []
#     for cell in observe_station_row.find_all("td"):
#         try:
#             observe_station_data = cell.find("p").text
#         except:
#             try:
#                observe_station_data = cell.find("span").text 
#             except:
#                 print("can not find text")
#             else:
#                 observe_station_data_list.append(observe_station_data)
#         else:
#             observe_station_data_list.append(observe_station_data)
#     if(len(observe_station_data_list) > 3):
#         if( observe_station_data_list[0] != "站號"):
#             all_observe_station_data_list.append(observe_station_data_list)
#         else:
#             col_name_list = observe_station_data_list

# #將觀測站資訊存成dataframe之後有需要可存成csv
# all_observe_station_data_table = pd.DataFrame(all_observe_station_data_list, columns = col_name_list)
# all_observe_station_data_table.set_index("站名", inplace = True)
# print(all_observe_station_data_table.index.names)

# #找離各球場最近的觀測站
# each_min_distances = []
# for address in address_list:
#     g = geocoder.arcgis(address)
#     stadium_latlng = g.latlng
#     min_distance_between_stadium_and_station = ["",39400,""] 
#     for station in all_observe_station_data_list:
#         print(station[1])
#         station_lng = float(station[3])
#         station_lat = float(station[4])
#         try:
#             distance = haversine(stadium_latlng[1],stadium_latlng[0],station_lng,station_lat)
#             if(distance < min_distance_between_stadium_and_station[1]):
#                 min_distance_between_stadium_and_station[1] = distance
#                 min_distance_between_stadium_and_station[0] = stadiums[address_list.index(address)]
#                 min_distance_between_stadium_and_station[2] = station[1]
#         except:
#             # print(station[1]+" "+station_latlng[1]+" "+station_latlng[0])
#             print("find lat lng fail")
#     print(min_distance_between_stadium_and_station)
#     each_min_distances.append(min_distance_between_stadium_and_station)  



# distance_between_stadium_and_station_table = pd.DataFrame(each_min_distances,columns = ["球場","最短距離","觀測站"])
# print(distance_between_stadium_and_station_table)

# Dat
list = [1,2,3,4,5,6]
print(list.remove(8))

