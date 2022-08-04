import sys
from random import random
import bcrypt
from utils.tond.dataUtils import DATA_UTILS
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from pathlib import Path
import utils.tond.Encryption as encryption
import json
import os
from getpass import getpass


class Cmd_UserKey:
    def __init__(self, user):
        self.dataUtils = DATA_UTILS()
        self.dir = os.getcwd()
        self.dirName = os.path.join(self.dir, 'user', str(user))
        self.fileName = os.path.join(self.dirName, 'user.key')
        self.uku = UserKeyUtils(user)
        self.pog = {}

    def checkKey(self):
        try:
            with open(self.fileName, 'r+') as file:
                a = self.uku.loadActivation()
                passCheck = a.split('?')[2]
                if passCheck == self.uku.load('PASSWORD'):
                    return True
                else:
                    return False

        except:
            return False

    def createKey(self):

        if not os.path.exists(self.dirName):
            os.mkdir(self.dirName)

        try:
            os.remove(self.fileName)
        except:
            pass

        try:
            with Path("activation.iac") as file:
                self.pog["INA"] = file.read_text()
            os.remove("activation.iac")
        except:
            self.pog["INA"] = None

        print()

        self.ask('Full Name', 'NAME')
        self.ask('Age', 'AGE')
        self.ask('Address', 'ADDRESS')
        self.ask("Email", "EMAIL")
        print()
        self.ask('Username', "USERNAME")
        self.createPassword('Password', "Confirm")

        self.genActivation()

        UserKeyUtils(self.pog["USERNAME"]).setFirst(self.pog)

        print('Done!')
        input('\npress enter to close ')

    def ask(self, msg, loc):
        temp = input(f'{msg}: ')
        self.pog[loc] = temp

    def createPassword(self, msg, msg_two):
        print()
        temp = getpass(f'{msg}: ')
        temp2 = getpass(f'{msg_two}: ')

        if temp != temp2:
            print("Error: Passwords don't match!")
            self.createPassword(msg, msg_two)

        passwd = str(temp).encode()
        salt = bcrypt.gensalt()

        try:
            os.makedirs(os.path.join(os.getcwd(), 'user', self.pog["USERNAME"]))
        except:
            pass

        with Path(os.path.join(os.getcwd(), 'user', self.pog["USERNAME"], 'salt')) as file:
            file.write_bytes(salt)

        hashed = bcrypt.hashpw(passwd, salt)

        with Path(os.path.join(os.getcwd(), 'user', self.pog["USERNAME"], 'password')) as file:
            file.write_bytes(hashed)

        self.pog['PASSWORD'] = hashed.decode()

    def genActivation(self):
        lettus = [
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z',
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z',
            '_',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '0',
            '!',
            '@',
            '#',
            '$',
            '%',
            '^',
            '&',
            '*',
            '(',
            ')',
            '{',
            '}',
            '[',
            ']',
            '"',
            '\'',
            '/',
            '\\',
            ',',
            '.',
            '~',
            ':',
        ]

        e = ''

        for i in range(120):
            e += lettus[round(random() * (len(lettus) - 1))]

        password = UserKeyUtils(self.pog["USERNAME"]).scuPass()

        activation = '?' + e + '?' + password.decode() + '?'

        self.pog["ACTIVATION"] = encryption.encryptData(activation, password.decode()).decode()

    def checkPassword(self, pwd):
        return self.uku.checkPassword(pwd)
