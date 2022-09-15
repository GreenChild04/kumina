from udr.utils.udrUtils import HelpMenu
import os


class CmdOs:
    def __init__(self):
        self.hm = HelpMenu("os", {}, [], [
            "-c: sets the command you want to run",
            "-",
            "os: \"commands you want to run\"",
            "os: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h") or interPackage.checkSwitch("help"):
                self.hm.makeHelpInfo()
            try:
                os.system(interPackage.getValue("c", 0))
            except:
                print("Execution Failed")
        else:
            self.hm.makeHelpInfo()
