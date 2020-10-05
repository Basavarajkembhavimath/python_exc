"""
S06Q03 : Beach Cricket Match
     - Collect the names of the 2 batmen currently playing. 
              Who among them is currently at the non striker’s end ?
          - Collect runs scored for each ball. 
              Make sure, you accumulate runs for the correct player 
                   based on who is facing the ball.
          - Remember that players change positions at the end of each over. 
          - The match ends after 30 balls, or 
               - if any batsman scores more than 60 runs.
          - Print all the statistics for each batsman 
               as was done for the earlier T20 match [ S06Q02 ]
               
"""
a = input("Enter the First Batsman Name : ")
b = input("Enter the Second Batsman Name : ")

Batsman = []
Single = []
Two_runs = []
Tree_runs = []
Fours = []
Sixes = []
Balls = []
Dot_balls = []
count = 0
count1 = 0

dict = {}
Batsman1 = []
Single1 = []
Two_runs1 = []
Tree_runs1 = []
Fours1 = []
Sixes1 = []
Balls1 = []
Dot_balls1 = []
all_runs = []
over = 0
out = 0 
def run():
    runs = input("Enter the run : ")
    return runs

def main(count,count1, out, over):
    
   
    def main1(count, count1,out, over):
        while True:
            runs = input("Enter the run : ")
            if not runs:
                out += 1
                Balls1.append(1)
                print('Batsman1',b,': OUT' )
                count +=1
                main(count,count1, out, over)
                break
            if count == 6:
                over += 1
                count = 0
            if count < 30 or all_runs[-1] == 0 or all_runs[-1] == 3 or all_runs[-1] == 1:
                count1 = 0
                
                if runs == '.':
                    print("1.Ohh Dot ball")
                    Batsman1.append(0)
                    Dot_balls1.append(1)
                    all_runs.append(0)
                    Balls1.append(1)
                    count += 1
                    
                elif int(runs) == 6:
                    print("1,WOW IT'S SIX")
                    Batsman1.append(int(runs))
                    Sixes1.append(int(runs))
                    all_runs.append(int(runs))
                    Balls1.append(1)
                    count +=1
                    
                elif int(runs) == 4:
                    print("1,Its a Four")
                    Batsman1.append(int(runs))
                    Fours1.append(int(runs))
                    all_runs.append(int(runs))
                    Balls1.append(1)
                    count += 1
                
                elif int(runs) == 3:
                    print("1,Three Runs")
                    Batsman1.append(int(runs))
                    Tree_runs1.append(int(runs))
                    all_runs.append(int(runs))
                    Balls1.append(1)
                    count += 1
                    main(count,count1, out,over)
                    break
                
                elif int(runs) == 2:
                    print("1,Two Runs")
                    Batsman1.append(int(runs))
                    Two_runs1.append(int(runs))
                    all_runs.append(int(runs))
                    Balls1.append(1)
                    count += 1
                
                elif int(runs) == 1:
                    print("1,Single Run")
                    Batsman1.append(int(runs))
                    Single1.append(int(runs))
                    all_runs.append(int(runs))
                    Balls1.append(1)
                    count += 1
                    main(count,count1, out,over)
                    break
                    
                elif int(runs) < 0 or int(runs) ==5 or int(runs) > 6:
                    print("1.Invalid!, Please enter the valid Runs :")  

     
    
    if out != 1:
        
        while True:
            runs = run()
            if not runs:
                Balls.append(1)
                print('Batsman',a, ': OUT ')
                count +=1
                break
            if count1 == 6:
                main1(count,count1,out,over)
            
            elif runs == '.':
                print("Ohh Dot ball")
                Batsman.append(0)
                Dot_balls.append(1)
                all_runs.append(0)
                Balls.append(1)
                count += 1
                count1 +=1
                
            elif int(runs) == 6:
                print("WOW IT'S SIX")
                Batsman.append(int(runs))
                Sixes.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                count +=1
                count1 +=1
                
            elif int(runs) == 4:
                print("Its a Four")
                Batsman.append(int(runs))
                Fours.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                count += 1
                count1 +=1
                
            elif int(runs) == 3:
                print("Three Runs")
                Batsman.append(int(runs))
                Tree_runs.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                count += 1
                count1 +=1
                main1(count, count1, out, over)

            elif int(runs) == 2:
                print("Two Runs")
                Batsman.append(int(runs))
                Two_runs.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                count += 1
                count1 +=1

            elif int(runs) == 1:
                print("Single Run")
                Batsman.append(int(runs))
                Single.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                count += 1
                count1 +=1
                main1(count, count1, out, over)

            elif int(runs) < 0 or int(runs) ==5 or int(runs) > 6:
                print("Invalid!, Please enter the valid Runs :")  

    print("")
    
    print("Great well played here is your score detais : \n")
    print("Batsman     :",a)
    print("Total_score :",sum(Batsman))
    print("Ball_forced :",sum(Balls))
    print('Total_over  :',float(over))
    print("Dot Balls   :",sum(Dot_balls))
    print("Single_runs :",Single)
    print("Two_runs    :",Two_runs)
    print("Thre_runs   :",Tree_runs)
    print("Fours       :", Fours)
    print("Sixes       :",Sixes)
    print("Stike_rate  :",sum(Batsman)*100/sum(Balls))

    print("Batsman1     :",b)
    print("Total_score1 :",sum(Batsman1))
    print("Ball_forced1 :",sum(Balls1))
    print("Dot Balls1   :",sum(Dot_balls1))
    print("Single_runs1 :",Single1)
    print("Two_runs1    :",Two_runs1)
    print("Thre_runs1   :",Tree_runs1)
    print("Fours1       :", Fours1)
    print("Sixes1       :",Sixes1)
    print("Stike_rate1  :",sum(Batsman1)*100/sum(Balls1))

main(0,0,0,0)
            
