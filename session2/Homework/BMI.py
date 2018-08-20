height = float(input("Input your height in centimeters: "))
weight = float(input("Input your weight in kilogram: "))
m_height = height * 0.01
bmi = weight / (m_height * m_height)
print("Your body mass index is: ", bmi)

if bmi < 16:
    print(" you are severely underweight.")
elif bmi > 16 and bmi < 18.5:
    print(" you are underweight.")        

elif bmi > 18.5 and bmi < 25:
    print(" you are normal.")

elif bmi > 25 and bmi < 30:
   print("you are overweight.")

elif bmi > 30:
    print(" you are obese.")

else:
     print("There is an error with you inputput")
       



