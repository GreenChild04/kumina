from utils.cmdUtils.userKeyUtils import UserKeyUtils
from menus.productLock import ProductLock
from dataclasses import dataclass
import utils.tond.Encryption as encryption
from fun.parser.udr import UdrParser
from udr.utils.udrUtils import clear
import pickle
import base64
from pathlib import Path
import time


class UdrScript:
    def __init__(self, script):
        self.script = open(script, "r+").read().split("\n")
        self.scriptN = script
        self.uku = None

    def run(self):
        if self.script[0] == "#! /udr/script":
            self.script = self.script[1:]
            USC(self.script, self.scriptN).compile(self.scriptN)
        elif self.scriptN.split(".")[1] == "cdn":
            USC(self.script, self.scriptN).readscript()
        else:
            raise "Error Not A Script Nor Compiled"


@dataclass()
class USO:
    script: list
    user: str
    pwd: str
    act: str = None

    def runScript(self):
        start = time.time()
        print(f"[Running Script: User({self.user})]\n")
        for i in self.script:
            parser = UdrParser(i, self.user, self.pwd)
            parser.run()
        print(f"\n[Finished Script time:{time.time() - start}]")


class USC:
    def __init__(self, script, name):
        self.script = script
        self.name = name

    def compile(self, name):
        print("Enter Username and Password to Compile Script")
        user, pwd = ProductLock().userEnter()
        start = time.time()
        print("Compiling Script")
        uso = USO(self.script, user, pwd)
        pikkled = pickle.dumps(uso)
        encrypted = encryption.encryptData(pikkled, "ιɳα-udr_script", True)
        based = base64.b85encode(encrypted)

        with Path(name.split(".")[0] + ".cdn") as file:
            file.write_text(based.decode())
        print(f"Compiled! time:[{time.time() - start}]")

    def readscript(self):
        start = time.time()
        print("Reading Script")
        encrypted = base64.b85decode(Path(self.name).read_text().encode())
        pikkled = encryption.decryptData("ιɳα-udr_script", encrypted, True)
        uso = pickle.loads(pikkled)
        print(f"Finished Reading Script: time[{time.time() - start}]")
        clear()
        uso.runScript()
