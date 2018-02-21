a = raw_input("Enter the Character : ")
b = ['a','e','i','o','u']
if(a.isalpha() and a != " "):
  if(a in b):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Invalid Input")
