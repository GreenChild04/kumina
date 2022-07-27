import sys
from tqdm import tqdm
from utils.tond.dataUtils import DATA_UTILS
from utils.tond.CMD_dataCheck import COMMAND_DATACHECK
from utils.cmdUtils.userKeyUtils import UserKeyUtils
import os
import utils.tond.Encryption as encryption
from dataclasses import dataclass
from zipfile import ZipFile
from pathlib import Path
import pickle
import zipfile


class FolderUtils:
    def __init__(self, user):
        self.dataUtils = DATA_UTILS()
        self.dataCheck = COMMAND_DATACHECK()
        self.user = user
        self.dirName = self.getDirName()
        self.uku = UserKeyUtils(user)

    def getDirName(self):
        dir = os.getcwd()
        dirName = os.path.join(dir, 'user', str(self.user), 'dir')
        return dirName

    def save(self, loc, obj, password):
        if not os.path.exists(self.dirName):
            os.makedirs(self.dirName)

        with Path(os.path.join(self.dirName, loc)) as file:
            preCrypt = self.fileToString(obj)
            final = encryption.encryptData(preCrypt, password)
            file.write_bytes(final)

    def load(self, loc, password):
        with Path(os.path.join(self.dirName, loc)) as file:
            decrypt = encryption.decryptData(password, file.read_bytes())
            byted = self.stringToFile(decrypt)
            return byted

    def jSave(self, loc, password, newPassword):
        old_data = self.load(loc, password)
        toString = self.fileToString(old_data)
        final = encryption.encryptData(toString, newPassword)

        with Path(os.path.join(loc)) as file:
            file.write_bytes(final)

    def jLoad(self, loc, password, newPassword):
        data = None

        with Path(loc) as file:
            decrypt = encryption.decryptData(password, file.read_bytes())
            data = decrypt

        with Path(os.path.join(self.dirName, loc)) as file2:
            encrypt = encryption.encryptData(data, newPassword)
            file2.write_bytes(encrypt)

    def fileToString(self, file):
        pikkled = pickle.dumps(file)
        converted = pikkled.hex()
        return converted

    def stringToFile(self, string2):
        byte = bytes.fromhex(string2)
        fixed = pickle.loads(byte)
        return fixed


@dataclass()
class fileObject:
    fileData: bytes = None
    fileDict: dict = None
    loadingBar: vars = None

    def save(self, locs, isFile):
        zipName = 'temp.zip'

        with ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED) as file:
            for i in locs:
                if isFile:
                    FolderZip(zipName, file, i).run()
                else:
                    print(f"Zipping File [{i}]")

                    file.write(str(i))
        print("Done!")

        print("\nSaving Files...")
        self.fileData = Path(zipName).read_bytes()
        os.remove(zipName)
        print("Done!")

    def load(self):
        zipName = 'temp.zip'

        print("\nLoading files:")
        Path(zipName).write_bytes(self.fileData)
        print("Done!\n")

        with ZipFile(zipName, 'r', zipfile.ZIP_DEFLATED) as file:
            file.printdir()
            print("\nExtracting Files...")
            file.extractall()
            print("Done!")
        os.remove(zipName)


class FolderZip:
    def __init__(self, zipName, zipObj: ZipFile, dirName):
        self.zipName = zipName
        self.zipObj = zipObj
        self.dirName = dirName
        self.bar = ''

    def filePaths(self):
        filePaths = []

        for root, directories, files in os.walk(self.dirName):
            for filename in files:
                filePath = os.path.join(root, filename)
                filePaths.append(filePath)
        return filePaths

    def run(self):
        filePaths = self.filePaths()
        self.bar = tqdm(total=len(filePaths), position=0)
        self.bar.set_description(f'Zipping Files')
        for file in filePaths:
            self.bar.set_description(f'Zipping Files [{file}]')
            self.zipObj.write(file)
            self.bar.update()
