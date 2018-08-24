from random import choice
word = 'ineedadoctor'
chars = list(word)
chars_len = len(chars)

for i in range(chars_len):
    chars_choice = choice(chars)
    chars.remove(chars_choice)
    print(chars_choice,'', end ="")

trl = input("Your answer:")

if trl == word:
    print("Hura!")
else :
    print(":(")


