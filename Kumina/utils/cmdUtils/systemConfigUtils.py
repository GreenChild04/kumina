from random import random
import bcrypt
from utils.tond.dataUtils import DATA_UTILS
import utils.tond.Encryption as encryption
import os


class SystemConfigUtils:
    def __init__(self):
        self.dataUtils = DATA_UTILS()
        self.dirName = self.getDirName()
        self.fileName = self.getFileName()
        self.systemPresets = {}
        self.systemPresetSet()

    def systemPresetSet(self):
        systemPresets = {
            "CMD_NAME": "kumιɳα",
            "CMD_VERSION": 2.4,
            "CRYPT_PASS": "kumιɳα%%!**&@",
            "LOG_LOC": "Log",
            "MUSIC_LOC": "Music",
            "VEX_LOC": "Vex",
            "STONKS_TMP": "__stonks__.tmp",
            "LOG_EXT": "log",
        }
        systemPresets["VEX.CODE_LOC"] = os.path.join(systemPresets["VEX_LOC"], "Code")

        for i in systemPresets:
            self.systemPresets[i] = systemPresets[i]

    def getFileName(self):
        fileName = os.path.join(self.dirName, 'system.config')
        return fileName

    def getDirName(self):
        dir = os.getcwd()
        dirName = os.path.join(dir, 'user', str(None))
        return dirName

    def save(self, item, keyWord):

        tempt = ''

        if not os.path.isfile(self.fileName):
            if not os.path.exists(self.dirName):
                os.makedirs(self.dirName)
            with open(self.fileName, 'w+') as file:
                file.write(str(encryption.encryptData('{}', self.systemPresets["CRYPT_PASS"])))

        with open(self.fileName, 'r+') as file:
            i = encryption.decryptData(self.systemPresets["CRYPT_PASS"], file.readlines(0)[0])
            a = str(self.dataUtils.saveToJsonString(keyWord, item, i))
            encrypt = encryption.encryptData(a, self.systemPresets["CRYPT_PASS"])
            tempt = str(encrypt)

        os.remove(self.fileName)

        with open(self.fileName, 'w+') as file:
            file.write(tempt)

    def load(self, loc):
        with open(self.fileName, 'r+') as file:
            decrypt = encryption.decryptData(self.systemPresets["CRYPT_PASS"], file.readlines(0)[0])
            a = str(self.dataUtils.loadFromJsonString(loc, decrypt))
            return a

    def runSystemPresets(self):

        try:
            os.remove(self.getFileName())
        except:
            pass

        for i in self.systemPresets:
            self.save(self.systemPresets[i], i)
