from utils.cmdUtils.CommandUtils import HelpMenu
from commands.wifi.cmd_wifiCrack import CmdCrack


class CmdWifi:
    def __init__(self):
        self.cmdList = {
            "help": WifiHelp(),
            "crack": CmdCrack(),
            "check": CmdCheck(),
        }

        self.details = [
            "Used to create a help menu for the Wifi command",
            "Used to run the wifi cracking software",
            "Used to check the available connections",
        ]

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            self.cmdList["help"].run(interPackage)


class CmdCheck:
    def __init__(self):
        self.sub = __import__("subprocess")

    def run(self, interPackage):
        nts = self.sub.check_output(["netsh", "wlan", "show", "network"])
        dnts = nts.decode("ascii")
        print("dnts")


class WifiHelp:
    def run(self, interPackage):
        HelpMenu("Wifi", CmdWifi().cmdList, CmdWifi().details).makeHelpMenu()
