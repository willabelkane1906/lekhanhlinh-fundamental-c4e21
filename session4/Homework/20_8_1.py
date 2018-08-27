from collections import Counter
text = input("enter a text:").lower()
letters = {}
for i in list(text): 
        letters[i] = list(text).count(i)
del letters[" "]
for k in sorted(letters):
    print (k + ': ' + str(letters[k]))

   

