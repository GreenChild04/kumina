from utils.cmdUtils.CommandUtils import InterPackage


class CmdMultiply:
    def __init__(self):
        pass

    def run(self, interPackage):
        if interPackage.syntax:
            print(f'Ans: {self.cal(interPackage.syntax)}')
        else:
            print('Write down the numbers you want to find the multiplied total of and separate them with a \',\'')
            inpit = input('>')
            inpit = inpit.strip(' ')
            inpit = inpit.split(',')
            print('\nAns: ' + str(self.cal(inpit)))

    def cal(self, num):
        result = 1

        for i in num:
            result *= float(i)

        return result
