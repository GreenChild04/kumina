from udr.utils.udrUtils import HelpMenu
import os


class CmdOs:
    def __init__(self):
        self.hm = HelpMenu("os", {}, [], [
            "-h: creates help menu",
            "-",
            "os: \"commands you want to run\"",
            "os: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h") or interPackage.checkSwitch("help"):
                self.hm.makeHelpInfo()
            try:
                for i in interPackage.inpit:
                    os.system(i)
            except:
                print("Execution Failed")
        else:
            self.hm.makeHelpInfo()
