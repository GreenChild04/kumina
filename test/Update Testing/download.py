import urllib.request as request
import requests
import os

initial = requests.get("https://www.evernote.com/shard/s631/sh/c925ed1f-1973-1bb3-ab49-679ac83ced3c/8cffc7673791616d8d41cd7cbd7202f0").text
open("log.html", "w+").write(initial)
initial = initial.split("content=\"")[6].split("\"")[0].replace(" ", "\n")

currentLargest = 3.0
currentLink = "https://ethanballs.net"

script = initial
scList = script.split("\n")
for i in scList:
	try:
		version = float(i.split("~")[0])
		link = i.split("~")[1]
		if version > currentLargest:
			currentLargest = version
			currentLink = link
			print(version)
	except: pass

print(currentLink)

