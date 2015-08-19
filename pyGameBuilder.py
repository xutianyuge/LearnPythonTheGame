 # Imports
import pickle, random

game = {"gameName":"Python_Tutorial", "version":"1.0", "engineVersion":"0.1", "banner":"To see a hint for your current question, submit 'hint'\nThe data provided is stored in a variable called 'data' that you can use in your solutions.", "gameData":[ {	\
				"Q":"Convert the string in data to an integer.", \
				"D":"'00' + str(random.randint(10, 99))", \
				"A":"int(data)", \
				"T":"T", \
				"H":"The 'int()' command will convert a string to an integer."} \

			,{	"Q":"Convert the hex value stored as a string to an integer.", \
				"D":"hex(random.randint(17, 255))", \
				"A":"int(data, 16)", \
				"T":"T", \
				"H":"The 'int()' command supports not only integers as strings, but also hex values as strings. You feed it an argument of '16' along with the string."} \

			,{	"Q":"Split the string supplied into a list.", \
				"D":"temp.split()[random.randint(0, len(temp.split())-1)] + ' ' + temp.split()[random.randint(0, len(temp.split())-1)]", \
				"A":"data.split()", \
				"T":"this is a random collection of words that will be used for this question", \
				"H":"String.split() where 'string' is the name of your string will split your string into a list by consuming everything specified in the arguments. If no argument is supplied it is assumed to be ' '."} \

			,{	"Q":"Count the number of number of words in the supplied data.", \
				"D":"' '.join([temp.split()[random.randint(0, len(temp.split())-1)] for x in range(random.randint(3, 8))])", \
				"A":"len(data.split())", \
				"T":"this is a random collection of words that will be used for this question but I might need to add more since this one will use up more than the others", \
				"H":"After splitting your data into a list, passing it to the 'len()' command will count the number of items in the list."} \

			,{	"Q":"Sum together all of the values supplied in the data.", \
				"D":"' '.join( [ str(random.randint(10, 99)) for x in range( random.randint(3, 8) ) ] )", \
				"A":"sum(map(int, data.split()))", \
				"T":"T", \
				"H":"This exercise requires splitting the string into a list, then converting each item in the list into an integer, then summing them together."} \

			,{	"Q":"Create an if statement for if the data is equal to 'A' return 'True' and for anything else return 'False'.", \
				"D":"temp.split()[random.randint(0, 3)]", \
				"A":"['False', 'True'][data == 'A']", \
				"T":"A B C D", \
				"H":"A simple single line if statement can be contructed like this: ['Greater than 5', 'Less than 5'][data < 5]. By having the right set of data evaluate to either True or False in binary results in generating either a 0 or a 1. And that value is used to query data from the list on the left."} \

			,{	"Q":"Q", \
				"D":"D", \
				"A":"A", \
				"T":"T", \
				"H":"H"} \

			,{	"Q":"Q", \
				"D":"D", \
				"A":"A", \
				"T":"T", \
				"H":"H"} \

			,{	"Q":"Q", \
				"D":"D", \
				"A":"A", \
				"T":"T", \
				"H":"H"} \

			]}

pickle.dump( game, open( ( str(game["gameName"]) + ".pleg"), "wb" ) )

myGame = pickle.load( open( ( str(game["gameName"]) + ".pleg"), "rb" ) )

for i in range(len(myGame["gameData"])):
	print "Q " + str(i) + ": " + myGame["gameData"][i]["Q"]
	print "T " + str(i) + ": " + myGame["gameData"][i]["T"]
	print "H " + str(i) + ": " + myGame["gameData"][i]["H"] + "\n"
	print "D-" + str(i) + ": " + myGame["gameData"][i]["D"]
	print "A-" + str(i) + ": " + myGame["gameData"][i]["A"] + "\n"
	try:
		temp = myGame["gameData"][i]["T"]
		data = eval(myGame["gameData"][i]["D"])
		print "D " + str(i) + ": " + str(data)
	except:
		print "D " + str(i) + ": Error"
	try:
		print "A " + str(i) + ": " + str(eval(myGame["gameData"][i]["A"])) + "\n"
	except:
		print "A " + str(i) + ": Error"
	print "----------------------" + "\n"
