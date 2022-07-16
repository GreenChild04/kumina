from commands.vex.code.cmd_code import CmdCode
from utils.cmdUtils.CommandUtils import HelpMenu


class CmdVex:
    def __init__(self):
        self.cmdList = {
            "help": VexHelp(),
            "code": CmdCode(),
        }

        self.details = [
            "Used to generate a help menu for the Vex command",
            "Used to access the Code commands of the Vex package",
        ]

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            VexHelp().run(interPackage)


class VexHelp:
    def run(self, interPackage):
        HelpMenu('vex', CmdVex().cmdList, CmdVex().details).makeHelpMenu()
