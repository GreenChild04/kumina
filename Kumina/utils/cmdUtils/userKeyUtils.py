from random import random
import bcrypt
from utils.tond.dataUtils import DATA_UTILS
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
import utils.tond.Encryption as encryption
from pathlib import Path
import os
import json


class UserKeyUtils:
    def __init__(self, user):
        self.user = user
        self.dataUtils = DATA_UTILS()
        self.dirName = self.getDirName()
        self.fileName = self.getFileName()

    def getFileName(self):
        fileName = os.path.join(self.dirName, 'user.key')
        return fileName

    def getDirName(self):
        dir = os.getcwd()
        dirName = os.path.join(dir, 'user', str(self.user))
        return dirName

    def scuPass(self):
        with Path(os.path.join(self.getDirName(), 'password')) as file:
            hashed = file.read_bytes()
        with Path(os.path.join(self.getDirName(), 'salt')) as file:
            salt = file.read_bytes()

        return hashed

    def checkPassword(self, pwd):
        rawPass = self.load('PASSWORD')

        with Path(os.path.join(self.getDirName(), 'salt')) as file:
            salt = file.read_bytes()

        enteredPassword = str(pwd).encode()
        hash = bcrypt.hashpw(enteredPassword, salt)

        if rawPass == hash.decode():
            return True
        else:
            return False

    def save(self, item, keyWord):
        tempt = ''

        if not os.path.isfile(self.fileName):
            with open(self.fileName, 'w+') as file:
                file.write(str(encryption.encryptData('{}', self.scuPass())))

        with open(self.fileName, 'r+') as file:
            i = encryption.decryptData(self.scuPass(), file.readlines(0)[0])
            a = str(self.dataUtils.saveToJsonString(keyWord, item, i))
            encrypt = encryption.encryptData(a, self.scuPass())
            tempt = str(encrypt)

        os.remove(self.fileName)

        with open(self.fileName, 'w+') as file:
            file.write(tempt)

    def load(self, loc):
        with open(self.fileName, 'r+') as file:
            decrypt = encryption.decryptData(self.scuPass(), file.readlines(0)[0])
            a = str(self.dataUtils.loadFromJsonString(loc, decrypt))
            return a

    def setFirst(self, item):
        tempt = ""

        with open(self.fileName, 'w+') as file:
            a = json.dumps(item)
            encrypt = encryption.encryptData(a, item['PASSWORD'])
            tempt = str(encrypt)
            file.write(tempt)

    def loadActivation(self):
        enc = self.load("ACTIVATION")
        dec = encryption.decryptData(self.scuPass().decode(), enc.encode())

        return dec
