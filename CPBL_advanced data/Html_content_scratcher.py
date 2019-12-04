import re

import urllib
from bs4 import BeautifulSoup

import All_html_visitor

batting_link_list = []
pitching_link_list = []

def __init__(self,root_quote_page_assigned,html_assigned):

    self.html = html_assigned
    self.root_quote_page = root_quote_page_assigned

def getHyperLink(self):  

    for item in ["batting","pitching"]:
        #抓含有歷年打擊數據的網頁連結，並將所有連結存到batting_link_list
        all_hyper_link_tags = html.find_all(href = re.compile("^/"+item+"/\d"))
        for hyper_link_tag in all_hyper_link_tags:
            hyper_link = hyper_link_tag.get("href")
            if(item == "batting"):
                batting_link_list.append(root_quote_page+hyper_link)
            else:
                pitching_link_list.append(root_quote_page+hyper_link)
                #抓2019的batting link、pitching link
        if(item == "batting"):
            batting_link_list.append(root_quote_page+"/"+item+"/")
        else:
            pitching_link_list.append(root_quote_page+"/"+item+"/")  
        
    
    #抓含有歷年投球數據的網頁連結，並將所有連結存到pitching_link_list
    # all_pitching_hyper_link_tags = html.find_all(href = re.compile("^/pitching/\d"))
    # for hyper_link_tag in all_pitching_hyper_link_tags:
    #     hyper_link = hyper_link_tag.get("href")
    #     pitching_link_list.append(root_quote_page + hyper_link)
    #     # print(hyper_link)

    #將batting、pitching link表單傳給All_html_visitor讓它一一造訪
    All_html_visitor.__init__(All_html_visitor, batting_link_list, pitching_link_list)
    


