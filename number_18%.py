"""
S04Q01

A Chemical plant has a tank for storing ethanol.
            - When the tank is more than 80% full, it
                 should raise an alarm to close the valve.
            - When the tank is less than 20% full, it
                 should send an SMS to buy more liquid.
            - The total tank capacity is 900 litres.
            - Write a program to simulate this.
            - Ask user to enter current level of ethanol in the tank.
            - Print the appropriate action based on value entered
            - Make sure that your program needs minimum changes
                 for a tank of different capacity.


def user_input():
    x = int(input("enter the current level of ethanol liquid"))
    return x

def divide(a, b):
    return(a / b)
    
def  main():
    z = 900
    y = user_input()
    t = divide(y, z)*100
    if t >= 80:
        print("your tank is full please close the valve")
    elif t <= 20 :
        print("your tank is going to empty please fill more liquid")
    else:
        print(" your tank has ",int(t),"% no need to fill")


main()


"""
#its for different tank capacity

def user_input():
    v = int(input("enter your tank capacity"))
    x = int(input("enter the current level of ethanol liquid"))
    
    return v, x

def divide(a, b):
    return(a / b)
    
def  main():
    y, z = user_input()
    if y >= z:
        t = divide(z, y)*100
        if t >= 80:
            print("your tank is ",int(t),"% full please close the valve")
        elif t <= 20:
            print("your tank is",int(t),"% going to empty please fill more liquid")
        else:
            print(" your tank has ",int(t),"% no need to fill")

    else:
        print("wrong value: tank capacity is always  more then current level")


main()

