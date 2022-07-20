from udr.utils.udrUtils import HelpMenu
from textgenrnn import textgenrnn
import pickle
from pathlib import Path


class CmdAidea:
    def __init__(self):
        self.hm = HelpMenu("aidea", helpInfo=[
            "-f: sets the filename of the ai training set",
            "-e: sets the epoch of the ai",
            "-t: sets the temperature of the ai",
            "-o: sets the output file",
            "-n: sets the number of outputs",
            "-p: sets if the isPickle switch",
            "-",
            "elite.aidea: \"filename\"",
            "elite.aidea: -f/\"filename\"",
            "elite.aidea: \"filename\" -e/epoch -t/temp -o/\"output\"",
            "elite.aidea: -f/\"filename\" -e/epoch -t/temp -o/\"output\"",
            "elite.aidea: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                self.runAi(interPackage)
        else:
            self.hm.makeHelpInfo()

    def runAi(self, interPackage):
        fileLoc = interPackage.getValue("f")
        epoch = 50
        newfile = f"{fileLoc}.out"
        temp = 0.5
        num = 1
        ai = None
        isPickle = interPackage.checkSwitch("p")
        if interPackage.isSwitchValue("t"):
            temp = interPackage.getValue("t")
        if interPackage.isSwitchValue("e"):
            epoch = interPackage.getValue("e")
        if interPackage.isSwitchValue("o"):
            newfile = interPackage.getValue("o")
        if interPackage.isSwitchValue("n"):
            num = interPackage.getValue("n")
        try:
            ai = textgenrnn()
            ai.load("__AI__.ina")
        except:
            ai = textgenrnn()
            print("Starting Ai Training")
            try:
                ai.train_from_file(fileLoc, num_epochs=epoch)
                if isPickle:
                    ai.save("__AI__.ina")
                print("Ai Training Done!")
            except Exception as error:
                print(f"Ai Training Failed: ({error})")
        if not isPickle:
            print("\nOutputting Ai Generation")
            try:
                ai.generate_to_file(newfile, temperature=temp, n=num)
                print("Outputting Done")
            except Exception as error:
                print(f"Ai outputting failed: [{error}]")
