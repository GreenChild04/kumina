import os.path
import random
import time
from utils.cmdUtils.CommandUtils import HelpMenu
import webbrowser
from utils.cmdUtils.systemConfigUtils import SystemConfigUtils
from playsound import playsound
from pytube import Playlist
from udr.utils.udrUtils import HelpMenu


class CmdMusic:
    def __init__(self):
        self.cmdList = {
            "help": MusicHelp(),
            "play": CmdPlay(),
            "auto": CmdAuto(),
            "playlist": CmdDownloadPlaylist(),
        }
        self.details = [
            "Used to create a help menu for the Music Command",
            "Used to play a specified music file",
            "Used to autoplay music files",
            "Used to download music off of youtube",
        ]
        self.hm = HelpMenu("music", helpInfo=[
            "-",
            "music",
            "music.help",
        ])

    def run(self, interPackage):
        if len(interPackage.cmdDir) > 0:
            interPackage.cmdList = self.cmdList
            interPackage.runCommands()
        else:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                MusicHelp().run(interPackage)


class MusicHelp:
    def run(self, interPackage):
        HelpMenu('folder', CmdMusic().cmdList, CmdMusic().details).makeHelpMenu()


class CmdAuto:
    def __init__(self):
        self.dirName = self.getDirName()
        self.hm = HelpMenu("auto", helpInfo=[
            "-",
            "music.auto",
            "music.auto: -h",
        ])

    def run(self, interPackage):
        if interPackage.checkSwitch("h"):
            self.hm.makeHelpInfo()
        else:
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
                        message = f"Playing: [{i}]"
                        spaces = ' ' * (100 - len(message))
                        print(f"{message}{spaces}", end='\r')
                        if os.name != "nt":
                            playsound(os.path.join(self.getDirName(), i))
                        else:
                            def with_moviepy(filename):
                                from moviepy.editor import VideoFileClip
                                clip = VideoFileClip(filename)
                                duration = clip.duration
                                fps = clip.fps
                                width, height = clip.size
                                return duration
                            dur = with_moviepy(os.path.join(self.getDirName(), i))
                            webbrowser.open(os.path.join(self.getDirName(), i))
                            print(dur)
                            for a in range(dur.round()):
                                time.sleep(1)
                                message = f"Playing: [{i}] time:{a}/{dur.round()}"
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
        self.hm = HelpMenu("play", helpInfo=[
            "-"
        ])

    def run(self, interPackage):
        if interPackage.checkSwitch("h"):
            pass
        webbrowser.open(os.path.join(self.getDirName(), interPackage.syntax[0]))

    def getDirName(self):
        paths = os.path.join(os.getcwd(), SystemConfigUtils().load("MUSIC_LOC"))
        return paths


class CmdDownloadPlaylist:
    def __init__(self):
        self.dirName = self.getDirName()
        self.hm = HelpMenu("playlist", helpInfo=[
            "-",
            "music.playlist: \"urlOfPlaylist\"",
            "music.playlist: -h",
        ])

    def run(self, interPackage):
        if interPackage.isColon:
            if interPackage.checkSwitch("h"):
                self.hm.makeHelpInfo()
            else:
                self.downloadMusic(interPackage.inpit[0])
        else:
            self.hm.makeHelpInfo()

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
