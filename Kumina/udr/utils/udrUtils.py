import sys
from dataclasses import dataclass
import os
import subprocess


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

        for i in self.commands:
            a += 1
            print(f'{a + 1}. <this>.{i}: {self.details[a]}')

    def makeHelpInfo(self):
        currentIndex = -1

        print("\t*Help Menu*")
        print(f"How to use the {self.menuName} command:\n")

        print("    Switches:")
        print(f"\t-h & --help: creates help menu for this command")
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
    try:
        out = subprocess.check_output("cls")
        if subprocess.check_output("cls") != "":
            os.system("clear")
    except:
        os.system("clear")
