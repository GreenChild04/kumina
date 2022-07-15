import math


class CmdPrimeFactors:
    def __init__(self):
        pass

    def cal(self, num):
        output = []

        i = 2

        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                output.append(i)
        if num > 1:
            output.append(num)

        return output

    def run(self, interPackage):
        if interPackage.syntax:
            print(f'Ans: {self.asString(self.cal(interPackage.syntax[0]))}')
        else:
            print('Write down the number you want to find the prime factors of')
            inpit = input('>')
            print('\nAns: ' + str(self.asString(self.cal(int(inpit)))))

    def asString(self, cal):
        output = ''
        for i in cal:
            output += f'{i}, '

        return output
