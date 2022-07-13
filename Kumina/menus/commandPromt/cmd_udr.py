from commands.cmd_userKey import Cmd_UserKey
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from fun.parser.udr import UdrParser
from menus.commandPromt.cmd_Main import Cmd_Main
from utils.cmdUtils.userKeyUtils import UserKeyUtils
import os
import sys


class Cmd_Udr:
    def __init__(self, user):
        self.user = user
        self.isUDR = False

    def run(self):
        try:
            os.system("cls")
        except:
            os.system("clear")
        udr = SystemConfigUtils().load("CMD_NAME")[3:]
        print(f'GreenChild {udr} [Version {SystemConfigUtils().load("CMD_VERSION")}]\n(c) GreenChild Corporation. All rights reserved.')
        while True:
            inpit = input(f'\n{str(UserKeyUtils(self.user).load("USERNAME"))}@kumina:~# ')
            print()
            parser = UdrParser(inpit, self.user)
            self.isUDR = parser.run()
            if not self.isUDR:
                Cmd_Main(self.user).run()
                sys.exit()

