import shutil
import convScript
from pathlib import Path
import os
from importlib import import_module
from dataclasses import dataclass


class Excutor:
    def __init__(self):
        self.testImp = None
        self.testFun = None

    def run(self):
        self.getImport()
        shutil.rmtree("tmp")

    def getImport(self):
        loc = "scripta"
        path = os.path.join("tmp", loc)
        contents = convScript.openFile(loc)
        script = convScript.from64(contents)

        os.makedirs("tmp")

        exec(script, {"bob": Uwu("hello my name is Ethan Ma")})


@dataclass()
class Uwu:
    data: str


if __name__ == "__main__":
    Excutor().run()
