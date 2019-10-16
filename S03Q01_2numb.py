def user_input():
    n = int(input("enter your number"))
    return n

def main():
    x = user_input()
    if x>=100 and x < 1000:
        print("this is three digit number")
    elif x >=10 and x <= 99:
        print("x  is two digit number")
    elif x >0  and x <= 9:
        print("x  is one digit number")
    else:
        print("x is not a two digit or three digit number =",x)


main()

