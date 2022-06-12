import os.path
import random
import time
from utils.cmdUtils.CommandUtils import HelpMenu
import webbrowser
from mutagen.mp3 import MP3
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from playsound import playsound
from pytube import Playlist


class CmdMusic:
    def __init__(self):
        self.cmdList = {
            "help": MusicHelp(),
            "play": CmdPlay(),
            "auto": CmdAuto(),
            "dPlaylist": CmdDownloadPlaylist(),
        }
        self.details = [
            "Used to create a help menu for the Music Command",
            "Used to play a specified music file",
            "Used to autoplay music files",
            "Used to download music off of youtube",
        ]

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            MusicHelp().run(interPackage)


class MusicHelp:
    def run(self, interPackage):
        HelpMenu('folder', CmdMusic().cmdList, CmdMusic().details).makeHelpMenu()


class CmdAuto:
    def __init__(self):
        self.dirName = self.getDirName()

    def run(self, interPackage):
        while True:
            songs = os.listdir(self.dirName)
            shuffled = songs
            random.shuffle(shuffled)
            print("Songs up next:")
            for i in shuffled:
                print(f"\t[{i}]")
            print()

            for i in shuffled:
                try:
                    print(f'Playing: [{i}]', end='\r')
                    song = os.path.join(self.dirName, i)
                    playsound(os.path.join(self.getDirName(), i))
                    message = f"Playing: [{i}]"
                    spaces = ' ' * (100 - len(message))
                    print(f"{message}{spaces}", end='\r')
                except:
                    pass
            print()

    def getDirName(self):
        paths = os.path.join(os.getcwd(), str(SystemConfigUtils().load("MUSIC_LOC")))
        return paths


class CmdPlay:
    def __init__(self):
        self.dirName = self.getDirName()

    def run(self, interPackage):
        if interPackage.syntax:
            webbrowser.open(os.path.join(self.getDirName(), interPackage.syntax[0]))
        else:
            print("Write down the song you want to play")
            inpit = input('>')
            print(f'Playing: [{inpit}]')
            webbrowser.open(os.path.join(self.getDirName(), inpit))

    def getDirName(self):
        paths = os.path.join(os.getcwd(), SystemConfigUtils().load("MUSIC_LOC"))
        return paths


class CmdDownloadPlaylist:
    def __init__(self):
        self.dirName = self.getDirName()

    def run(self, interPackage):
        if interPackage.syntax:
            self.downloadMusic(interPackage.syntax[0])
        else:
            print("Write down the URL of the youtube playlist")
            a = input(">")
            self.downloadMusic(a)

    def downloadMusic(self, playlistURL):

        try:
            os.makedirs(os.path.join(os.getcwd(), SystemConfigUtils().load("MUSIC_LOC")))
        except:
            pass

        p = Playlist(playlistURL)

        print(f"Downloading: {p.title}\n")

        count = 0
        for i in p.videos:
            count += 1
            print(f"{count}. {i.title}")
            st = i.streams.get_highest_resolution()

            st.download(self.dirName)

        print("\nDone!")

    def getDirName(self):
        return os.path.join(os.getcwd(), SystemConfigUtils().load("MUSIC_LOC"))
