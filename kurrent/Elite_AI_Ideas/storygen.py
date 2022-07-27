from random import randint

def characterGen():
	characters = [
		"Charlie",
		"Bob",
		"Liam",
		'Ethan',
		"Eli",
		"Asher",
		"Ryan",
		"Jason",
		"Billy",
		"George",
		"Cleve",
		"Erica",
		"Brodie",
		"Kate",
		"Aayla",
		"Hudson",
		"Yuujin",
		"Aom"
	]
	return characters[randint(0, len(characters) - 1)]

def introGen():
	introList = [
		"Once upon a time,",
		"Long, long ago,",
		"In a faraway land,",
		"In a distant land,",
		"In a magical forest,",
		"Inside a living video game,",
		"In a magical forest,",
		"In a place beyond the void,",
		"Inside the mind of a crazy gray bird,",
	]
	return introList[randint(0, len(introList) - 1)]

def actionGen():
	actions = [
		"kicked",
		"pushed",
		"hugged",
		"licked",
		"head-butted",
		"rolled",
		"chucked",
		"strangled",
		"punched",
		"ripped",
		"poked",
		"cut",
		"massaged",
		"fought",
		"sliced",
		"snapped",
		"touched",
	]
	return actions[randint(0, len(actions) - 1)]

def objectGen():
	objects = [
		"ball",
		"bird",
		"poop",
		"log",
		"bug",
		"tree",
		"dog",
		"cat",
		"human",
		"eyeball",
		"bear",
		"brick",
		"wall",
		"dirt block",
		"bed",
		"rock",
		"diamond",
		"pen",
		"cup",
	]
	return objects[randint(0, len(objects) - 1)]

count = 0
while count < 526:
	character = characterGen()
	intro = introGen()
	action = actionGen()
	object = objectGen()
	with open("stuff.txt", "a+") as file:
		file.write(f"{intro} a boy named {character} {action} a {object}.\n")
	count += 1