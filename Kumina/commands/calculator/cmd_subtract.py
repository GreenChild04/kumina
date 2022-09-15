from utils.cmdUtils.CommandUtils import InterPackage


class CmdSubtract:
    def __init__(self):
        pass

    def run(self, interPackage):
        if interPackage.syntax:
            print(f'Ans: {self.cal(interPackage.syntax)}')
        else:
            print('Write down the numbers you want to find the subtracted total of and separate them with a \',\'')
            inpit = input('>')
            inpit = inpit.strip(' ')
            inpit = inpit.split(',')
            print('\nAns: ' + str(self.cal(inpit)))

    def cal(self, num):
        result = float(num[0]) * 2

        for i in num:
            result -= float(i)

        return result
