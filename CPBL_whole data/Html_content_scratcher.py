import re

import urllib
from bs4 import BeautifulSoup

import All_html_visitor
import Data_processor

import time
import pandas as pd

team_link_list = [[] for i in range(5)]
# team_list = []

def __init__(self,root_quote_page_assigned,html_assigned):

    self.html = html_assigned
    self.root_quote_page = root_quote_page_assigned

#同時抓取各隊連結和各隊名稱，存在team_link_list這個二維list。0:連結；1:隊名
def get_team_links(self):  
    all_teams = (self.html.find("ul",attrs = {"id":"menu-submenu2"}).contents)[3:13:2]
    for team_index in range(len(all_teams)):
        team_link = self.root_quote_page + all_teams[team_index].a.get("href")
        team_link_list[team_index].append(team_link)
        team_link_list[team_index].append(all_teams[team_index].a.text) 

    return team_link_list
def get_position_links(self,html_assigned): 
    self.html = html_assigned 
    position_html = self.html.find("select",id="pos").contents
    position_list = [position.text for position in position_html[3:len(position_html):2]]
    return position_list
def get_grade_links(self,html_assigned):  
    self.html = html_assigned
    grade_html = self.html.find("select",id="sgrade").contents
    grade_list = [grade.text for grade in grade_html[1:len(grade_html):2]]
    return grade_list
def get_year_links(self,html_assigned):  
    self.html = html_assigned
    year_html = self.html.find("select",id="syear").contents
    year_list = [year.text for year in year_html[-2:-len(year_html):-2]]
    return year_list
def get_html(self,page_source_assigned):
    self.page_source = page_source_assigned
    soup = BeautifulSoup(self.page_source, "html.parser")
    return soup
def try_click(driver,tag,text,count=0):
    try:
        driver.find_element_by_xpath("//"+tag+"[contains(text(),'"+text+"')]").click()
    except:
        time.sleep(2)
        count+=1
        if(count <2):
            try_click(driver,tag,text,count)
        else:
            print("cannot locate element",tag,text)
def try_click_img(driver,img,count=0):
    try:
        driver.find_element_by_xpath('//a[img/@src="'+img+'"]').click()
    except:
        time.sleep(2)
        count+=1
        if(count <2):
            try_click(driver,img,count)
        else:
            print("cannot locate element",img)
def try_get_table(driver,table_index,count=0):
    try:
        table = pd.read_html(driver.page_source)[table_index]
    except:
        time.sleep(2)
        count+=1
        if(count <5):
            try_get_table(driver,table_index,count)
        else:
            print("cannot find table")
    else:
        return table
























    


