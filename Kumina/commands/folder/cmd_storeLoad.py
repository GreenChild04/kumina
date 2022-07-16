from utils.cmdUtils.folderUtils import FolderUtils
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from utils.cmdUtils.folderUtils import fileObject
import utils.tond.Encryption as encryption
from pathlib import Path
import subprocess
import os
import json
import platform


class CmdStore:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.uku = UserKeyUtils(None)

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.uku = UserKeyUtils(interPackage.user)
        if interPackage.syntax:
            syntax = list(interPackage.syntax)
            peopleLoc = syntax.pop(0)
            self.fileStore(syntax, peopleLoc)
        else:
            print("Write down the location you want to store the file at")
            loc = input(">")
            print("Write down the mode you want to store it as")
            mode = int(input(">"))
            print("Now write down the locations of the files and separate them with a ','")
            fileLoc = input(">")
            fileLoc = fileLoc.split(",")
            print()
            print('Storing Data...')
            self.fileStore(fileLoc, loc)
            print("Done!")

    def fileStore(self, loc, peopleLoc):
        try:
            file = fileObject()

            file.save(loc)

            self.fu.save(peopleLoc, file, self.uku.loadActivation())
        except Exception:
            print(f"ERROR: FILE '{loc}' NOT FOUND")


class CmdLoad:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.uku = UserKeyUtils(None)

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.uku = UserKeyUtils(interPackage.user)
        if interPackage.syntax:
            self.fileLoad(interPackage.syntax[0])
        else:
            print("Write down the location of the files you want to load")
            loc = input(">")
            self.fileLoad(loc)

    def fileLoad(self, loc):
        try:
            pikkled = self.fu.load(loc, self.uku.loadActivation())
            pikkled.load()
        except Exception as error:
            print(f"ERROR: FILE '{loc}' DOES NOT EXIST")


class CmdCheck:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.uku = UserKeyUtils(None)
        self.dirName = self.fu.getDirName()

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(interPackage.user)

        try:
            os.makedirs(self.dirName)
        except: pass

        contents = os.listdir(self.dirName)
        print("Here are the files stored:\n")

        count = 0
        for i in contents:
            count += 1
            print(f"{count}. {i}")


class CmdRemove:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.uku = UserKeyUtils(None)
        self.dirName = self.fu.getDirName()

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(interPackage.user)
        if interPackage.syntax:
            self.removeFiles(interPackage.syntax)
        else:
            print("Write down the files you want to remove and separate them with a ','")
            inpit = input(">").split(',')
            self.removeFiles(inpit)

    def removeFiles(self, files):
        print("Removing Files...")
        for i in files:
            try:
                print(f"-removing [{i}]")
                os.remove(os.path.join(self.dirName, i))
            except: pass

        print("Done!")


class CmdEject:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(None)

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(interPackage.user)
        if interPackage.syntax:
            self.ejectFile(interPackage.syntax)
        else:
            syntax = []
            print("Write down the file you want to eject")
            syntax.append(input(">"))
            print("Write down the password you want to encrypt it to")
            syntax.append(input(">"))
            self.ejectFile(syntax)

    def ejectFile(self, files):
        print("Ejecting Files...")
        try:
            print(f"\n-ejecting [{files[0]}]")
            self.fu.jSave(files[0], self.uku.loadActivation(), files[1])


        except: pass
        print("Done!")


class CmdInject:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(None)

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(interPackage.user)
        if interPackage.syntax:
            self.injectFile(interPackage.syntax)
        else:
            syntax = []
            print("Write down the location of the data you want to inject")
            syntax.append(input(">"))
            print("Write down the password to the file")
            syntax.append(input(">"))
            self.injectFile(syntax)

    def injectFile(self, files):
        print("Injecting Files...")
        try:
            print(f"-injecting [{files[0]}]")
            self.fu.jLoad(files[0], files[1], self.uku.loadActivation())
        except: pass
        print("Done!")


class CmdOpen:
    def __init__(self):
        self.exPath = self.getPath()
        self.path = os.getcwd()

    def run(self, interPackage):
        subprocess.run([self.exPath, self.path])

    def getPath(self):
        path = ""
        plat = platform.system()

        if plat == "Windows":
            path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        elif plat == "Linux":
            path = 'xdg-open'
        else:
            raise "ERROR: Are you using a potato to run my program???"

        return path
