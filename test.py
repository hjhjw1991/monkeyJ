#!usr/bin/python
# -*- coding:utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from case import ShortcutPhraseCase
from config.config import *
from util import getToday

# connect to device, obtain a MonkeyDevice
device = MonkeyRunner.waitForConnection()
print "waiting for connection..."

# install package
# device.removePackage(packageName)
# device.installPackage(pathOfApk)

# run app
runComponent = packageName+'/'+launcherActivity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(5)# wait for activity

"""
tutorial
# screen shot
# result = device.takeSnapshot()
# save screenshot
# result.writeToFile('shot.png', 'png')
# click at location
# device.touch(150,685, 'DOWN_AND_UP')
# MonkeyRunner.sleep(3)# wait for animation
# drag from A to B
# device.drag((550, 1250), (550, 850), 2)
# MonkeyRunner.sleep(3)

# device.press('KEYCODE_BACK', 'DOWN_AND_UP')
"""
logroot = 'log'
today = str(getToday())
brand = Huawei6P
# brand = RedmiNote2
subdir = str.join('/',(logroot,today,brand.__name__))
preceeding = ''
phrases = []
mycase = {}

import os
if not os.path.exists(subdir):
    os.makedirs(subdir)
    
def navToSearch(method):
    def wrapper(*args, **kwargs):
        action = [brand.searchButton, brand.searchBar]
        for act in action:
            device.touch(act[0],act[1], 'DOWN_AND_UP')
            MonkeyRunner.sleep(2)
        return method(*args, **kwargs)
    return wrapper


def performTest(cases, device):
    timeout = 5
    index = 1
    for case in cases:
        case.performActionOn(device)
        MonkeyRunner.sleep(timeout)
        screen = device.takeSnapshot()
        screen.writeToFile(str.join('/', (subdir, (case.getName()+"-the-"+str(index)+(" th" if index>1 else "st") +".png"))),'png')
        index += 1


@navToSearch
def testInputShortcutPhrase():
    pickAndCommitPhrase = [brand.firstCandidate, brand.shownPhrase, brand.targetPhrase]
    
    case = ShortcutPhraseCase("Shortcut Phrase Case: 测试多条快捷短语".decode("utf-8"), brand)
    case.addPinyinInput(mycase['head'])
    case.extendTouchAction(pickAndCommitPhrase)
    suite = [case]
    
    performTest(suite, device)
    MonkeyRunner.sleep(5)
    device.touch(brand.clearSearchButton[0],brand.clearSearchButton[1], 'DOWN_AND_UP')


def prepareToAddPhrase():
    case = ShortcutPhraseCase("Shortcut Phrase Case: 打开添加删除快捷短语界面".decode("utf-8"), brand)
    navToShortcutPhrase = [brand.SLogo,brand.ShortcutPhraseEntry,brand.ShortcutPhraseModifyEntry]
    case.setTouchAction(navToShortcutPhrase)
    performTest([case], device)
    MonkeyRunner.sleep(3)


def deleteTheHeading(count):
    manage = brand.manage
    anchor = brand.firstRecordAnchor
    step = brand.gapBetweenPhrase
    delete = brand.deletePhraseButton
    case = ShortcutPhraseCase(("Shortcut Phrase Case: 删除快捷短语:"+str(count)+"条").decode("utf-8"), brand)
    case.setTouchAction([manage])
    for i in range(count):
        select = (anchor[0],anchor[1]+step*i)
        case.appendTouch(select)
    case.appendTouch(delete)
    performTest([case], device)


def addShortcutPhrase(phraseSet):
    cases = []
    head = phraseSet['head']
    for phrase in phraseSet['body']:
        case = ShortcutPhraseCase("Shortcut Phrase Case: 添加快捷短语:".decode("utf-8")+head+phrase, brand)
        case.setTouchAction([brand.pressAddPhrase])
        case.addPinyinInput(head)
        case.appendTouch(brand.firstCandidate)
        case.addPinyinInput(phrase)
        case.appendTouch(brand.firstCandidate)
        case.appendTouch(brand.pressSavePhrase)
        cases.append(case)
    return cases


@navToSearch
def testAddShortcutPhrase():
    prepareToAddPhrase()
    
    cases = addShortcutPhrase(mycase)
    performTest(cases, device)
    MonkeyRunner.sleep(5)
    
    # deleteTheHeading(len(phrases))


@navToSearch
def testAddEmojiPhrase():
    prepareToAddPhrase()

    expression = 'heihei'
    case = ShortcutPhraseCase(("Shortcut Phrase Case: 测试输入表情"+expression).decode("utf-8"), brand)
    case.setTouchAction([brand.pressAddPhrase])
    case.addPinyinInput('ceshi')
    case.appendTouch(brand.firstCandidate)
    case.addPinyinInput(expression)
    case.appendTouch(brand.firstCandidate)
    case.appendTouch(brand.firstCandidate)
    case.appendTouch(brand.pressSavePhrase)
    performTest([case], device)

    deleteTheHeading(1)


@navToSearch
def testTouchOutsideShortcutPhrase():
    prepareToAddPhrase()
    
    cases = addShortcutPhrase(mycase)
    performTest(cases, device)
    device.press('KEYCODE_BACK', 'DOWN_AND_UP')
    MonkeyRunner.sleep(2)
    
    inputPhraseAndClickOutside(mycase)
    
    device.touch(brand.clearSearchButton[0], brand.clearSearchButton[1], 'DOWN_AND_UP')
    MonkeyRunner.sleep(2)
    prepareToAddPhrase()
    deleteTheHeading(len(mycase['body']))


def inputPhraseAndClickOutside(mycase):
    case = ShortcutPhraseCase("Shortcut Phrase Case: 测试多条快捷短语窗口外部点击".decode("utf-8"), brand)
    case.addPinyinInput(mycase['head'])
    case.extendTouchAction([brand.firstCandidate, brand.shownPhrase])
    suite = [case]
    name = case.name
    case.name = name+"点击前".decode("utf-8")
    performTest(suite, device)
    case.name = name+"点击后".decode("utf-8")
    case.setTouchAction([brand.outside])
    performTest(suite, device)
    

if __name__ == "__main__":
    phrases = ['diyitiao',
                'diertiao',
                'disantiao']
    preceeding = 'ceshi'
    mycase = {'head':preceeding,'body':phrases}
    
    print '----perform test----'
    # testAddShortcutPhrase()
    testInputShortcutPhrase()
    # testAddEmojiPhrase()
    # testTouchOutsideShortcutPhrase()
    # performTestShortcutPhrase()
    print '----finished----'
