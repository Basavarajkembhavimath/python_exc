
"""
S01AQ03
     - Modify program in S01Q02 to print the multiplication table 
           of any number desired by the user

"""

def user_input():
   x = 17
   return (x)

def multiplication(a, b):
    return (a * b)

def main():
    m = user_input()
    for i in range(1, 11):
        n = i
        y = multiplication(m, i)
        print("your multplication number is =", m, "x", n, "=", y)


#main starts here
main()




