a = raw_input("Enter Integer: ")
if(a.isdigit() and a != ""):
    count = 0
    while(a>0):
        a = int(a)/10
        count+=1
    print count
else:
    print("Invalid Input")
