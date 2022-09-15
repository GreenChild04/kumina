from pathlib import Path
from utils.cmdUtils.userKeyUtils import UserKeyUtils
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
import json
import os


class CmdLoad:
    def __init__(self):
        self.uku = UserKeyUtils(None)
        self.scu = SystemConfigUtils()

    def run(self, interPackage):
        self.uku = UserKeyUtils(interPackage.user)
        if interPackage.syntax:
            self.codeLoad(interPackage.syntax[0])
        else:
            print("Write down the location of your vexcode file")
            loc = input(">")
            self.codeLoad(loc)

    def codeLoad(self, loc):

        if not os.path.exists(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC"))):
            os.makedirs(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC")))

        with open(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC"), loc), 'r+') as file:
            contents = json.load(file)
            code = contents["textContent"]

        newLoc = loc.split('.')[0] + ".py"

        with Path(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC"), newLoc)) as file:
            file.write_text(code)


class CmdSave:
    def __init__(self):
        self.scu = SystemConfigUtils()

    def run(self, interPackage):
        if interPackage.syntax:
            self.codeSave(interPackage.syntax[0])
        else:
            print("Write down the location of your python script")
            loc = input(">")
            self.codeSave(loc)

    def codeSave(self, loc):

        newloc = loc.split(".")[0] + ".iqpython"

        with Path(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC"), loc)) as file:
            code = file.read_text()

        with open(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC"), newloc), 'r+') as file:
            contents = json.load(file)

        os.remove(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC"), newloc))

        with Path(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC"), newloc)) as file:
            contents2 = contents
            contents2["textContent"] = code
            a = json.dumps(contents2)
            file.write_text(a)

        os.remove(os.path.join(os.getcwd(), self.scu.load("VEX.CODE_LOC"), loc))
