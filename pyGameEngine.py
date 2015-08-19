### Imports
import pickle, os, platform, random

### Functions
def main():
	curPlayer = loadPlayer( 'Tory' )
	curGame   =   loadGame( 'Python_Tutorial' ) 
	startGame(curPlayer, curGame)
	
def banner():
	'''
	if platform.system() == "Windows":
		clearCmd = "cls"
	elif platform.system() == "Linux":
		clearCmd = "clear"
	else:
		print ("Unknown operating system detected. Some operations may not perform correctly!\n")
	os.system(clearCmd)
	'''
	version = 0.1
	banner = ("  **Welcome to the Python Learning Environment\n\
  **Written by Tory Clasen - Version: " + str(version) + "   \n\
  **For help at any time please type '?' or 'help'           \n\
  **To exit the program type 'exit' or 'quit'                \n\n")
	print banner
	
def startGame(curPlayer, curGame):
	try:
		curScore = curPlayer['score'][curGame['gameName']]
	except:
		curScore = 0

	while True:
		#banner()
		print '----------------------------------------\n' + curGame['gameName'] + ' has been loaded'
		print curGame['banner'] + '\n----------------------------------------'
		try:
			pickle.dump( curPlayer, open( ( str(curPlayer['Name']) + ".plep"), "wb" ) )
		except:
			print "Error! Unable to save player profile at current location!"
		print 'Your current score is: ' + str(curScore) + ' out of a total possible score of: ' + str(len(curGame['gameData']))
		print "Question " + str(curScore) + ": \n" + str(curGame['gameData'][curScore]["Q"]) + "\n"
		temp = curGame['gameData'][curScore]["D"]
		data = eval(str(curGame['gameData'][curScore]["D"]))
		print "Data " + str(curScore) + ": \n" + data
		print '----------------------------------------\n'
		try:
			myAnswer = eval(str(getInput('What command do you want to submit? ')))
			if myAnswer == (eval(str(curGame['gameData'][curScore]["A"]))):
				print "Correct!"
				curScore = curScore + 1
			else:
				print "Incorrect!"
		except:
			print 'The answer you submitted crashed the program, so it was probably wrong'
		#break
		
def getInput(prompt):
	theInput = raw_input( str(prompt) + "\n" )
	if theInput == '?' or theInput.lower() == 'help':
		print "HELP! HELP!"
	elif theInput.lower() == 'exit' or theInput.lower() == 'quit':
		raise SystemExit
	else:
		return theInput

def loadPlayer(playerName = ''):
	#banner()
	curPlayer = {}
	
	if playerName == '':
		playerName = getInput("I would like to load your profile. \nWhat is your name? ")
	
	try:
		# Attempt to load the player file.
		curPlayer = pickle.load( open( ( str(playerName) + ".plep"), "rb" ) )
		print "Player profile found... loading player data..."
	except:
		# Ask the player if they want to try to create a new profile file.
		createNew = getInput( "Player profile not found for '" + str(playerName)  + "'\nWould you like to create a new one? [Y/N]").lower()
		curPlayer = {'Name':playerName}
		if createNew == "y":
			try:
				pickle.dump( curPlayer, open( ( str(playerName) + ".plep"), "wb" ) )
				print "Player profile successfully created!"
			except:
				print "Error! Unable to create player profile at current location!"
		else:
			print "Progress will not be saved for you..."
	return curPlayer		
	
def loadGame(gameName = ''):
	banner()
	curGame = {}

	while True:
		if gameName == '':
			gameName = getInput("What game would you like to load? ")
		try:
			# Attempt to load the player file.
			curGame = pickle.load( open( ( str(gameName) + ".pleg"), "rb" ) )
			print "Game module found... loading game data..."
			gameName = ''
			break
		except:
			gameName = ''
			print "Game module not found... please try again..."
	return curGame		
	
main()
