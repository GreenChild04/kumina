from udr.utils.udrUtils import HelpMenu
#from udr.commands.elite.cmdaidea import CmdAidea


class CmdElite:
    def __init__(self):
        self.hm = HelpMenu("elite", helpInfo=[
            "-",
            "elite",
            "elite: -h",
        ])
        self.cmdList = {
            "help": EliteHelp(),
            #"aidea": CmdAidea(),
        }
        self.details = [
            "Used to create a help menu for the elite command",
            #"Used to make youtube ideas using an ai"
        ]

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            if interPackage.isColon and interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                EliteHelp().run(interPackage)


class EliteHelp:
    def run(self, interPackage):
        HelpMenu("elite", CmdElite().cmdList, CmdElite().details).makeHelpMenu()
