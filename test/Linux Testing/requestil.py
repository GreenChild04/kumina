from dataclasses import dataclass
from multiprocessing import Process, Queue


@dataclass()
class RequestPackage:
    origin: vars
    target: vars
    interPackage: vars
    pipe: vars = None
    process: vars = None

    def start(self):
        self.pipe = Queue()
        self.process = Process(target=self.target.run, args=(self.interPackage, self))
        self.process.start()

    def askCmd(self, cmd):
        return globals()[cmd]()

    def test(self):
        return self.origin.testdata()

    def request___(self):
        pass
