"""

S06Q02 :
        T20 Cricket Match
     - Collect the runs scored for each ball faced by the batsman. 
              A dot ball is represented by a dot in input. 
              An empty line represents a wicket. 

          - Find the total runs scored by the batsman
          - Find the strike rate of the batsman [ runs scored/balls faced ]
          - Find the number of balls wasted by the batsman
          - How many boundaries and sixes did he score ?


"""

def main():
    a = input("Enter the Name of Batsman : ")
    Batsman = []
    Single = []
    Two_runs = []
    Tree_runs = []
    Fours = []
    Sixes = []
    Balls = []
    Dot_balls = []
    count = 0
    while True:
        runs = input("Enter the run : ")
        if not runs:
            count +=1
            break
        
        elif runs == '.':
            print("Ohh Dot ball")
            Dot_balls.append(1)
            count += 1
            
        elif int(runs) == 6:
            print("WOW IT'S SIX")
            Batsman.append(int(runs))
            Sixes.append(int(runs))
            count +=1
            
        elif int(runs) == 4:
            print("Its a Four")
            Batsman.append(int(runs))
            Fours.append(int(runs))
            count += 1

        elif int(runs) == 3:
            print("Three Runs")
            Batsman.append(int(runs))
            Tree_runs.append(int(runs))
            count += 1

        elif int(runs) == 2:
            print("Two Runs")
            Batsman.append(int(runs))
            Two_runs.append(int(runs))
            count += 1

        elif int(runs) == 1:
            print("Single Run")
            Batsman.append(int(runs))
            Single.append(int(runs))
            count += 1

        elif int(runs) < 0 or int(runs) ==5 or int(runs) > 6:
            print("Invalid!, Please enter the valid Runs :")  

    print("")
    print("Great well played here is your score detais : \n")
    print("Batsman Name :",a)
    print("Total_score  :",sum(Batsman))
    print("Ball_forced  :",count)
    print("Dot Balls    :",sum(Dot_balls))
    print("Single_runs  :",sum(Single))
    print("Two_runs     :",sum(Two_runs))
    print("Thre_runs    :",sum(Tree_runs))
    print("Fours        :", Fours)
    print("Sixes        :",Sixes)
    print("Stike_rate   :",sum(Batsman)*100/count)

            

main()
            
