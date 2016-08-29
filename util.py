# -*- coding:utf-8 -*-
keyToPoint = {'a':(747, 1616),
             'd':(1071, 1616),
             'g':(441, 1829),
             'j':(747, 1829),
             'm':(1071, 1829),
             'p':(441, 2042),
             't':(747, 2042),
             'w':(1071, 2042),
             }
pinyinMap = {'a':'a',
                'b':'a',
                'c':'a',
                'd':'d',
                'e':'d',
                'f':'d',
                'g':'g',
                'h':'g',
                'i':'g',
                'j':'j',
                'k':'j',
                'l':'j',
                'm':'m',
                'n':'m',
                'o':'m',
                'p':'p',
                'q':'p',
                'r':'p',
                's':'p',
                't':'t',
                'u':'t',
                'v':'t',
                'w':'w',
                'x':'w',
                'y':'w',
                'z':'w'}
                
def pinyinToTouch(pinyin):
    ret = ''
    for c in pinyin:
        ret += pinyinMap[c.lower()]
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
