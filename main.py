from time import sleep
import pyinputplus as pyip

# constants
broadMargin = .1 # 1 percent point
refinedMargin = .1 # .1 percent point (for refining)

def addScore(num, deno): 
	# appends to numerator and denominator
	numerator.append(num)
	denominator.append(deno)

def findScores(): 
	# find all possible grades, given an amount of questions on the test
	for numMissed in range(0, totalQuestions+1):
		calcScore = ((totalQuestions - numMissed) / totalQuestions) * 100
		# print(calcScore)
		global index
		index = 0
		if (score - broadMargin) < calcScore < (score + broadMargin):
			addScore(totalQuestions - numMissed, totalQuestions)

def restart():
	again = pyip.inputYesNo("[y/n] ")
	if again == 'yes':
		start()
	else:
		print("\nThanks for using this program! Have a nice day.")
def results():
	# shows results of calculations
	if not numerator:
		print("\nI can't find any matching scores. Play again?")
		restart()
	else:
		print("\nGetting your scores...")
		sleep(0.5)
		for i, otherGuesses in enumerate(numerator):
			# only show the values from indexes that were not in the accurate list
			num = numerator[i]
			deno = denominator[i]
			percent = (num/deno) * 100
			print(f"You got {num} questions right out of {deno}, so you got a {percent:.2f}%." )
		print("\nWould you like to play again?")
		restart()

def start():
	# indexes are synced -> percent = numerator[1] / denominator[1], etc
	global numerator, denominator
	numerator = [] # guesses for how many I got right
	denominator = [] # guesses for how many questions are on the test

	# introduction
	print('Based on your test score, I will find find out\nhow many questions are on the test, and \nhow many you missed.\n\nHowever, I need an estimate of how many questions were\non the test. Please enter your lower and higher guess below.\n')

	# user inputs
	min = pyip.inputInt("Lower guess of number of questions: ", min=1)
	max = pyip.inputInt("Higher guess of number of questions: ", min=1)
	global score
	score = float(input("Your score: "))
	score = pyip.inputNum("Your score: ", min=0, max=100)

	# makes sure the min and max are not flipped
	if min > max:
		min, max = max, min
	
	global totalQuestions
	for totalQuestions in range(min, max+1):
		# do this for every possible amount of questions on the test
		findScores()
	results() # show results

start() # begins the program