a,b,c = map(int,input("Enter Three Number Spe by ' ' : ").split())
if a < b:
    if a < c:
        print(a,'is smallest number out of given three')
    else:
        print(c,'is smallest number out of given three')
else:
    if b < c:
        print(b,'is smallest number out of given three')
    else:
        print(c,'is smallest number out of given three')