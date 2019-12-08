import re

import urllib
from bs4 import BeautifulSoup

import All_html_visitor
import Data_processor

import time
import pandas as pd

team_link_list = [[] for i in range(5)]
error = []
# team_list = []

def __init__(self,html_assigned):
    self.html = html_assigned
def get_year_links():  
    year_link_list = []
    for year in range(24,30):
        year_link_list.append("http://zxc22.idv.tw/cpbl"+str(year)+"/allgame.asp")
    year_link_list.append("http://zxc22.idv.tw/allgame.asp?clickflag=999")
    # print(year_link_list)
    return year_link_list
def get_html_bydriver(self,page_source_assigned):
    self.page_source = page_source_assigned
    soup = BeautifulSoup(self.page_source, "html.parser")
    return soup
def get_html_bylink(self,link):
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, "html.parser")
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
            error.append("cannot locate element"+" "+tag+" "+text)
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
def get_pages_nums(self,link):
    soup = get_html_bylink(self,link)
    year_options = soup.find("select",onchange="javascript:document.size.submit();").find_all("option")
    # pages_num = len(year_options)
    pages_per_year = [page.text for page in year_options]
    
    return pages_per_year

























    


