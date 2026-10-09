WEIGHT = float(input("Enter your weight(in kg): "))
if WEIGHT >=0:
    HEIGHT= float(input("Enter your Height (in m): "))
    if HEIGHT >=0:
        PORDERAL =  ( WEIGHT/(HEIGHT**3))
        print("Your Porderal is", PORDERAL)
    else:
        print("Invalid Height")
else:
    print("Invalid Weight")
