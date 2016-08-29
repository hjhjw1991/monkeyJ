# -×- coding:utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as MR
from util import *
    
INTERNAL = 1
class Case(object):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.__class__+":"+self.name;
        
    def getName(self):
        return self.name
    
    def performActionOn(self, device):
        raise NotImplementedError()

class InputMethodCase(Case):
    action = []
    search = [(1188,165),(342,346)]# click search bar to invoke IME
    clearSearch = (1152,357)
    device = None
    def navToSearch(self):
        for (x, y) in self.search:
            self.device.touch(x, y, 'DOWN_AND_UP')
            MR.sleep(INTERNAL)
    
    def clear(self):
        self.device.touch(self.clearSearch[0], self.clearSearch[1], 'DOWN_AND_UP')
            
    def performActionOn(self, device):
        self.device = device
        self.navToSearch()
        
    def setTouchAction(self, action):
        self.action = action
        
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
        if not self.action:
            self.action = []
        for c in pinyin:
            self.action.append(keyToPoint[pinyinMap[c.lower()]])
        
class ShortcutPhraseCase(InputMethodCase):
    
    @printNameDecor
    def performActionOn(self, device):
        if not device:
            raise RuntimeError("device is null")
        super(ShortcutPhraseCase, self).performActionOn(device)
        for (x, y) in self.action:
            device.touch(x, y, 'DOWN_AND_UP')
            MR.sleep(INTERNAL)
