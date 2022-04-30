
def my_translator(word):
    translation = ""
    for character in word:
        if character in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + character
    return translation
print(my_translator(input("please enter a word: ")))





