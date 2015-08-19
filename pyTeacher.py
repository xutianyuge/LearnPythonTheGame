from random import randint

class game:
	myScore = [0,0,0,0,0,0,0,0,0,0,0,0,0]

	def __init__(self):
		self.generateData()
			
	def generateData(self):
		q0 = 'The data element contains a string comprised of two integers separated by a space. add the m together and submit the sum.'
		d0 = str(randint(10, 89)) + " " + str(randint(1, 9))
		a0 = sum(map(int, d0.split()))
	
		q1 = 'The data element contains a long string. Extract the substring that is surrounded by dashes. submit that substring.'
		d1 = str( chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) + '-' + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) + '-' + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90)) )
		a1 = d1.split('-')[1]
		
		tmp = ["My sample sentence for this course", "Some stupid text generator", "Are you really paying attention?", "I dont think anyone is going to notice this", "What were we doing again?"]
		q2 = 'Return the 2nd word in the sentence in reverse. Example "The quick brown cow" would be "kciuq"'
		d2 = str(tmp[randint(0, (len(tmp)-1))])
		a2 = d2.split()[1][::-1]
		
		tmp = ["Did we learn how to Base64 encode stuff?", "I'm pretty sure I was sleeping through class", "What is Python?", "What is love?", "Baby don't hurt me"]
		q3 = 'Base64 decode the string and submit the answer'
		d3 = str(tmp[randint(0, (len(tmp)-1))].encode('Base64'))
		a3 = d3.decode('Base64')
		
		q4 = 'The data contains a string of numbers separated by commas. Add together all the numbers and submit the total.'
		d4 = str(randint(1, 30)) + "," + str(randint(1, 30)) + "," + str(randint(1, 30)) + "," + str(randint(1, 30)) + "," + str(randint(1, 30))
		a4 = sum(map(int, d4.split(',')))
		
		tmp = ["Never gonna give you up.", "Never gonna let you down", "Never gonna run around", "And desert you"]
		q5 = 'Cut the string in half and submit the 2nd half. Example: "Hello world" would be " world"'
		d5 = str(tmp[randint(0, (len(tmp)-1))])
		a5 = d5[(len(d5)/2):]
	
		tmp = ["0xFF", "0xAA", "0x2A", "0xA3", "0xFA", "0xCC", "0xC0", "0x10"]
		q6 = 'Convert the base16 string to a decimal number example: "0xFF" would be 255'
		d6 = str(tmp[randint(0, (len(tmp)-1))])
		a6 = int(d6, 16)
		
		tmp = [["a", "b", "c", "d", "e", "f"], ["q", "c", "e", "z", "q", "e", "q", "v", "d"], ["d", "q", "i", "v"], ["m", "n", "w", "n", "h", "k"], ["z", "c", "m", "e", "f", "c", "z"]]
		q7 = 'The data contains a list. What is the 3rd item in the list?'
		d7 = tmp[randint(0, (len(tmp)-1))]
		a7 = d7[2]
		
		tmp = [{'combat':'zone', 'computer':'stuff', 'cyber':'warrior', 'sans':'training'}, {'awesome':'sauce', 'space':'time', 'inter':'webs', 'cyber':'space'}, {'castle':'crushers', 'cyber':'defenders', 'block':'breakers', 'tetris':'tetrisers?'}]
		q8 = 'The data contains a dictioniary. What is the value in the entry with a key of "cyber"?'
		d8 = tmp[randint(0, (len(tmp)-1))]
		a8 = d8['cyber']

		q9 = 'It is currently 2130 hours. The data element contains how many hours are left on your shift as towel hander at gym 5. What time will it be when your shift ends. Express your answer in proper military time. Example: 0130'
		d9 = randint(1, 8)
		a9 =  str([[('0' + str((2130 + (d9 * 100)) - 2400)), ('00' + str((2130 + (d9 * 100)) - 2400))][d9==3], ((2130 + (d9 * 100)))][(((2130 + (d9 * 100))) < 2400)])

		tmp = [["I am headed to the hospital", 0], ["I work at the NSA", 1], ["I work at signal towers", 2], ["I just really like to drive fast", 0.5], ["There are speeds?", 0.5], ["Sorry, I'm drunk", 0.5]]
		q10 = 'The data contains your current driving speed and an excuse. The speed limit is 15 MPH on post and you just got pulled over. If you are not speeding there is no fine. If your speed is less than 5 MPH over the limit then you are fined $20. Iif your speed is 5 MPH or more over the limit you are fined $40. However yhou can try various excuses on the MPs. If your excuse is "I work at the NSA" no adjustment to the fine is made. If your excuse is "I work at signal towers" your fine is doubled. If your excuse is "I am headed to the hospital" no fine is issued. Any other excuse cuts the fine in half. Submit the fine as an integer (no $ signs, no decimal points).'
		d10 = [randint(10, 30), tmp[randint(0, (len(tmp)-1))][0]]
		a10 = int([[[0.5, 2][d10[1]=="I work at signal towers"], 1][d10[1]=="I work at the NSA"], 0][d10[1]=="I am headed to the hospital"] * [[20, 40][d10[0] > 20], 0][d10[0] <= 15])
		
		q11 = 'Add together all the unique numbers in the string. If a number is not unique do not include it in the total. Example: 1, 1, 2, 3, 4, 4 would be 5.'
		d11 = str(randint(1, 8)) + ", " + str(randint(1, 8)) + ", " + str(randint(1, 8)) + ", " + str(randint(1, 8)) + ", " + str(randint(1, 8)) + ", " + str(randint(1, 8)) + ", " + str(randint(1, 8)) + ", " + str(randint(1, 8))
		a11 = len([x for x in d11.split(', ') if d11.split(', ').count(x)==1])
		
		tmp = [["Delta", "United", "Ryan"], ["Atlanta", "Portland", "Chicago", "Frankfurt"], ["Sunny", "Raining"]]
		q12 = 'If you are flying "Delta" airlines and it is "Raining" your flight will be delayed. If you are in "Atlanta" GA, your flight will be delayed regardless of weather. The data element contains your airline, the weather and your location. Return "delayed" or "not-delay".'
		d12 = [tmp[0][randint(0, (len(tmp[0])-1))], tmp[1][randint(0, (len(tmp[1])-1))], tmp[2][randint(0, (len(tmp[2])-1))]]
		a12 = [["not-delay", "delayed"][d12[0]=="Delta" and d12[2]=="Raining"], "delayed"][d12[1]=="Atlanta"]
		
		self.gameData = [{'Q': q0, 'D': d0, 'A': a0}, {'Q': q1, 'D': d1, 'A': a1}, {'Q': q2, 'D': d2, 'A': a2}, {'Q': q3, 'D': d3, 'A': a3}, {'Q': q4, 'D': d4, 'A': a4}, {'Q': q5, 'D': d5, 'A': a5}, {'Q': q6, 'D': d6, 'A': a6}, {'Q': q7, 'D': d7, 'A': a7}, {'Q': q8, 'D': d8, 'A': a8}, {'Q': q9, 'D': d9, 'A': a9}, {'Q': q10, 'D': d10, 'A': a10}, {'Q': q11, 'D': d11, 'A': a11}, {'Q': q12, 'D': d12, 'A': a12}]
		return 
	
	def question(self, num):
		self.generateData()
		return self.gameData[num]['Q']

	def data(self, num):
		self.generateData()
		return self.gameData[num]['D']
	
	def score(self):
		if sum(map(int, self.myScore))==13:
			return 'You win the game! Now go outside and play.'
		else:
			return self.myScore	

	def answer(self, num, sub):
		if sub == self.gameData[num]['A']:
			self.generateData()
			self.myScore[num] = 1
			return 'Correct!'
		else:
			self.generateData()
			return 'Incorrect!'
