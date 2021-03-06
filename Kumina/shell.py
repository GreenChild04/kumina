from menus.productLock import ProductLock
from menus.commandPromt.cmd_Main import Cmd_Main
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from menus.commandPromt.cmd_udr import Cmd_Udr
from udr.udrLock.udrLock import UdrLock
from udr.utils.udrUtils import clear
from udr.udrScript import UdrScript
from sys import *
import fun.web.test
import os
import subprocess

# Init
productLock = ProductLock()
# Init


# Process
def process():
    clear()
    try:
        a = argv[1]
        UdrScript(a).run()
    except:
        user, password = productLock.run()
        if UdrLock().isActRight(UserKeyUtils(user).load("INA")):
            Cmd_Udr(user, password).run()
        else:
            Cmd_Main(user, password).run()


if __name__ == "__main__":
    process()
# Process
