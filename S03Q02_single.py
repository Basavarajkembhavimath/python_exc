"""
 Ask the user to enter a number.
            - If the number is a single digit number,
                 add 7 to it, and print the number in its unit’s place
            - If the number is a two digit number,
                raise the number to the power of 5, 
                and print the number in its unit’s place
            - If the number is a three digit number, 
                ask the user to enter another number. 
                Add the 2 numbers and print the number in its unit’s place

"""

def user_input():
    x = int(input("enter your number"))
    return x

def add(a, b):
    return (a + b)

def modlous(a):
    print(a % 10)

def power( a ):
    return (a ** 5)

def main():

    m = 7
    y = user_input()

    if y <= 9:
        s = add(y,m)
        modlous(s)

    elif y >= 10 and y <= 99:
        t = power(y)
        modlous(t)

    elif y >= 100 and y < 1000:
        z = user_input()
        w = add(y, z)
        modlous(w)
    else:
        print ("your number is more then 3 digit")
        
        
        
    


main()

