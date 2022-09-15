import sys
from dataclasses import dataclass
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
import os
import udr.utils.convScript as convScript
import subprocess
import base64


@dataclass()
class InterPackage:
    cmdList: dict
    cmdDir: list
    user: str
    isColon: bool
    inpit: list = None
    switch: dict = None
    pwd: str = None

    def runCommands(self):
        cmd = None

        try:
            a = self.cmdDir[0]
        except:
            sys.exit()

        if self.cmdList.__contains__(self.cmdDir[0]):
            cmd = self.cmdList[self.cmdDir.pop(0)]

        if cmd:
            cmd.run(self)
        else:
            print(f'(Error) Invalid Syntax: Command \'{self.cmdDir[0]}\' not found')

    def checkSwitch(self, switch):
        try:
            for i in self.switch:
                if i == switch:
                    return True
        except:
            return False
        return False

    def isColon(self):
        return self.isColon

    def getValue(self, switch, index=0):
        if self.checkSwitch(switch) and self.switch[switch]:
            return self.switch[switch]
        else:
            try:
                return self.inpit[index]
            except:
                return None

    def isSwitchValue(self, switch):
        try:
            if self.switch[switch] is not None:
                return True
            else:
                return False
        except:
            return False


@dataclass()
class HelpMenu:
    menuName: str
    commands: dict = None
    details: list = None
    helpInfo: list = None

    def makeHelpMenu(self):
        a = -1

        print('*Help Menu*')
        print(f'Welcome to the help menu for the {self.menuName} command!')
        print('Here is a list of commands you can use!\n')

        chars = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            'a',
            'b',
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        for i in self.commands:
            a += 1
            print(f'[{chars[a + 1]}] <this>.{i}: {self.details[a]}')

    def makeHelpInfo(self):
        currentIndex = -1

        print("\t*Help Menu*")
        print(f"How to use the {self.menuName} command:\n")

        print("    Switches:")
        print(f"\t-h: creates help menu for this command")
        for i in self.helpInfo:
            currentIndex += 1
            if i != "-":
                print(f"\t{i}")
            else:
                currentIndex += 1
                break

        print()

        print("    Example:")
        examples = self.helpInfo[currentIndex:]
        for i in examples:
            print(f"\texample: [{i}]")

    def run(self, interPackage):
        self.makeHelpMenu()


@dataclass()
class Dict3:
    key: list
    value: list
    value2: list

    def read(self, key):
        index = self.key.index(key)
        return self.value[index], self.value2[index]

    def append(self, key, value, value2):
        self.key.append(key)
        self.value.append(value)
        self.value2.append(value2)

    def __str__(self):
        finalDict = {}

        i = -1
        for a in self.key:
            i += 1
            value1 = self.value[i]
            value2 = self.value2[i]
            finalDict[a] = [value1, value2]

        return str(finalDict)

    def __repr__(self):
        finalDict = {}

        i = -1
        for a in self.key:
            i += 1
            value1 = self.value[i]
            value2 = self.value2[i]
            finalDict[a] = [value1, value2]

        return finalDict


def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


class Mini_Commands:
    def __init__(self, command):
        self.command = command

    def run(self, interPackage):
        if interPackage.checkSwitch("h"):
            HelpMenu(self.command, helpInfo=[
                "-",
                self.command,
                f"{self.command}: -h",
            ]).makeHelpInfo()
        else:
            if self.command == "clear":
                clear()
            elif self.command == "pause":
                if os.name == 'nt':
                    os.system("PAUSE")
                else:
                    os.system("read 'pog'")


@dataclass()
class ExterPackage:
    utils: dict
    inter: vars
    pluginList: list
    helpMenu: vars

    def runPlugins(self):
        cmd = None

        try:
            a = self.inter.cmdDir[0]
        except:
            sys.exit()

        if self.pluginList.__contains__(self.inter.cmdDir[0]):
            cmd = os.path.join(os.getcwd(), SystemConfigUtils().load("PLUGINS_LOC"), self.inter.cmdDir[0])
        if self.inter.cmdDir[0] == "help":
            self.helpMenu.run(self.inter)
        elif cmd:
            contents = convScript.openFile(cmd)
            script = convScript.from64(contents)
            exec(script, {"exterPackage": self})
        else:
            print(f'(Error) Invalid Syntax: Plugin \'{self.inter.cmdDir[0]}\' not found')
