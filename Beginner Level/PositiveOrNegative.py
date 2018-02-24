a = raw_input("Enter the Integer:")
if(a.isdigit() and a != " "):
    if(a>0):
        print("Positive")
    elif(a<0):
        print("Negative")
    else:
        print("Zero")
else:
    print("Invalid Input")
