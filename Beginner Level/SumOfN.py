a1 = raw_input("Enter the number: ")
sum = 0
if(a1.isdigit() and a1 != ""):
    for i in range(1,a1+1):
        sum+=i
    print sum
else:
    print("Invalid Input")
