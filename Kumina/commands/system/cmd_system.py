from utils.cmdUtils.CommandUtils import InterPackage
from utils.cmdUtils.CommandUtils import HelpMenu
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
import utils.tond.Encryption as encryption
import json


class CmdSystem:
    def __init__(self):
        self.cmdList = {
            "help": SystemHelp(),
            "reset": SystemReset(),
            "edit": SystemEdit(),
            "list": SystemList(),
        }

        self.details = [
            "Creates help menu for the system command",
            "Used to reset the system configurations",
            "Used to edit the system configurations",
            "Used to list the system configurations",
        ]

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            SystemHelp().run(interPackage)


class SystemHelp:
    def run(self, interPackage):
        HelpMenu('system', CmdSystem().cmdList, CmdSystem().details).makeHelpMenu()


class SystemReset:
    def run(self, interPackage):
        print("Resetting System...")
        SystemConfigUtils().runSystemPresets()
        print("Done!")


class SystemEdit:
    def run(self, interPackage):
        if interPackage.syntax:
            print(f"Editing the ({interPackage.syntax[0]}) Config...")
            self.edit(interPackage.syntax)
            print("Done!")
        else:
            print("Write down the location and value you want to edit and separate them with a ','")
            inpit = input(">")
            inpit = inpit.split(",")
            print(f"Editing the ({inpit[0]}) Config...")
            self.edit(inpit)
            print("Done!")

    def edit(self, inputList):
        SystemConfigUtils().save(inputList[1], inputList[0])


class SystemList:
    def run(self, interPackage):
        with open(SystemConfigUtils().fileName, 'r+') as file:
            decrypt = encryption.decryptData(SystemConfigUtils().systemPresets["CRYPT_PASS"], file.readlines(0)[0])
            data = json.loads(decrypt)

        count = 0
        for i in dict(data):
            count += 1
            print(f"{count}.{i}:{dict(data)[i]}")
