from udr.utils.udrUtils import HelpMenu


class CmdPrint:
    def __init__(self):
        self.hm = HelpMenu("print", {}, [], [
            "-t: used to input data to print",
            "-",
            "print: \"stuff you want to print\"",
            "print: -t/\"stuff you want to print\"",
            "print: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h") or interPackage.checkSwitch("help"):
                self.hm.makeHelpInfo()
            else:
                print(interPackage.getValue("t", 0))
        else:
            self.hm.makeHelpInfo()
