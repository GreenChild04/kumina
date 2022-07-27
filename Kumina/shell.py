from menus.productLock import ProductLock
from menus.commandPromt.cmd_Main import Cmd_Main
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from menus.commandPromt.cmd_udr import Cmd_Udr
from udr.udrLock.udrLock import UdrLock
import fun.web.test
import os

# Init
productLock = ProductLock()


def runCmd(username):
    try:
        Cmd_Main(username).run()
    except Exception as error:
        print(error)
        print(f"\nCRITICAL: {SystemConfigUtils().load('CMD_NAME')} HAS CRASHED")

        input('')
        runCmd(username)


# Init


# Process
def process():
    try:
        os.system("cls")
    except:
        os.system("clear")
    # fun.web.test.run()
    user, password = productLock.run()
    #runCmd(user)
    if UdrLock().isActRight(UserKeyUtils(user).load("INA")):
        Cmd_Udr(user, password).run()
    else:
        Cmd_Main(user, password).run()


if __name__ == "__main__":
    process()
# Process
