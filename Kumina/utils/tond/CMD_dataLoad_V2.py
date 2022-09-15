from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import os
import utils.tond.dataUtils


class COMMAND_DATALOAD_V2:
    def __init__(self):
        self.dataUtils = utils.tond.dataUtils.DATA_UTILS()

    def runDataLoad(self, loc, cellLoc, fileName):
        loc = loc

        if os.path.exists(fileName):
            wb = load_workbook(fileName)

        sheet = wb.active

        cell = sheet[cellLoc]
        cellValue = self.dataUtils.loadFromJsonString(loc, cell.value)

        return cellValue
