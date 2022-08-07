from dataclasses import dataclass
from udr.utils.udrUtils import InterPackage
import os
from udr.utils.udrUtils import ExterPackage
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from utils.cmdUtils.userKeyUtils import UserKeyUtils


@dataclass()
class HelpMenu:
    menuName: str
    commands: list = None
    helpInfo: list = None

    def makeHelpMenu(self):
        a = -1

        print('*Help Menu*')
        print(f'Welcome to the help menu for the {self.menuName} command!')
        print('Here is a list of commands you can use!\n')

        chars = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            'a',
            'b',
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        for i in self.commands:
            a += 1
            print(f'[{chars[a + 1]}] plugin.{i}')

    def makeHelpInfo(self):
        currentIndex = -1

        print("\t*Help Menu*")
        print(f"How to use the {self.menuName} command:\n")

        print("    Switches:")
        print(f"\t-h: creates help menu for this command")
        for i in self.helpInfo:
            currentIndex += 1
            if i != "-":
                print(f"\t{i}")
            else:
                currentIndex += 1
                break

        print()

        print("    Example:")
        examples = self.helpInfo[currentIndex:]
        for i in examples:
            print(f"\texample: [{i}]")

    def run(self, interPackage):
        self.makeHelpMenu()


class Plugin:
    def __init__(self):
        try:
            os.makedirs(SystemConfigUtils().load("PLUGINS_LOC"))
        except:
            pass
        self.contents = os.listdir(SystemConfigUtils().load("PLUGINS_LOC"))
        self.exterPackage = ExterPackage({}, [], "", [])
        self.hm = HelpMenu("plugin", helpInfo=[
            "-",
            "plugin",
            "plugin: -h",
        ])

    def run(self, interPackage):
        self.exterPackage = ExterPackage({
            "system": SystemConfigUtils(),
            "userKey": UserKeyUtils(interPackage.user),
        }, interPackage, self.contents, PluginHelp())
        if len(interPackage.cmdDir) > 0:
            self.exterPackage.runPlugins()
        else:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                PluginHelp().run(interPackage)


class PluginHelp:
    def run(self, interPackage):
        con = Plugin().contents
        con.append("help")
        HelpMenu("plugin", con).makeHelpMenu()
