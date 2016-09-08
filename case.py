# -×- coding:utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as MR
from util import *
    
INTERNAL = 2
class Case(object):
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    def __repr__(self):
        return self.__class__+":"+self.name;
        
    def getName(self):
        return self.name
    
    def performActionOn(self, device):
        raise NotImplementedError()

class InputMethodCase(Case):
    action = []
    device = None
    
    def setDevice(self, device):
        self.device = device
        
    def performActionOn(self, device):
        raise NotImplementedError()
        
    def setTouchAction(self, action):
        self.action = list(action)
        
    def extendTouchAction(self, action):
        if not self.action:
            self.action = []
        self.action.extend(action)
        
    def appendTouch(self, action):
        if not isinstance(action, tuple):
            raise RuntimeError("action must be tuple")
        self.extendTouchAction([action])
    
    @debug(False)
    def addPinyinInput(self, pinyin):
        self.extendTouchAction(pinyinToTouch(pinyin, self.brand))
        
class ShortcutPhraseCase(InputMethodCase):
    
    @printNameDecor
    def performActionOn(self, device):
        if not device:
            raise RuntimeError("device is null")
        super(ShortcutPhraseCase, self).setDevice(device)
        for (x, y) in self.action:
            device.touch(x, y, 'DOWN_AND_UP')
            MR.sleep(INTERNAL)
