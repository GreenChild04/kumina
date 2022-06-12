from menus.productLock import ProductLock
from menus.commandPromt.cmd_Main import Cmd_Main
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
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
    runCmd(user)
    Cmd_Main(user).run()


process()
# Process
