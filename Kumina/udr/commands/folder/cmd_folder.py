from utils.cmdUtils.CommandUtils import InterPackage
from udr.utils.udrUtils import HelpMenu
from udr.commands.folder.cmd_storeLoad import CmdStore
from udr.commands.folder.cmd_storeLoad import CmdLoad
from udr.commands.folder.cmd_storeLoad import CmdCheck
from udr.commands.folder.cmd_storeLoad import CmdRemove
from udr.commands.folder.cmd_storeLoad import CmdEject
from udr.commands.folder.cmd_storeLoad import CmdInject
from udr.commands.folder.cmd_storeLoad import CmdOpen


class CmdFolder:
    def __init__(self):
        self.cmdList = {
            "help": FolderHelp(),
            "save": CmdStore(),
            "load": CmdLoad(),
            "list": CmdCheck(),
            "remove": CmdRemove(),
            "eject": CmdEject(),
            "inject": CmdInject(),
            "open": CmdOpen(),
        }

        self.details = [
            "Creates help menu for the folder command",
            "Used to store files into the system",
            "Used to load filed from the system",
            "Used to check all the file names",
            "Used to remove stored files",
            "Used to eject the encrypted file for later usage",
            "Used to inject encrypted file data for usage",
            "Used to open the directory",
        ]

        self.hm = HelpMenu("file", {}, [], [
            "-",
            "file",
            "file: -h",
        ])

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            if interPackage.isColon and interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                FolderHelp().run(interPackage)


class FolderHelp:
    def run(self, interPackage):
        HelpMenu('folder', CmdFolder().cmdList, CmdFolder().details).makeHelpMenu()
