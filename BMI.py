WEIGHT = float(input("Enter your weight(in kg): "))
if WEIGHT >=0:
    HEIGHT= float(input("Enter your Height (in m): "))
    if HEIGHT >=0:
        BMI =  ( WEIGHT/(HEIGHT*HEIGHT))
        print(BMI)
    else:
        print("Invalid Height")
else:
    print("Invalid Weight")
if BMI< 18.5:
    print("You fall in Underweight catagory")
elif BMI<=24.9:
    print("You fall in Normal catgory")
elif BMI<=29.9:
    print("You lie in Overweight catagogy")
elif BMI<= 34.9:
    print("You fall in Obese Class 1 catagory")
elif BMI <= 39.9:
    print("You fall in Obese Class 2 catagory")
else:
    print("You fall in Obese Class 3 catagory")    