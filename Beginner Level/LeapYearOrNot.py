a = raw_input("Enter the Year: ")
if(a != "" and a.isdigit()):
    b=int(a)
    if(b%4==0):
        print "Yes"
    else:
        print "No"
else:
    print("Invalid Input")
