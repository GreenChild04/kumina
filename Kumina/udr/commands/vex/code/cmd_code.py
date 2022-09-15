from utils.cmdUtils.CommandUtils import HelpMenu
from commands.vex.code.cmd_saveLoad import CmdLoad
from commands.vex.code.cmd_saveLoad import CmdSave


class CmdCode:
    def __init__(self):
        self.cmdList = {
            "help": CodeHelp(),
            "load": CmdLoad(),
            "save": CmdSave(),
        }

        self.details = [
            "Used to create a help menu for Code command",
            "Used to load python files from vex files",
            "Used to save python files to vex files",
        ]

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            CodeHelp().run(interPackage)



class CodeHelp:
    def run(self, interPackage):
        HelpMenu('code', CmdCode().cmdList, CmdCode().details).makeHelpMenu()
