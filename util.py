# -*- coding:utf-8 -*-
from config.config import pinyinMap
from datetime import date


# noinspection PyPep8Naming
def getToday():
    return date.today()


def pinyinToTouch(pinyin, brand):
    ret = []
    if not brand:
        return ret
    for c in pinyin:
        ret.append(brand.keyToPoint[pinyinMap[c.lower()]])
    return ret


def printNameDecor(method):
    def method_wrapper(*args, **kwargs):
        if hasattr(args[0], 'name'):
            print getattr(args[0], 'name')
        return method(*args, **kwargs)
    return method_wrapper
    
    
def debug(isDebug):
    def method_decor(method):
        def method_wrapper(*args, **kwargs):
            if isDebug == True:
                print "DEBUG/executing:"+method.__name__
            return method(*args, **kwargs)
        return method_wrapper
    return method_decor
