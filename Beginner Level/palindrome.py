a = raw_input("Enter the number: ")
if(a != "" and a.isdigit()):
    b=int(a)
    a=int(a)
    r=0
    if(a<=1000):
        while(a>0):
            c=a%10
            r = r*10+c
            a=a/10
        if(b==r):
            print("Yes")
        else:
            print "No"
    else:
        print "Invalid Input"
else:
    print("Invalid Input")
