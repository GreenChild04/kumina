import base64
import time
from pathlib import Path
from udr.utils.udrUtils import HelpMenu
import utils.tond.Encryption as encryption
import pickle


class CmdScript:
    def __init__(self):
        self.hm = HelpMenu("script", helpInfo=[
            "-d: used to decompile the file",
            "-",
            "script: \"file_you_want_to_run.dn\"",
            "script: -d \"file_you_want_to_decompile.cdn\"",
            "script: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                if interPackage.checkSwitch("d"):
                    self.decompile(interPackage)
                else:
                    self.runScript(interPackage)
        else:
            self.hm.makeHelpInfo()

    def decompile(self, interPackage):
        start = time.time()
        print("Decompiling Script")
        encrypted = base64.b85decode(Path(interPackage.inpit[0]).read_text().encode())
        pikkled = encryption.decryptData("ιɳα-udr_script", encrypted, True)
        uso = pickle.loads(pikkled)
        with open(f"{interPackage.inpit[0].split('.')[0]}.dn", "a+") as file:
            file.write("#! /udr/script\n")
            for i in uso.script:
                file.write(i + "\n")
        print(f"Finished Decompiling Script: time[{time.time() - start}]")

    def runScript(self, interPackage):
        from udr.udrScript import UdrScript
        UdrScript(interPackage.inpit[0]).run()
