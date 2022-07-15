from utils.cmdUtils.stonksUtils import StonksUtils
from pathlib import Path


class CmdStonks:
    def __init__(self):
        self.su = StonksUtils()

    def run(self, interPackage):
        self.su.getData("AU", "tesla")
