dictionary = {
    "LMM" : "i am about to lose my mind",
    "IND" : "i need a doctor",
    "CMD" : "call me a doctor",
    "BMBL": "to bring me back to life",
    "EM" : "eminem",
}
while True:
    key = input("Enter a key: ")

    if key in dictionary:
        print(dictionary[key])
    else:
        print(":((")        
        ask = input("do you want to enter a new explan?(Y/N)") .upper()    
        if ask == "N":
            print(":))")
        else:
            explan = input("enter a new explan: ")
            dictionary[ask] = explan
            print(dictionary)




