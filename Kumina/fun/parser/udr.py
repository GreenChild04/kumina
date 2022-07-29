from udr.utils.udrUtils import InterPackage
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from udr.utils.udrUtils import HelpMenu

from udr.commands.print import CmdPrint
from udr.commands.os import CmdOs
from udr.commands.folder.cmd_folder import CmdFolder
from udr.commands.wifi.cmd_wifi import CmdWifi
from udr.commands.system.cmd_system import CmdSystem
from udr.commands.elite.cmd_elite import CmdElite
from udr.commands.cmd_log import CmdLog
from udr.utils.udrUtils import Mini_Commands


##########################
# Run
##########################

class UdrParser:
    def __init__(self, text, user, pwd):
        self.text = text
        self.user = user
        self.pwd = pwd

    def run(self):
        tokens, error = Lexer(self.text).run()
        if error:
            print(error.asString())
        if Interpreter(tokens).checkToken(TT_UDR, tokens):
            return False
        inter = Interpreter(tokens).run()

        cmdList = {
            "print": CmdPrint(),
            "os": CmdOs(),
            "file": CmdFolder(),
            "wifi": CmdWifi(),
            "system": CmdSystem(),
            "elite": CmdElite(),
            "log": CmdLog(),
            "clear": Mini_Commands("clear"),
            "pause": Mini_Commands("pause"),
        }

        details = [
            "Used to print a specified message",
            "Used to run specified commands in os terminal",
            "Used to run all utilizes concerning files",
            "Used to run wifi based commands (highly experimental)",
            "Used to run all system commands",
            "Used to run commands made for Elite80",
            "Used to write log entries",
            "Clears the screen",
            "Pauses the program",
        ]

        self.helpMenu(cmdList, details)

        interPackage = InterPackage(cmdList, inter[0], self.user, inter[3], inter[1], inter[2], pwd=self.pwd)
        interPackage.runCommands()

        return True

    def helpMenu(self, cmdList, details):
        cmdList["help"] = HelpMenu(SystemConfigUtils().load("CMD_NAME"), cmdList, details)
        details.append(f"Used to create a help menu for {SystemConfigUtils().load('CMD_NAME')}")


##########################
# Interpreter
##########################
class Interpreter:
    def __init__(self, tokenList):
        self.tokenList = tokenList

    def getTokenType(self, token):
        return token.asType()

    def getTokenValue(self, token):
        return token.asValue()

    def checkToken(self, token, tokenList):
        for i in tokenList:
            if self.getTokenType(i) == token:
                return True

        return False

    def run(self):
        if self.checkToken(TT_COL, self.tokenList):
            colonSides = self.colonParser()
            finalCmdDir = self.dotParser(colonSides[0])

            inpit = self.findSeparateInput(colonSides)
            switches = self.findSwitches(colonSides)
            isColon = True

        else:
            finalCmdDir = self.dotParser(self.tokenList)
            inpit = None
            switches = None
            isColon = False

        return finalCmdDir, inpit, switches, isColon

    def colonParser(self):
        activeTokens = self.tokenSplit(TT_COL, self.tokenList)
        return activeTokens

    def findSeparateInput(self, colonSides):
        output = []

        for i in colonSides[1]:

            if self.getTokenType(i) in [TT_FUN, TT_FLOAT, TT_INT, TT_STR]:
                output.append(self.getTokenValue(i))

            typeMemory = self.getTokenType(i)

        return output

    def findSwitches(self, colonSides):
        output = []
        dic = {}
        for i in colonSides[1]:
            if self.getTokenType(i) == TT_SCH:
                output.append(self.getTokenValue(i))

        for i in output:
            dic[i[0]] = i[1]
        return dic

    def dotParser(self, tokenList):
        activeTokens = self.tokenSplit(TT_DOT, tokenList)
        output = []

        for i in activeTokens:
            for a in i:
                output.append(self.getTokenValue(a))

        return output

    def tokenSplit(self, token, tokenList):
        result = []
        current_set = []
        for item in tokenList:
            if self.getTokenType(item) is token:
                result.append(current_set)
                current_set = []
            else:
                current_set.append(item)
        result.append(current_set)
        return result


##########################
# Lexer
##########################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.currentChar = None
        self.pos = -1

    def run(self):
        self.advance()
        tokenList, error = self.makeTokens()
        return tokenList, error

    def advance(self):
        self.pos += 1
        self.currentChar = self.text[self.pos] if self.pos < len(self.text) else None

    def makeTokens(self):
        tokens = []

        while self.currentChar is not None:
            if self.currentChar in ' <>\t':
                self.advance()
            elif self.currentChar in DIGITS:
                tokens.append(self.makeNumbers())
            elif self.currentChar in CHARACTERS:
                tokens.append(self.makeCharacters())
            elif self.currentChar == "-":
                tokens.append(self.makeSwitch())
            elif self.currentChar == '"' or self.currentChar == "'":
                tokens.append(self.makeText())
            elif self.currentChar == ':' or self.currentChar == ";":
                tokens.append(Token(TT_COL))
                self.advance()
            elif self.currentChar == '#' or self.currentChar == ">":
                tokens.append(Token(TT_UDR))
                self.advance()
            elif self.currentChar == '.':
                tokens.append(Token(TT_DOT))
                self.advance()
            else:
                char = self.currentChar
                self.advance()
                return [], IllegalCharError(f"'{char}'")

        return tokens, None

    def makeNumbers(self):
        numStr = ''
        dot_count = 0

        while self.currentChar is not None and self.currentChar in DIGITS + '.':
            if self.currentChar == '.':
                if dot_count == 1: break
                dot_count += 1
                numStr += '.'
            else:
                numStr += self.currentChar
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(numStr))
        else:
            return Token(TT_FLOAT, float(numStr))

    def makeCharacters(self):
        charStr = ''

        while self.currentChar is not None and self.currentChar in CHARACTERS:
            charStr += self.currentChar
            self.advance()
        return Token(TT_FUN, charStr)

    def makeText(self):
        charText = ''

        self.advance()

        while self.currentChar is not None and self.currentChar != '"':
            charText += self.currentChar
            self.advance()
        self.advance()
        return Token(TT_STR, charText)

    def makeSwitch(self):
        switchVal = [None, None]

        self.advance()

        if self.currentChar == "-":
            self.advance()
            switchVal[0] = self.makeCharacters().asValue()
        else:
            switchVal[0] = self.currentChar
            self.advance()

        if self.currentChar == "/":
            self.advance()
            if self.currentChar == '"':
                switchVal[1] = self.makeText().asValue()
            elif self.currentChar in CHARACTERS:
                switchVal[1] = self.makeCharacters().asValue()
            elif self.currentChar in DIGITS:
                switchVal[1] = self.makeNumbers().asValue()
            else:
                "Error: That is not a friggin input char"

        return Token(TT_SCH, switchVal)


##########################
# Tokens
##########################

TT_COL = 'COL'
TT_DOT = 'DOT'
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_FUN = 'FUN'
TT_STR = "STR"
TT_UDR = "UDR"
TT_SCH = "SCH"


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def asString(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

    def asValue(self):
        return self.value

    def asType(self):
        return self.type


##########################
# CONSTANTS
##########################

DIGITS = '0123456789'

CHARACTERS = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM_'


##########################
# ERRORS
##########################

class Error:
    def __init__(self, errorName, details):
        self.errorName = errorName
        self.details = details
        self.asString()

    def asString(self):
        return f'(Error) {self.errorName}: {self.details}'


class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Unexpected Character', details)


class InvalidSyntaxError(Error):
    def __init__(self, details):
        super().__init__('Invalid Syntax', details)
