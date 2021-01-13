n=int (input ("enter"))
n = 5
c = 0
while  c<=9:
    c = c+1
    b = n*c
    x = str(n)+" X "+str(c)+" "
    if len(str(c)) > 1:
    	x = str(n)+" X "+str(c)
    print (x,"=",b)
