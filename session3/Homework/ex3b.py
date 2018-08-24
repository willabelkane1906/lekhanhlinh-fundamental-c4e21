from random import choice
WORD = ['moksha', 'familia', 'eletric']

word = choice(WORD)
chars = list(word)
chars_len = len(chars)

for i in range(chars_len):
    chars_choice = choice(chars)
    chars.remove(chars_choice)
    print(chars_choice,'', end ="")

ans = input("Your answer:")

if ans == word:
    print("Hura!")
else :
    print(":(")