from menus.productLock import ProductLock
from menus.commandPromt.cmd_Main import Cmd_Main
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from menus.commandPromt.cmd_udr import Cmd_Udr
import fun.web.test

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
    # fun.web.test.run()
    user = productLock.run()
    #runCmd(user)
    if UserKeyUtils(user).load("HACK_PERM") == "Green":
        Cmd_Udr(user).run()
    else:
        Cmd_Main(user).run()


if __name__ == "__main__":
    process()
# Process
