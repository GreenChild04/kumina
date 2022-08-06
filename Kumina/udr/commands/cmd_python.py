from udr.utils.udrUtils import HelpMenu
from pathlib import Path


class CmdPython:
    def __init__(self):
        self.hm = HelpMenu("python", helpInfo=[
            "-f: sets if it is a file you want to execute",
            "-",
            "python: \"python command you want to run\"",
            "python: -f \"name of the python file you want to run\"",
            "python: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                if interPackage.checkSwitch("f"):
                    with Path(interPackage.inpit[0]) as file:
                        exec(file.read_text())
                else:
                    exec(interPackage.inpit[0])
        else:
            self.hm.makeHelpInfo()
