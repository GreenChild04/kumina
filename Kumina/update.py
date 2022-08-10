import os
import requests
from urllib import request
import sys


def getVersions():
    versionData = requests.get(
        "https://www.evernote.com/shard/s631/sh/c925ed1f-1973-1bb3-ab49-679ac83ced3c/8cffc7673791616d8d41cd7cbd7202f0"
    ).text
    versionData = versionData.split("content=\"")[6].split("\"")[0].replace(" ", "\n")
    return versionData


def getLatestVersion(currentVersion):
    try:
        currentLink = None
        currentLargest = float(currentVersion)
        script = getVersions()
        scList = script.split("\n")
        for i in scList:
            try:
                version = float(i.split("~")[0])
                link = i.split("~")[1]
                if version > currentLargest:
                    currentLargest = version
                    currentLink = link
            except:
                pass
    except: pass
    if currentLink:
        return True, currentLink, currentLargest
    else:
        return False, currentLink, currentLargest


def update(current):
    currentLink = getLatestVersion(current)[1]
    print(currentLink)
    request.urlretrieve(currentLink, os.path.join(os.getcwd(), "kumina.exe"))


def run(current):
    print("Updating...")
    try:
        os.rename("kumina.exe", "kumina_old.exe")
    except:
        pass
    if getLatestVersion(current)[0]:
        update(current)
    print("Done!")
    os.system("start kumina.exe")
    sys.exit()


if __name__ == "__main__":
    run(0)
