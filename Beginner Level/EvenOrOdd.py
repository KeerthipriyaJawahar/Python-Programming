a = raw_input("Enter the number:")
if(a.isdigit() and a != " "):
    b = int(a)
    if(b%2==0):
        print("Even")
    else:
        print("Odd")
else:
    print("Invalid Input")
