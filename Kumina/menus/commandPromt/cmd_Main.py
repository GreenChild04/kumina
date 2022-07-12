from commands.cmd_userKey import Cmd_UserKey
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from fun.parser.parser import Parser
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from fun.parser.udr import UdrParser
from utils.cmdUtils.userKeyUtils import UserKeyUtils
import os


class Cmd_Main:
    def __init__(self, user):
        self.user = user
        self.isUDR = False

    def run(self):
        try:
            os.system("cls")
        except:
            os.system("clear")
        print(f'GreenChild {SystemConfigUtils().load("CMD_NAME")} [Version {SystemConfigUtils().load("CMD_VERSION")}]\n(c) GreenChild Corporation. All rights reserved.')
        while True:
            if not self.isUDR:
                inpit = input(f'\nK:/user/{str(UserKeyUtils(self.user).load("USERNAME"))}>')
                print()
                parser = Parser(inpit, self.user)
                self.isUDR = parser.run()
            elif UserKeyUtils(self.user).load("HACK_PERM") == "Green":
                inpit = input(f'\n{str(UserKeyUtils(self.user).load("USERNAME"))}@kumina:~# ')
                print()
                parser = UdrParser(inpit, self.user)
                self.isUDR = parser.run()
