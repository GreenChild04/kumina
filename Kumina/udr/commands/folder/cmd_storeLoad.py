from udr.utils.folderUtils import FolderUtils
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from udr.utils.folderUtils import fileObject
from udr.utils.udrUtils import HelpMenu
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
        self.hm = HelpMenu("save", {}, [], [
            "-d: sets the saving method for a folder/directory instead of a file",
            "-n: sets the name you want to save it as",
            "-f: sets the file location of selected item",
            "-",
            "file.save: \"filename\" \"file location\"",
            "file.save: -d \"filename\" \"file location\"",
            "file.save: -n/\"filename\" -f/\"file location\"",
            "file.save: -h",
        ])

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.uku = UserKeyUtils(interPackage.user)
        if interPackage.isColon:
            if interPackage.checkSwitch("h") or interPackage.checkSwitch("help"):
                self.hm.makeHelpInfo()
            else:
                if not interPackage.checkSwitch("n") or not interPackage.checkSwitch("f"):
                    syntax = interPackage.inpit
                    peopleLoc = syntax.pop(0)
                    self.fileStore(syntax, peopleLoc, interPackage.checkSwitch("d"), interPackage.pwd)
                elif interPackage.checkSwitch("n") and interPackage.checkSwitch("f"):
                    loc = interPackage.getValue("n", "")
                    files = interPackage.getValue("f", "")
                    self.fileStore([files], loc, interPackage.checkSwitch("d"), interPackage.pwd)
        else:
            self.hm.makeHelpInfo()

    def fileStore(self, loc, peopleLoc, isFile, pwd):
        try:
            file = fileObject()

            file.save(loc, isFile)

            self.fu.save(f"{peopleLoc}.udf", file, f"{self.uku.loadActivation()}`{pwd}")
        except Exception:
            print(f"ERROR: FILE '{loc}' NOT FOUND")


class CmdLoad:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.uku = UserKeyUtils(None)
        self.hm = HelpMenu("load", {}, [], [
            "-n: sets the filename to load",
            "-",
            "file.load: \"name of saved file/directory\"",
            "file.load: -n/\"name of saved file/directory\"",
            "file.load: -h",
        ])

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.uku = UserKeyUtils(interPackage.user)
        if interPackage.isColon:
            if interPackage.checkSwitch("h") or interPackage.checkSwitch("help"):
                self.hm.makeHelpInfo()
            else:
                self.fileLoad(interPackage.getValue("n", 0), interPackage)
        else:
            self.hm.makeHelpInfo()

    def fileLoad(self, loc, inter):
        try:
            pikkled = self.fu.load(f"{loc}.udf", f"{self.uku.loadActivation()}`{inter.pwd}")
            pikkled.load()
        except Exception as error:
            print(f"ERROR: FILE '{loc}' DOES NOT EXIST")


class CmdCheck:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.uku = UserKeyUtils(None)
        self.dirName = self.fu.getDirName()
        self.hm = HelpMenu("list", {}, [], [
            "-",
            "file.list",
            "file.list: -h"
        ])

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(interPackage.user)

        if interPackage.isColon and interPackage.checkSwitch("h"):
            self.hm.makeHelpInfo()
        else:
            try:
                os.makedirs(self.dirName)
            except: pass

            contents = os.listdir(self.dirName)
            print("Here are the files stored:\n")

            count = 0
            for i in contents:
                count += 1
                print(f"{count}. {i.split('.')[0]}")


class CmdRemove:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.uku = UserKeyUtils(None)
        self.dirName = self.fu.getDirName()
        self.hm = HelpMenu("remove", {}, [], [
            "-n: sets the file you want to remove",
            "-",
            "file.remove: \"fileyouwanttoremove\"",
            "file.remove: -n/\"fileyouwanttoremove\"",
            "file.remove: -h"
        ])

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(interPackage.user)

        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                self.removeFiles(interPackage.getValue("n", 0))
        else:
            self.hm.makeHelpInfo()

    def removeFiles(self, files):
        print("Removing File...")
        try:
            print(f"-removing [{files}]")
            os.remove(os.path.join(self.dirName, f"{files}.udf"))
        except: pass

        print("Done!")


class CmdEject:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(None)
        self.hm = HelpMenu("eject", {}, [], [
            "-n: sets the name of the file",
            "-p: sets the new password",
            "-",
            "file.eject: \"name of file\" \"new password\"",
            "file.eject: -n/\"name of the file\" -p/\"new password\"",
            "file.eject: -h",
        ])

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(interPackage.user)

        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                self.ejectFile(interPackage.getValue("n", 0), interPackage.getValue("p", 1), interPackage)
        else:
            self.hm.makeHelpInfo()

    def ejectFile(self, files, pwd, inter):
        print("Ejecting Files...")
        try:
            print(f"\n-ejecting [{files}]")
            self.fu.jSave(f"{files}.udf", f"{self.uku.loadActivation()}`{inter.pwd}", pwd)


        except: pass
        print("Done!")


class CmdInject:
    def __init__(self):
        self.fu = FolderUtils(None)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(None)
        self.hm = HelpMenu("inject", {}, [], [
            "-n: sets the name of the file to inject",
            "-p: sets the password of the file",
            "-",
            "file.inject: \"filename\" \"password\"",
            "file.inject: -n/\"filename\" -p/\"password\"",
            "file.inject: -h"
        ])

    def run(self, interPackage):
        self.fu = FolderUtils(interPackage.user)
        self.dirName = self.fu.getDirName()
        self.uku = UserKeyUtils(interPackage.user)

        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                self.injectFile(interPackage.getValue("n", 0), interPackage.getValue("p", 1), interPackage)
        else:
            self.hm.makeHelpInfo()

    def injectFile(self, files, pwd, inter):
        print("Injecting Files...")
        try:
            print(f"-injecting [{files}]")
            self.fu.jLoad(files, pwd, f"{self.uku.loadActivation()}`{inter.pwd}")
        except: pass
        print("Done!")


class CmdOpen:
    def __init__(self):
        self.exPath = self.getPath()
        self.path = os.getcwd()
        self.hm = HelpMenu("open", helpInfo=[
            "-",
            "file.open",
            "file.open: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon and interPackage.checkSwitch("h"):
            self.hm.makeHelpInfo()
        else:
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
