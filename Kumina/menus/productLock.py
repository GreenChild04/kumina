import sys
import time
import os
from commands.cmd_userKey import Cmd_UserKey
import utils.tond.Encryption as encryption
from utils.tond.dataUtils import DATA_UTILS
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from getpass import getpass
from udr.utils.udrUtils import clear


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
        isUserTrue = True

        try:
            if userKey.checkPassword(inpit):
                print('\nLogin Successful!')
                time.sleep(1.8)
                clear()
            else:
                print('\n\nError: Password incorrect')
                inpit = self.passwordEnter(username)
        except:
            print('\n\nError: User not found')
            getpass("\nPress enter to try again")
            shell = __import__("shell")
            clear()
            shell.process()

        if not userKey.checkKey():
            print('\n\nError: User Not Valid')
            self.passwordEnter(username)

        return inpit

    def userEnter(self):
        inpit = input("\nUsername: ")
        if inpit == 'CREATE_KEY':
            Cmd_UserKey(None).createKey()
            sys.exit()
        inpot = self.passwordEnter(inpit)
        return inpit, inpot
