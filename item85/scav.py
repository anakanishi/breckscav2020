import sys
import os

#item 85

def createFile(initial_command):
	filename = initial_command.split(" ")
	print(filename)
	print(filename[2])
	f = open(filename[2], "r")
	text = f.read()
	f.close()
	text = text.replace("furret", "func")
	text = text.replace("burmy", "package")
	text = text.replace("impidimp", "import")
	print(text)
	f = open(filename[2].replace("pok", "go"), "w")
	f.write(text)
	f.close()


	

def parse(x):
	x = x.replace("golem", "go")
	x = x.replace("runerigus", "run")
	x = x.replace("pok", "go")
	print(x)
	os.system(x)


print('Welcome to pokemon-go. To run your pokemon-go file, please run: golem runerigus [filename].pok')
while(True):
	file = input("$ ")
	createFile(file)
	parse(file)


