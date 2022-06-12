from utils.tond.CMD_dataSave_V2 import COMMAND_DATASAVE_V2
from utils.tond.CMD_dataLoad_V2 import COMMAND_DATALOAD_V2


class DATA:
    def __init__(self, fileName):
        self.dataSave = COMMAND_DATASAVE_V2()
        self.dataLoad = COMMAND_DATALOAD_V2()
        self.fileName = fileName

    def save(self, loc, data, cellLoc):
        self.dataSave.runDataSave(loc, data, cellLoc, self.fileName)

    def load(self, loc, cellLoc):
        return self.dataLoad.runDataLoad(loc, cellLoc, self.fileName)
