from utils.tond.data import DATA as SaveLoad
from utils.tond.dataUtils import DATA_UTILS


class MenuUtils:
    def __init__(self):
        self.dataUtils = DATA_UTILS()
        self.tempStore = SaveLoad('temp.xlsx')
