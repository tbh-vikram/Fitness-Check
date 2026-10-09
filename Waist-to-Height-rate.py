Waist = float(input("Enter your weight(in m): "))
if Waist >=0:
    HEIGHT= float(input("Enter your Height (in m): "))
    if HEIGHT >=0:
        result =  ( Waist/(HEIGHT))
        print("Your WHtR is", result)
    else:
        print("Invalid Height")
else:
    print("Invalid Weight")
if result<0.4:
    print("Too Low")
elif result<0.49:
    print("Lowe Risk Rate")
elif result<0.59:
    print("Increased Health Risk")
elif result>=0.6:
    print("Hgher Risk")
print("Thank you for using our system")