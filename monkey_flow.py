#!usr/bin/python
# -*- coding:utf-8 -*-

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from case import ShortcutPhraseCase
from config.config import pathOfApk,packageName,launcherActivity

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
logroot = "log/"
import os
if not os.path.exists(logroot):
    os.mkdir(logroot)

first = (162,1397)# click 测试 candidate
shownPhrase = (621,1397)# click shortcut phrase
targetPhrase = (382,1616)# pick the first shortcutphrase
pickAndCommitPhrase = [first, shownPhrase]
    
def performTest(cases, device):
    print '----perform test----'
    timeout = 5
    index = 1
    for case in cases:
        case.performActionOn(device)
        MonkeyRunner.sleep(timeout)
        screen = device.takeSnapshot()
        screen.writeToFile(logroot+case.getName()+str(index)+'.png','png')
        index += 1
    print '----finished----'

def performTestShortcutPhrase():
    case = ShortcutPhraseCase("Shortcut Phrase Case: 测试多条快捷短语".decode("utf-8"))
    case.setTouchAction([])
    case.addPinyinInput('ceshi')
    case.extendTouchAction(pickAndCommitPhrase)
    suite = [case]
    performTest(suite, device)
    # MonkeyRunner.sleep(5)
    # case.clear()

if __name__ == "__main__":
    performTestShortcutPhrase()
