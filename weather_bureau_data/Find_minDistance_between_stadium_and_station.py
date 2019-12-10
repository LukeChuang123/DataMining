import pandas as pd
import re

import urllib
from bs4 import BeautifulSoup

import random as rd
import time
import datetime
import geocoder
from math import radians, cos, sin, asin, sqrt  

#判斷當前找到的觀測站其使用時間之加總是否包含整個研究期間
def if_found_station_enough(stadium,each_min_distances):
    is_found_station_enough = False
    start_date = datetime.datetime.strptime("2013-03-23", "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime("2019-10-17", "%Y-%m-%d").date()
    found_stations_for_stadium = [min_distance for min_distance in each_min_distances if min_distance[0] == stadium]
    for found_station in found_stations_for_stadium:
        if(datetime.datetime.strptime(found_station[3], "%Y-%m-%d").date() <= start_date):
            for found_station in found_stations_for_stadium:
                if(found_station[4] == None):
                    is_found_station_enough = True
                    break
                else:
                    if(end_date <= datetime.datetime.strptime(found_station[4], "%Y-%m-%d").date()):
                        is_found_station_enough = True
                        break
                    else:
                        continue
        else:
            continue
    return is_found_station_enough

def get_list_at(index,all_observe_station_data_list):
    for list in all_observe_station_data_list:
        if(list[-1] == index):
            return list
def haversine(lon1, lat1, lon2, lat2): # 经度1，纬度1，经度2，纬度2 （十进制度数）  
    '''
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    ''' 
    # 将十进制度数转化为弧度  
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
  
    # haversine公式  
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 # 地球平均半径，单位为公里  
    return c * r * 1000 

def find_min_distance(all_observe_station_data_list,min_distance_between_stadium_and_station,stadiums,address_index,each_min_distances,start_and_end_date):
    start_date = datetime.datetime.strptime(start_and_end_date[0], "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(start_and_end_date[1], "%Y-%m-%d").date()
    for station in all_observe_station_data_list:
        print(station[1])
        station_lng = float(station[3])
        station_lat = float(station[4])
        try:
            distance = haversine(stadium_latlng[1],stadium_latlng[0],station_lng,station_lat)
            if(distance < min_distance_between_stadium_and_station[1]):
                min_distance_between_stadium_and_station[1] = distance
                min_distance_between_stadium_and_station[0] = stadiums[address_index]
                min_distance_between_stadium_and_station[2] = station[1]
                min_distance_between_stadium_and_station[3] = station[7].replace("/","-")
                min_distance_between_stadium_and_station.append(station[-1])
                if(station[8] == '\u3000'):
                    min_distance_between_stadium_and_station[4] = None
                else:
                    min_distance_between_stadium_and_station[4] = station[8].replace("/","-")
        except:
            # print(station[1]+" "+station_latlng[1]+" "+station_latlng[0])
            print("find lat lng fail")
        else:
            pass
    print(min_distance_between_stadium_and_station)
    removed_station_if_need = get_list_at(min_distance_between_stadium_and_station[-1],all_observe_station_data_list)
    print("remove")
    print(removed_station_if_need)
    #找到最小距離的觀測站後要判斷該觀測站的使用期間是否涵蓋我的研究範圍(2013-03-23~2019-10-17)
    station_start_date = datetime.datetime.strptime(min_distance_between_stadium_and_station[3], "%Y-%m-%d").date()
    if(min_distance_between_stadium_and_station[4] == None):
        print("hello")
        if(station_start_date <= start_date):
            each_min_distances.append(min_distance_between_stadium_and_station[0:5])
        else:
            print("hello")
            # input("continue1?")
            each_min_distances.append(min_distance_between_stadium_and_station[0:5])
            all_observe_station_data_list.remove(removed_station_if_need)
            if(if_found_station_enough(stadiums[address_index],each_min_distances) == False):
                find_min_distance(all_observe_station_data_list,["",39400,"","",""],stadiums,address_index,each_min_distances,["2013-03-23",min_distance_between_stadium_and_station[3]])
    else:
        station_end_date = datetime.datetime.strptime(min_distance_between_stadium_and_station[4], "%Y-%m-%d").date()
        if(station_start_date <= start_date and end_date <= station_end_date):
            each_min_distances.append(min_distance_between_stadium_and_station[0:5])
        elif(station_start_date <= start_date and start_date <= station_end_date and station_end_date < end_date):
            # input("continue2?")
            each_min_distances.append(min_distance_between_stadium_and_station[0:5])
            all_observe_station_data_list.remove(removed_station_if_need)
            if(if_found_station_enough(stadiums[address_index],each_min_distances) == False):
                find_min_distance(all_observe_station_data_list,["",39400,"","",""],stadiums,address_index,each_min_distances,[min_distance_between_stadium_and_station[4],"2019-10-17"])
        elif(start_date < station_start_date and end_date <= station_end_date):
            # input("continue3?")
            each_min_distances.append(min_distance_between_stadium_and_station[0:5])
            all_observe_station_data_list.remove(removed_station_if_need)
            if(if_found_station_enough(stadiums[address_index],each_min_distances) == False):
                find_min_distance(all_observe_station_data_list,["",39400,"","",""],stadiums,address_index,each_min_distances,["2013-03-23",min_distance_between_stadium_and_station[3]])
        else:
            # input("continue4?")
            all_observe_station_data_list.remove(removed_station_if_need)
            if(if_found_station_enough(stadiums[address_index],each_min_distances) == False):
                find_min_distance(all_observe_station_data_list,["",39400,"","",""],stadiums,address_index,each_min_distances,["2013-03-23","2019-10-17"])

#將root的html文件從網站抓取並存於soup變數，然後將soup傳給Html_content_scratcher
quote_page = "http://www.cpbl.com.tw/footer/stadium/"
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

latitude_and_longitude = ["經度","緯度"]
stadiums = ["天母","新莊","桃園","新竹","台灣國立體育","洲際","雲林","嘉義市","台南","澄清湖","屏東","羅東","花蓮"]

stadium_link_list = []
for stadium in stadiums:
    stadium_link_list.append("http://www.cpbl.com.tw"+soup.find("a", text = re.compile(stadium+"[\u4e00-\u9fa5]*棒球場")).get("href"))
print(stadium_link_list)

#試著向遠端伺服器取得棒球場地址
try:
    for stadium_link in stadium_link_list:
        quote_page = stadium_link
        page = urllib.request.urlopen(quote_page)
        soup = BeautifulSoup(page, "html.parser")
        address_list.append(soup.find("table").find_all("tr")[2].find_all("td")[1].text)
        time.sleep(rd.randint(50,130)/10)
except:
    address_list = ["台北市士林區忠誠路二段77號","新北市新莊區和興街66號","桃園市中壢區領航北路一段1號","新竹市西大路559號","台中市雙十路一段16號","台中市北屯區崇德路三段835號","	雲林縣斗六市明德北路二段320號","嘉義市東區山仔頂249-1號","台南市健康路一段257號","高雄市鳥松區蔦松里大埤路113號","屏東市棒球路1號","宜蘭縣羅東鎮公正路666號","花蓮市達古湖灣大路1號"]
else:
    pass
print(address_list)

#取得各天氣觀測站資訊
quote_page = "https://e-service.cwb.gov.tw/wdps/obs/state.htm"
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")
all_observe_station_data_list = []
col_name_list = []
row_index = 0
for observe_station_row in soup.find_all("tr"):
    observe_station_data_list = []
    for cell in observe_station_row.find_all("td"):
        try:
            observe_station_data = cell.find("p").text
        except:
            try:
               observe_station_data = cell.find("span").text 
            except:
                print("can not find text")
            else:
                observe_station_data_list.append(observe_station_data)
        else:
            observe_station_data_list.append(observe_station_data)
    observe_station_data_list.append(row_index)
    if(len(observe_station_data_list) > 4):
        if( observe_station_data_list[0] != "站號"):
            all_observe_station_data_list.append(observe_station_data_list)
        else:
            col_name_list = observe_station_data_list
    row_index += 1

#將觀測站資訊存成dataframe之後有需要可存成csv
all_observe_station_data_table = pd.DataFrame(all_observe_station_data_list, columns = col_name_list)
all_observe_station_data_table.set_index("站名", inplace = True)
# all_observe_station_data_table.set_index("資料起始日期", inplace = True)
# all_observe_station_data_table.set_index("撤站日期", inplace = True)
print(all_observe_station_data_table.index.names)

#找離各球場最近的觀測站，順便將各球場的經緯度座標存到stadium_lnglat_list = []
stadium_lnglat_list = []
each_min_distances = []
for address in address_list:
    g = geocoder.arcgis(address)
    stadium_latlng = g.latlng
    min_distance_between_stadium_and_station = ["",39400,"","",""] 
    find_min_distance(all_observe_station_data_list,min_distance_between_stadium_and_station,stadiums,address_list.index(address),each_min_distances,["2013-03-23","2019-10-17"])
    #找到最小距離後再存球場經緯度
    stadium_latlng.reverse()
    stadium_lnglat_list.append(stadium_latlng)


distance_between_stadium_and_station_table = pd.DataFrame(each_min_distances,columns = ["球場","最短距離","觀測站","資料起始日期","撤站日期"])
print(distance_between_stadium_and_station_table)

stadium_location  = pd.DataFrame(stadium_lnglat_list, index = stadiums, columns = latitude_and_longitude)
print(stadium_location)

#輸出資料
stadium_location.to_excel('各球場位置.xls')
distance_between_stadium_and_station_table.to_excel('各球場對應觀測站.xls')




