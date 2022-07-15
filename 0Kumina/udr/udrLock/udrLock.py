import base64
from random import randint
from pathlib import Path
import utils.tond.Encryption as encryption
from utils.cmdUtils.userKeyUtils import UserKeyUtils


class UdrLock:
    def createActCode(self):
        long = self.genActivation()
        encrypted = encryption.encryptData(long, "ina")
        b64 = self.to64(encrypted)
        return b64

    def isActRight(self, act):
        try:
            b64 = self.from64(act)
            encrypt = encryption.decryptData("ina", b64)
            return True
        except:
            return False

    def oldConvert(self, user):
        item = self.createActCode()
        UserKeyUtils(user).save(item, "INA")

    def to64(self, contents):
        b64 = base64.b85encode(contents)
        return b64.decode()

    def from64(self, contents):
        normal = base64.b85decode(contents.encode())
        return normal

    def genActivation(self):
        lettus = [
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z',
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z',
            '_',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '0',
            '!',
            '@',
            '#',
            '$',
            '%',
            '^',
            '&',
            '*',
            '(',
            ')',
            '{',
            '}',
            '[',
            ']',
            '"',
            '\'',
            '/',
            '\\',
            ',',
            '.',
            '~',
            ':',
        ]

        e = ''

        for i in range(128):
            e += lettus[randint(0, len(lettus) - 1)]

        return e


if __name__ == "__main__":
    with Path("activation.iac") as file:
        #code = UdrLock().createActCode()
        #file.write_text(code)
        #print(code)
        print(UdrLock().isActRight(file.read_text()))
