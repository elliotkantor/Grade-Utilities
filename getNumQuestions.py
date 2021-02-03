from time import sleep
import pyinputplus as pyip
import logging
from os import system, name

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s -  %(levelname)s -  %(message)s"
)
logging.disable(logging.CRITICAL)  # to disable critical logs after this

BROAD_MARGIN = 0.1  # 1 percent point


def clear():
    # windows
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def addScore(num, deno):
    # appends to numerator and denominator
    numerator.append(num)
    denominator.append(deno)


def findScores():
    # find all possible grades, given an amount of questions on the test
    for totalQuestions in range(minGuess, maxGuess + 1):
        for numMissed in range(0, totalQuestions + 1):
            calcScore = ((totalQuestions - numMissed) / totalQuestions) * 100
            logging.debug("calcScore = " + str(calcScore))
            if (score - BROAD_MARGIN) < calcScore < (score + BROAD_MARGIN):
                addScore(totalQuestions - numMissed, totalQuestions)


def results():
    # shows results of calculations
    if len(numerator) == 0:
        print("\nI can't find any matching scores.")
    else:
        # for i, otherGuesses in enumerate(numerator):
        for num, deno in zip(numerator, denominator):
            percent = (num / deno) * 100
            print(
                f"You got {num} questions right out of {deno}, so you got a {percent:.2f}%."
            )


while True:
    clear()

    # introduction
    print(
        """Based on your test score, I will find find out
how many questions are on the test, and 
how many you missed.
However, I need an estimate of how many questions were
on the test. Please enter your lower and higher guess below.
"""
    )

    # indexes are synced -> percent = numerator[1] / denominator[1], etc
    numerator = []  # num correct
    denominator = []  # total questions

    # user inputs
    minGuess = pyip.inputInt("Lower guess of number of questions: ", min=1)
    maxGuess = pyip.inputInt("Higher guess of number of questions: ", min=1)
    score = pyip.inputNum("Your score: ", min=0, max=100)

    # makes sure the min and max are not flipped
    if minGuess > maxGuess:
        minGuess, maxGuess = maxGuess, minGuess

    findScores()
    results()

    again = pyip.inputYesNo("Try again? [y/n] ")
    if again == "no":
        break
