#encoding=utf-8
import sys
from imp import reload
reload(sys)
# sys.setdefaultencoding('utf8')

def is_contain_chinese(check_str):

    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False