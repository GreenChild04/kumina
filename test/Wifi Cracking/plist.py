from pathlib import Path
from tqdm import tqdm


def gennum(length):
    bar = tqdm(total=(10 ** length), position=0)
    bar.set_description("Generating Number Passwords")
    passwords = []
    for i in range(0, (10 ** length)):
        currentChar = []
        for a in str(i):
            currentChar.append(int(a))
        while len(currentChar) < length:
            currentChar.insert(0, 0)
        passwords.append(currentChar)
        bar.update()
    return passwords


def listToNum(listen):
    final = ""
    for i in listen:
        final += str(i)
    return final


if __name__ == "__main__":
    # with Path("plist.dic") as file:
    #	file.write_text(gennum())
    num = int(input("[length]-"))
    with open("passwords.pwd", "a+") as file:
        listable = gennum(num)
        bar = tqdm(total=len(listable))
        bar.set_description("Writing combinations into file")
        for i in listable:
            file.write(listToNum(i) + "\n")
            bar.update()
    print("done")
    input("press enter to close")
