import readchar
import sys
import time
import os
from commands.cmd_userKey import Cmd_UserKey
import utils.tond.Encryption as encryption
from utils.tond.dataUtils import DATA_UTILS
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from getpass import getpass


class ProductLock:
    def __init__(self):
        self.dataUtils = DATA_UTILS()
        self.uku = UserKeyUtils(None)
        self.scu = SystemConfigUtils()

    def run(self):
        try:
            print(f'*Welcome, to {self.scu.load("CMD_NAME")} {self.scu.load("CMD_VERSION")}!*')
        except:
            self.scu.runSystemPresets()
            print(f'*Welcome, to {self.scu.load("CMD_NAME")} {self.scu.load("CMD_VERSION")}!*')
        return self.userEnter()

    def passwordEnter(self, username):
        inpit = getpass('Password: ')
        userKey = Cmd_UserKey(username)

        try:
            if userKey.checkPassword(inpit):
                print('\nLogin Successful!')
                time.sleep(1.8)
                os.system('cls')
            else:
                print('\n\nError: Password incorrect')
                self.passwordEnter(username)
        except:
            print('\n\nError: User not found')
            self.userEnter()

        if not userKey.checkKey():
            print('\n\nError: User Not Valid')
            self.passwordEnter(username)

    def userEnter(self):
        inpit = input("\nUsername: ")
        if inpit == 'CREATE_KEY':
            Cmd_UserKey(None).createKey()
            sys.exit()
        self.passwordEnter(inpit)
        return inpit
