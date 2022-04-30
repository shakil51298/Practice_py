
def my_translator(word):
    translation = ""
    for character in word:
        if character.lower() in "aeiou":
            if character.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + character
    return translation
print(my_translator(input("please enter a word: ")))

# shakil = "SHAKIL"
# print(shakil.upper())





