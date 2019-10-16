"""

S04Q02
     - Brilliant School sets an exam wherein, 
                English exam is for 80 marks, 
                Science for 90 marks and 
                Mathematics for 100 marks. 

            Ask the student to enter the marks scored in each of these exams. 
            Calculate the total percentage marks and rank the student as below :
               - First Class if score is more than or equal to 90 %
               - Second Class if score is more than or equal to 75%
               - Average if student has not failed
               - Failed if score is less than or equal to 35 %

"""
def add (a,b,c):
    return(a + b + c)

def division(a):
    return (a / 270)

def user_output(a,b,c,d,e):
    print("english: science: mathematics: total: persentage:")
    print(" ",a,"     ",b,"       ",c,"     ",d,"    ",(e),"%") 
    

def main():
    
    x = int(input("enter your scored english marks the maximum marks is 80 ="))
    y = int(input("enter your scored science marks the maximum marks is 90 ="))
    z = int(input("enter your scored mathematics marks the maximum marks is 100 ="))
    n = add(x, y, z)
    m = int(division(n)*100)
    if x <=80 and y <= 90 and z <= 100:
        if x >= 29 and  y >= 33 and  z >= 36 :
            if m >= 90:
                print("first class with",(m),"%")
                user_output(x,y,z,n,m)
            elif m >= 75:
                print("second class with",(m),"%")
                user_output(x,y,z,n,m)
            elif m >= 36:
                print("average with",(m),"%")
                user_output(x,y,z,n,m)
        else :
            print("failed with",(m),"%")
            user_output(x,y,z,n,m)
            
    else:
        print("user entered more than maximum marks")

main()
        
    
    
    
    
    
