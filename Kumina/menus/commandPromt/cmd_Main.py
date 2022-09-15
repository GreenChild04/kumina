from commands.cmd_userKey import Cmd_UserKey
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from fun.parser.parser import Parser
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from udr.udrLock.udrLock import UdrLock
from udr.utils.udrUtils import clear
import sys
import os


class Cmd_Main:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.isUDR = False

    def run(self):
        clear()
        print(f'GreenChild {SystemConfigUtils().load("CMD_NAME")[:3]} [Version {SystemConfigUtils().load("CMD_VERSION")}]\n(c) GreenChild Corporation. All rights reserved.')
        while True:
            inpit = input(f'\nK:/user/{str(UserKeyUtils(self.user).load("USERNAME"))}>')
            print()
            parser = Parser(inpit, self.user)
            self.isUDR = parser.run()
            if self.isUDR and UdrLock().isActRight(UserKeyUtils(self.user).load("INA")):
                Cmd_Udr = __import__("menus.commandPromt.cmd_udr")
                Cmd_Udr.commandPromt.cmd_udr.Cmd_Udr(self.user, self.pwd).run()
                sys.exit()
