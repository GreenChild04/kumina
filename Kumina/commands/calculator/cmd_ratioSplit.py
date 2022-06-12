from utils.cmdUtils.CommandUtils import InterPackage


class CmdRatioSplit:
    def __init__(self):
        pass

    def run(self, interPackage):
        if interPackage.syntax:
            print(f'Ans: {self.cal(interPackage.syntax)}')
        else:
            print('Write down the number you want to find the ratio split of and separate them with a \',\'')
            inpit = input('>')
            inpit = inpit.strip(' ')
            inpit = inpit.split(',')
            print('\nAns: ' + str(self.cal(inpit)))

    def cal(self, num):
        result = ""
        listable = []
        # equation
        ratio = str(num[1]).split(":")
        ratioSum = sum(self.toFloat(ratio))
        frac = float(num[0]) / ratioSum

        for i in range(ratio.__len__()):
            listable[i] = float(frac) * float(ratio[i])

        for i in listable:
            result += str(listable[i]) + ":"

        result = result[:-1]

        return result

    def toFloat(self, iList):
        result = []
        for i in iList:
            result.append(float(i))

        return result
