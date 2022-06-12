from commands.cmd_userKey import Cmd_UserKey
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from fun.parser.parser import Parser
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
import os


class Cmd_Main:
    def __init__(self, user):
        self.user = user

    def run(self):
        os.system("cls")
        print(f'GreenChild {SystemConfigUtils().load("CMD_NAME")} [Version {SystemConfigUtils().load("CMD_VERSION")}]\n(c) GreenChild Corporation. All rights reserved.')
        while True:
            inpit = input(f'\nT:\\Users\\{str(UserKeyUtils(self.user).load("USERNAME")).replace(" ", "_").upper()}>')
            print()
            parser = Parser(inpit, self.user)
            parser.run()
