from utils.cmdUtils.CommandUtils import InterPackage
from utils.cmdUtils.CommandUtils import HelpMenu
from commands.calculator.cmd_average import CmdAverage
from commands.calculator.cmd_hcfLcm import CmdHcf
from commands.calculator.cmd_hcfLcm import CmdLcm
from commands.calculator.cmd_primeFactors import CmdPrimeFactors
from commands.calculator.cmd_add import CmdAdd
from commands.calculator.cmd_subtract import CmdSubtract
from commands.calculator.cmd_multiply import CmdMultiply
from commands.calculator.cmd_ratioSplit import CmdRatioSplit
import commands.calculator.cmd_calCal


class Calculator:
    def __init__(self):
        self.cmdList = {
            'help': CalHelpMenu(),
            'avg': CmdAverage(),
            'prime': CmdPrimeFactors(),
            'hcf': CmdHcf(),
            'lcm': CmdLcm(),
            'add': CmdAdd(),
            'sub': CmdSubtract(),
            'mul': CmdMultiply(),
            'ratSplit': CmdRatioSplit(),
        }

        self.details = [
            'Creates Help menu for cmd user',
            'Used to find the average of a number',
            'Used to find the prime factors of a number',
            'Used to find the highest common factor of a list of numbers',
            'Used to find the lowest common multiple of a list of numbers',
            'Used to add all the numbers in a list',
            'Used to subtract all the numbers combined from the first number',
            'Used to multiply all the numbers in a list',
            "Used to get the result of splitting a number into a ratio",
        ]

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            while True:
                text = input('calculator>')
                print()
                result, error = commands.calculator.cmd_calCal.run('<stdin>', text)

                if error:
                    print(error.as_string())
                else:
                    print(f'Ans: {result}\n')

        

class CalHelpMenu:
    def run(self, interPackage):
        HelpMenu('calculate', Calculator().cmdList, Calculator().details).makeHelpMenu()
