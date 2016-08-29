# -*- coding:utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as MR
from com.android.monkeyrunner.recorder import MonkeyRecorder as rec

deviceName = "ENU7N15A30001176"
device = MR.waitForConnection(5, deviceName)
rec.start(device)
