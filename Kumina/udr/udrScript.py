from utils.cmdUtils.userKeyUtils import UserKeyUtils
from dataclasses import dataclass


class UdrScript:
    def __init__(self, script):
        self.script = open(script, "r+").read().split("\n")
        self.uku = None

    def run(self):
        if self.script[0] == "#! /udr/script":
            self.script = self.script[1:]
            for i in self.script:
                print(i)
        else:
            pass


dataclass()
class USO:
    script: list
    user: str
    pwd: str
    act: str = None

    def createAct(self):
        pass


class USC:
    def __init__(self, script):
        pass
