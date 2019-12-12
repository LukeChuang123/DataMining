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
def try_input(driver,img,text,count=0):
    try:
        driver.find_element_by_xpath('//td[img/@src="'+img+'"]').send_keys(text)
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
def get_table(soup):
    try:
        table_rows = soup.find_all("tbody")[1].find_all("tr")
    except:
        table_rows = soup.find_all("tbody")[0].find_all("tr")
    else:
        pass

    # print(table_rows)

    col_name_list = []
    for col_name in table_rows[1].find_all("th"):
        col_name_list.append(col_name.text)
    col_name_list[10] = col_name_list[10][:-1]
    col_name_list[14] = col_name_list[14][:-1]
    print(col_name_list)

    row_list = []
    for row in table_rows[3:]:
        row_cell_list = []
        for cell in row.find_all("td"):
            if(cell.text == '...\xa0'):
                row_cell_list.append(None)
            else:
                row_cell_list.append(cell.text)
        print(row_cell_list)
        row_list.append(row_cell_list)

    table = pd.DataFrame(row_list,columns = col_name_list)
    print(table)

    return table


























    


