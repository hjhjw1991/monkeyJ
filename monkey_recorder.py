# -*- coding:utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner as MR
from com.android.monkeyrunner.recorder import MonkeyRecorder as rec

Huawei6P = "ENU7N15A30001176"
RedmiNote2 = "5e22aa12"
deviceName = Huawei6P 
device = MR.waitForConnection(5, deviceName)
rec.start(device)
