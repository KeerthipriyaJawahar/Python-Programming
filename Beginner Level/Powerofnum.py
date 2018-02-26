 a = raw_input("Enter the Number: ")
b=raw_input("Enter the Power: ")
n=1
if(a != "" and b != "" and a.isdigit() and b.isdigit()):
    for i in range(int(b)):
        n=n*int(a)
    print n
else:
    print("Invalid Input")
