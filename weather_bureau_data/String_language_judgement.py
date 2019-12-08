#encoding=utf-8
import sys
from imp import reload
reload(sys)
import re
# sys.setdefaultencoding('utf8')

def is_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
def keep_only_chinese(toalter_list):
    for index in range(len(toalter_list)):
        toalter_list[index] = re.findall(r"[\u4e00-\u9fa5]{1,10}",toalter_list[index].replace(" ",""))[0]
    return toalter_list
