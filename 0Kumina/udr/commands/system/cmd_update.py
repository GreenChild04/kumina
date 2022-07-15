from utils.cmdUtils.CommandUtils import InterPackage
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils


class CmdUpdate:
    def __init__(self):
        self.scu = SystemConfigUtils()
        self.currentVersion = self.scu.load("CMD_VERSION")

    def flipper(self):
        pass
