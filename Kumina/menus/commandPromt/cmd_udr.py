from commands.cmd_userKey import Cmd_UserKey
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from fun.parser.udr import UdrParser
from menus.commandPromt.cmd_Main import Cmd_Main
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from udr.utils.udrUtils import clear
import os
import sys


class Cmd_Udr:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.isUDR = False

    def run(self):
        clear()
        udr = SystemConfigUtils().load("CMD_NAME")[3:]
        print(f'GreenChild {udr} [Version {SystemConfigUtils().load("CMD_VERSION")}]\n(c) GreenChild Corporation. All rights reserved.')
        while True:
            inpit = input(f'\n{str(UserKeyUtils(self.user).load("USERNAME"))}@kumina:~# ')
            print()
            parser = UdrParser(inpit, self.user, self.pwd)
            self.isUDR = parser.run()
            if not self.isUDR:
                Cmd_Main(self.user, self.pwd).run()
                sys.exit()

