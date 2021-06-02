a,b,c = map(int,input("Enter Three Number Spe by ' ' : ").split())
if a < b:
    if b < c:
        print(c,'is gratest number out of given three')
    else:
        print(b,'is gratest number out of given three')
else:
    if a < c:
        print(c,'is gratest number out of given three')
    else:
        print(a,'is gratest number out of given three')