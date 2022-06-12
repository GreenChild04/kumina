import shutil
from multiprocessing import Process, Queue, Pipe
import convScript
from pathlib import Path
import os
from importlib import import_module
from requestil import RequestPackage


class Excutor:
    def __init__(self):
        self.testImp = None
        self.testFun = None

    def run(self):
        self.getImport()
        req = RequestPackage(self, self.testImp.TestScript(), None)
        req.start()
        shutil.rmtree("tmp")

    def getImport(self):
        loc = "scripta"
        path = os.path.join("tmp", loc)
        contents = convScript.openFile(loc)
        script = convScript.from64(contents)

        os.makedirs("tmp")

        with Path(path + ".py") as file:
            file.write_text(script)

        self.testImp = import_module("tmp.scripta")
        self.testFun = self.testImp.TestScript().run

    def testdata(self):
        return "uwu"


Excutor().run()
