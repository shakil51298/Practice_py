secret_word = "shakil"
guess = ""
guessingMaxTime = 3
guessTimeLeft = 0
out_of_try_limit = False
while guess != secret_word and not(out_of_try_limit):
    print("u have " + str(guessingMaxTime - guessTimeLeft ) + " time to try more!")
    if guessTimeLeft < guessingMaxTime:
        guess = input("please enter your guessing word: ")
        guessTimeLeft += 1
    else:
        out_of_try_limit = True

if out_of_try_limit:
    print("u lose the game")
else:
    print("you win")