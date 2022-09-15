from utils.cmdUtils.CommandUtils import InterPackage
from commands.calculator.cmd_primeFactors import CmdPrimeFactors
import math
import collections





class CmdHcf:
    def __init__(self):
        pass

    def run(self, interPackage):
        if interPackage.syntax:
            print(f'Ans: {self.cal(interPackage.syntax)}')
        else:
            print('Write down the numbers you want to find the Highest Common Factor of and separate them with a \',\'')
            inpit = input('>')
            inpit = inpit.strip(' ')
            inpit = inpit.split(',')
            print('\nAns: ' + str(self.cal(inpit)))

    def cal(self, nums):
        numPrimes = []
        middle = []
        numNoListPrimes = []
        dupes = []
        sides = []
        sidesNo = []
        hcf = 1

        for i in nums:
            numPrimes.append(CmdPrimeFactors().cal(float(i)))
            sides = numPrimes

        for i in numPrimes:
            for d in i:
                numNoListPrimes.append(d)

        for i in numNoListPrimes:
            if self.findDupes(i, numPrimes):
                dupes.append(i)
        dupes = list(dict.fromkeys(dupes))

        for i in dupes:
            count = self.findDupeAmount(i, numPrimes)

            for a in range(count):
                middle.append(i)

        for i in numPrimes:
            for a in middle:
                sides[numPrimes.index(i)].remove(a)

        for i in sides:
            for a in i:
                sidesNo.append(a)

        hcf = self.timesList(middle)

        return hcf

    def findDupes(self, item, iList):
        itemCount = 0

        for i in iList:
            for a in i:
                if a == item:
                    itemCount += 1
                    break

        if itemCount == len(iList): return True

        return False

    def timesList(self, myList):
        result = 1
        for x in myList:
            result = result * x

        return result

    def findDupeAmount(self, item, iList):
        itemCount = []
        lowestCount = 9999999
        for i in iList:
            itemCount.append(i.count(item))

        for i in itemCount:
            if i < lowestCount:
                lowestCount = i

        return lowestCount


class CmdLcm:
    def __init__(self):
        pass

    def run(self, interPackage):
        if interPackage.syntax:
            print(f'Ans: {self.cal(interPackage.syntax)}')
        else:
            print('Write down the numbers you want to find the Lowest Common Multiple of and separate them with a \',\'')
            inpit = input('>')
            inpit = inpit.strip(' ')
            inpit = inpit.split(',')
            print('\nAns: ' + str(self.cal(inpit)))

    def cal(self, iList):
        return self.LCMofArray(self.makeListVar(iList, int))

    def makeListVar(self, iList, var):
        aList = iList
        for i in range(len(iList)):
            aList[i] = var(iList[i])

        return aList

    def LCMofArray(self, a):
        lcm = a[0]
        for i in range(1, len(a)):
            lcm = lcm * a[i] // math.gcd(lcm, a[i])
        return lcm
