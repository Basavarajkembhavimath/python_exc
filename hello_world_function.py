
S01AQ01
"""
Modify the first “Hello World” program to prompt for user’s name 
           and then wish the user by saying Hello followed by his name

           Example :
           If user's name is Sam, then expected output is :
           Hello Sam !!!
"""

def say_hello(x):
    print("hello", x,  "!!!")

def user_input():
    x = input("enter")
    return x
def for_loop(a,b):
    for i in range(b):
        say_hello(a)
def main ():
    x = user_input()
    n = int(user_input())
    for_loop(x,n)

#main starts from here

main()
    
