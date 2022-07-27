from utils.cmdUtils.userKeyUtils import UserKeyUtils
from menus.productLock import ProductLock
from dataclasses import dataclass
import pickle


class UdrScript:
    def __init__(self, script):
        self.script = open(script, "r+").read().split("\n")
        self.uku = None

    def run(self):
        if self.script[0] == "#! /udr/script":
            self.script = self.script[1:]
            USC(self.script)
        else:
            pass


@dataclass()
class USO:
    script: list
    user: str
    pwd: str
    act: str = None

    def runScript(self):
        pass


class USC:
    def __init__(self, script):
        self.script = script

    def compile(self):
        uso = USO(self.script, )