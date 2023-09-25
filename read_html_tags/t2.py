strlist=[]
z=1
while z==1:
    a = input("Enter a string (y=stop): ")
    if a == 'y':
        break
    else:
        ab = False
        xy = False

        for i in a:
            if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                ab = True
            if i in '0123456789':
                xy = True

        if ab and xy:
            strlist.append(a)
            print("This is an alphanumeric string.")
        elif ab:
            strlist.append(a)
            print("This is an alphabetic string.")
        elif xy:
            print("This is a numeric sorry")
        else:
            
            print("This is neither alphabetic nor numeric.")
print(strlist)
