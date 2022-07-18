from udr.utils.udrUtils import HelpMenu
from textgenrnn import textgenrnn


class CmdAidea:
    def __init__(self):
        self.hm = HelpMenu("aidea", helpInfo=[
            "-f: sets the filename of the ai training set",
            "-e: sets the epoch of the ai",
            "-t: sets the temperature of the ai",
            "-",
            "elite.aidea: \"filename\"",
            "elite.aidea: -f/\"filename\"",
            "elite.aidea: \"filename\" -e/\"epoch\" -t/\"temp\"",
            "elite.aidea: -f/\"filename\" -e/\"epoch\" -t/\"temp\"",
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
        temp = 0.5
        if interPackage.isSwitchValue("t"):
            temp = interPackage.getValue("t")
        if interPackage.isSwitchValue("e"):
            epoch = interPackage.getValue("e")
        ai = textgenrnn()
        print("Starting Ai Training")
        try:
            ai.train_from_file(fileLoc, num_epochs=epoch)
            ai.generate(temperature=temp)
        except Exception as error:
            print(f"Ai Training Failed: ({error})")
