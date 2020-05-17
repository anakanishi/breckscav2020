import sys
import os

#item 85

def createGoFile(pok_filename):
	"""
	Reads in the contents of the .pok file
	Writes the translated poklang into a .go file
	Args:
		pok_filename: name of the .pok file (should be in the same directory as this code)
	"""
	f = open(pok_filename, "r")
	pok_text = f.read()
	f.close()
	go_text = parsePokLang(pok_text)
	f = open(pok_filename.replace("pok", "go"), "w")
	f.write(go_text)
	f.close()

def parsePokLang(text):
	"""
	Translates poklang into golang
	Args:
		text: poklang code
	Returns:
		text: golang code
	"""
	text = text.replace("breloom", "break")
	text = text.replace("dewott", "default")
	text = text.replace("furret", "func")
	text = text.replace("inteleon", "interface")
	text = text.replace("seel", "select")
	text = text.replace("cascoon", "case")
	text = text.replace("delcatty", "defer")
	text = text.replace("golem", "go")
	text = text.replace("marowak", "map")
	text = text.replace("starly", "struct")
	text = text.replace("chansey", "chan")
	text = text.replace("eldegoss", "else")
	text = text.replace("gothita", "goto")
	text = text.replace("burmy", "package")
	text = text.replace("swirlix", "switch")
	text = text.replace("conkeldurr", "const")
	text = text.replace("falinks", "fallthrough")
	text = text.replace("igglybuff", "if")
	text = text.replace("raichu", "range")
	text = text.replace("typhlosion", "type")
	text = text.replace("corphish", "continue")
	text = text.replace("forretress", "for")
	text = text.replace("impidimp", "import")
	text = text.replace("remoraid", "return")
	text = text.replace("vaporeon", "var")
	return text

def runPokLang(command, pokFile):
	command = command.replace("golem", "go")
	command = command.replace("runerigus", "run")
	command = command.replace("pok", "go")
	os.system(command)

	# Delete the go file that was created
	go_file = pokFile.replace("pok", "go")
	os.remove(go_file)


print('Welcome to pokemon-go. To run your pokemon-go file, please run: golem runerigus [filename].pok')
command = input("$ ")
filename = command.split(" ")[2]
createGoFile(filename)
runPokLang(command, filename)


