from utils.cmdUtils.CommandUtils import InterPackage


class CmdAdd:
    def __init__(self):
        pass

    def run(self, interPackage):
        if interPackage.syntax:
            print(f'Ans: {self.cal(interPackage.syntax)}')
        else:
            print('Write down the numbers you want to find the sum of and separate them with a \',\'')
            inpit = input('>')
            inpit = inpit.strip(' ')
            inpit = inpit.split(',')
            print('\nAns: ' + str(self.cal(inpit)))

    def cal(self, num):
        result = None
        result = sum(self.toFloat(num))
        return result

    def toFloat(self, iList):
        result = []
        for i in iList:
            result.append(float(i))

        return result
