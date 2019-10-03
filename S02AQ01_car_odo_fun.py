"""
2
S02AQ01
Re-write the earlier question of S02Q02 using functions :

     - Using the starting and ending values of your car’s odometer, 
            calculate its mileage

"""

def substraction(a, b):
    substraction = (a - b)
    return substraction

def division(a, b):
    division = (a / b)
    return division

def user_input():
    a = int(input("enter the starting value"))
    e = int(input("enter the ending value"))
    tank_capacity = 26
    d = 560
    return a,e,tank_capacity,d
      
def main ():
    v,w,x,z = user_input()
    mileage = division(substraction(w, v),x)
    print("your car mileage is =", mileage,"kmh")


#main program starts from here

main()
    
                      
                      
                      
                              
    

