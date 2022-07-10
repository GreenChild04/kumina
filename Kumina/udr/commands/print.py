from udr.utils.udrUtils import HelpMenu


class CmdPrint:
    def __init__(self):
        self.hm = HelpMenu("print", {}, [], [
            "-",
            "print: \"stuff you want to print\"",
            "print: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h") or interPackage.checkSwitch("help"):
                self.hm.makeHelpInfo()
            else:
                for i in interPackage.inpit:
                    print(i)
        else:
            self.hm.makeHelpInfo()
