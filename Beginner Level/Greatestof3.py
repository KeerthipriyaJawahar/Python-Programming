a = input("Enter the 1st number: ")
b = input("Enter the 2nd number: ")
c = input("Enter the 3rd number: ")
if(a<0 or a>=0 or b>0 or b<=0 or c>0 or c<=0):
    if(a<b>c):
        print b
    elif(b<c>a):
        print c
    else:
        print a
else:
    print("Invalid Input")
