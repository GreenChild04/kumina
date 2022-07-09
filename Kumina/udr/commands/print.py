from udr.utils.udrUtils import HelpMenu


class CmdPrint:
    def __init__(self):
        self.hm = HelpMenu("print", {}, [], [
            "-h: creates help menu",
            "-",
            "print: \"stuff you want to print\""
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h") or interPackage.checkSwitch("help"):
                self.hm.makeHelpInfo()
            try:
                for i in interPackage.inpit:
                    print(i)
            except:
                print(None)
        else:
            self.hm.makeHelpInfo()
