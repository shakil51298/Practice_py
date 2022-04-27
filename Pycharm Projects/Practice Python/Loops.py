# i = 1
# while i <= 10 :
#     print(i)
#     i += 1
# print("done with while lopp")



# secret wods game

secret_word = "shakil"
guess = ""
guess_left = 0
guess_limit = 3 ;
outOfGuess = False

while guess!= secret_word and not(outOfGuess):
    print("U ahve " + str(guess_limit - guess_left) + " times of try left")
    if guess_left < guess_limit:
        guess = input("enter th guess : ")
        guess_left += 1
    else:
        outOfGuess = True

if outOfGuess:
    print("You lose the game")
else:
    print("You win")