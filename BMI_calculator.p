def calculator():
    bmi = weight / height ** 2
    if bmi < 18.5:
        print("Warning! UNDERWEIGHT")
    elif bmi > 18.5 < 24.9:
        print("NORMAL WEIGHT")
    elif bmi > 25 < 30:
        print("Warning! UNDERWEIGHT")
    elif bmi > 30:
        print("Warning! OBESE")
    

while True:
    print("---BMI CALCULATOR---")
    option = input("Enter '1' to calculate your BMI and 'Q' to quit: ").upper()
    if option == "1":
        weight = float(input("Pls enter your weight in kg: "))
        height = float(input("Pls enter your height in m: "))
        calculator()
    elif option == "Q":
        print("Exiting........\n Exited")
        break
    else:
        print("invalid input")