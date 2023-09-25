strlist = []
z = 1
a=0
while z == 1:
    a = input(("Enter a string (y=stop): "))    
    if a == 'y':
        break
    elif a.isnumeric():
        print("sorry -- this is num")
    elif a.isnumeric() or (a.replace(".","1").isdigit()):
        print("sorry -- this is double")
    elif a.isalpha():
        print("alpha string -- stored")
        strlist.append(a)
    elif a.isalnum():
        print("alpha and numeric string -- stored")
        strlist.append(a)
    else:
        print("string -- stored")
        strlist.append(a)
print("Strings:", strlist)

