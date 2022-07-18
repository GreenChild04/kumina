from utils.cmdUtils.CommandUtils import InterPackage
from udr.utils.udrUtils import HelpMenu
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

        self.hm = HelpMenu("system", helpInfo=[
            "-",
            "system",
            "system: -h",
        ])

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                SystemHelp().run(interPackage)


class SystemHelp:
    def run(self, interPackage):
        HelpMenu('system', CmdSystem().cmdList, CmdSystem().details).makeHelpMenu()


class SystemReset:
    def run(self, interPackage):
        hm = HelpMenu("reset", helpInfo=[
            "-",
            "system.reset",
            "system.reset: -h",
        ])

        if interPackage.checkSwitch("h"):
            hm.makeHelpInfo()
        else:
            print("Resetting System...")
            SystemConfigUtils().runSystemPresets()
            print("Done!")



class SystemEdit:
    def run(self, interPackage):
        hm = HelpMenu("edit", helpInfo=[
            "-s: sets the setting you want to change",
            "-v: sets the new value you want to set the setting to",
            "-",
            "system.edit: \"name of setting\" \"new value\"",
            "system.edit: -s/\"name of setting\" -v/\"new value\"",
            "system.edit: -h",
        ])
        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                hm.makeHelpInfo()
            else:
                print(f"Editing the ({interPackage.getValue('s')}) Config...")
                self.edit(interPackage.getValue("s"), interPackage.getValue("v", 1))
                print("Done!")

    def edit(self, type, value):
        SystemConfigUtils().save(value, type)


class SystemList:
    def run(self, interPackage):
        hm = HelpMenu("list", helpInfo=[
            "-",
            "system.list",
            "system.list: -h",
        ])
        if interPackage.checkSwitch("h"):
            hm.makeHelpInfo()
        else:
            with open(SystemConfigUtils().fileName, 'r+') as file:
                decrypt = encryption.decryptData(SystemConfigUtils().systemPresets["CRYPT_PASS"], file.readlines(0)[0])
                data = json.loads(decrypt)

            count = 0
            for i in dict(data):
                count += 1
                print(f"{count}.{i}:{dict(data)[i]}")
