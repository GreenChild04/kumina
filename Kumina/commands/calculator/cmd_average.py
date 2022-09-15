from utils.cmdUtils.CommandUtils import InterPackage


class CmdAverage:
    def __init__(self):
        pass

    def run(self, interPackage):
        if interPackage.syntax:
            print(f'Ans: {self.cal(interPackage.syntax)}')
        else:
            print('Write down the numbers you want to find the average of and separate them with a \',\'')
            inpit = input('>')
            inpit = inpit.strip(' ')
            inpit = inpit.split(',')
            print('\nAns: ' + str(self.cal(inpit)))

    def cal(self, numbers):
        num = 0

        for i in numbers:
            num += float(i)

        num /= len(numbers)

        return num
