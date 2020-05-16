import sys
import os

# fuck this bullshit

def parse(x):
	x = x.replace("golem", "go")
	x = x.replace("runerigus", "run")
	print(x)
	os.system(x)


print('Welcome to pokemon-go. Run your command')
while(True):
	x = input("$ ")
	parse(x)


