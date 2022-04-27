# monthNameConverter = {
#     "jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "Jun",
#     "Jul": "July",
#     "Aug": "August",
#     "Nov": "November",
#     "Dec": "December"
# }
# # first way to get access;
#
# print(monthNameConverter["Mar"])
# # another way to access
# print(monthNameConverter.get("Jul"))
#
#

# gussing games
my_Secret_word = "Khan"
guess_word = ""
guess_max_try = 3
guess_left = 0
out_of_guess = False

while guess_word != my_Secret_word and not(out_of_guess):
    print("You have let " + str(guess_max_try - guess_left) + " of try, Please this game is case sensitive")
    if guess_left < guess_max_try:
        guess_word = input("Enter your guess word: ")
        guess_left += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You lose the game")
else:
    print("You win")