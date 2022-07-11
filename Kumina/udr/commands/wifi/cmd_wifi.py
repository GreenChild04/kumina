import time
from udr.utils.udrUtils import HelpMenu
from commands.wifi.cmd_wifiCrack import CmdCrack


class CmdWifi:
    def __init__(self):
        self.cmdList = {
            "help": WifiHelp(),
            "crack": CmdCrack(),
            "check": CmdCheck(),
            "connect": CmdConnect(),
        }

        self.details = [
            "Used to create a help menu for the Wifi command",
            "Used to run the wifi cracking software",
            "Used to check the available connections",
            "Used to connect to a wifi connection",
        ]

        self.hm = HelpMenu("wifi", helpInfo=[
            "-",
            "wifi",
            "wifi: -h"
        ])

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            if interPackage.isColon and interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                self.cmdList["help"].run(interPackage)


class CmdCheck:
    def __init__(self):
        self.sub = __import__("subprocess")
        self.hm = HelpMenu("check", helpInfo=[
            "-",
            "wifi.check",
            "wifi.check: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
        else:
            nts = self.sub.check_output(["netsh", "wlan", "show", "network"])
            dnts = nts.decode("ascii")
            print(dnts)


class CmdConnect:
    def __init__(self):
        self.url = __import__("urllib")

    def run(self, interPackage):
        if interPackage.syntax:
            ispwd = None
            try:
                lel = interPackage.syntax[1]
                ispwd = True
            except:
                ispwd = False
            if ispwd:
                self.connect(interPackage.syntax[0], interPackage.syntax[1])
            else:
                self.connect(interPackage.syntax[0])
        else:
            pass

    def connect(self, ssid, pwd=None):
        try:
            self.wifi.WinWiFi.add_profile(ssid)
        except: print("Alert: Could not create wifi profile")
        if pwd:
            try:
                self.wifi.WinWiFi.connect(ssid, pwd)
                print(f"Success: Connected to {ssid} network" if self.checkCon() else "Error: Could not connect to wifi")
            except: print("Error: Wifi SSID is not found")
        else:
            try:
                self.wifi.WinWiFi.connect(ssid)
                print(f"Success: Connected to {ssid} network" if self.checkCon() else "Error: Could not connect to wifi")
            except: print("Error: Wifi SSID is not found")

    def checkCon(self):
        host = "http://google.com"
        try:
            self.url.request.urlopen(host)
            return True
        except:
            return False


class WifiHelp:
    def run(self, interPackage):
        HelpMenu("Wifi", CmdWifi().cmdList, CmdWifi().details).makeHelpMenu()
