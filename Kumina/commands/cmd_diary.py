import os
import sys
from datetime import datetime, date
from pathlib import Path
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils


class CmdDiary:
    def __init__(self):
        self.entry = ''
        self.finalText = ''

    def run(self, interPackage):
        os.system("cls")
        inpit = ""
        while True:

            if os.path.exists(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC"))):
                inpit = FileRead().loadTemp()

            inpit = input(inpit)
            self.mainFun(inpit)
            os.system("cls")

    def mainFun(self, entry):
        self.entry = entry

        if self.entry.__contains__("~"):
            self.entry.strip("~")
            if FileRead().checkFile():
                self.old()
            else:
                self.new()
            os.remove(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC"), '_temp_'))
            self.entry = ''
            self.finalText = ''
        else:
            self.conJ()

    def new(self):
        self.addLine(self.getDay())
        self.addLine("")
        self.addLine("-\n" + self.getTime() + "\n")
        self.addLine(FileRead().loadTemp())
        self.addLine("-\n")

        FileRead().writeOnFile(self.finalText)

    def old(self):
        self.addLine("-\n" + self.getTime() + "\n")
        self.addLine(FileRead().loadTemp())
        self.addLine("-\n")

        FileRead().writeOnFile(self.finalText)
        self.finalText = ""

    def save(self):
        pass

    def conJ(self):
        current = FileRead().loadTemp() + self.entry.replace('`', '\n')
        FileRead().storeTemp(current)

    def addLine(self, line):
        self.finalText += line + "\n"

    def getTime(self):
        pass

    def getDay(self):
        days = [
            None,
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        time = datetime.today()

        return time.strftime("%d/%m/%Y") + " - " + days[time.isoweekday()]

    def getTime(self):
        time = datetime.now().strftime("%I:%M")
        pmam = datetime.now().strftime("%p")

        return time + pmam.lower()


class FileRead:
    def __init__(self):
        self.fileLoc = os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC"), f"{TimeDate().asIndex()}; {f'{TimeDate().day} {TimeDate().month} {TimeDate().year}'} - {TimeDate().asDay()}.log")

    def checkFile(self):
        return os.path.isfile(self.fileLoc)

    def writeOnFile(self, data):
        if not os.path.exists(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC"))):
            os.makedirs(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC")))

        if os.path.exists(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC"))):
            inpit = FileRead().loadTemp()

        if self.checkFile():
            with open(self.fileLoc, "a") as file:
                file.write(data)
        else:
            with open(self.fileLoc, "w+") as file:
                file.write(data)

    def storeTemp(self, data):

        if not os.path.exists(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC"))):
            os.makedirs(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC")))

        with open(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC"), '_temp_'), 'w') as file:
            file.write(data)

    def loadTemp(self):
        try:
            with Path(os.path.join(os.getcwd(), SystemConfigUtils().load("DIARY_LOC"), '_temp_')) as file:
                return file.read_text()
        except:
            return ''


class TimeDate:
    def __init__(self):
        self.time = datetime.today()

        self.day = self.time.strftime("%d")
        self.month = self.time.strftime("%m")
        self.year = self.time.strftime("%Y")

    def asDate(self):
        return f"{self.day}-{self.month}-{self.year}"

    def asIndex(self):
        d0 = date(day=int(self.day), month=int(self.month), year=int(self.year))
        d1 = date(2020, 1, 1)

        delta = d0 - d1

        return delta.days

    def asDay(self):
        time = self.time.isoweekday()

        days = [
            None,
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        return days[time]

