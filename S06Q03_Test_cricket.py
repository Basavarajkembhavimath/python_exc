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

Batsman1 = []
Single1 = []
Two_runs1 = []
Tree_runs1 = []
Fours1 = []
Sixes1 = []
Balls1 = []
Dot_balls1 = []
all_runs = []
ovr = 0
over = []
overs = {}
out = 0 
def run():
    runs = input("Enter the run : ")
    return runs

def main(count, out, ovr):
    
   
    def main1(count, out, ovr):
        while True:
            if count == 6:
                ovr += 1
                count = 0
                print(str(ovr)+' '+'Over Completed')
                overs[str(ovr)] = over
                print(overs)
                over.clear()
                main(count, out, ovr)
                break
            
            if out == 0:
                runs = input("Enter the run : ")
            if not runs:
                out += 1
                Balls1.append(1)
                print('Batsman1',b,': OUT' )
                over.append('OUT')
                count +=1
                main(count, out, ovr)
                break
            
            if runs == '.':
                print("1.Ohh Dot ball")
                Batsman1.append(0)
                Dot_balls1.append(1)
                all_runs.append(0)
                Balls1.append(1)
                over.append('0')
                count += 1
                
            elif int(runs) == 6:
                print("1,WOW IT'S SIX")
                Batsman1.append(int(runs))
                Sixes1.append(int(runs))
                all_runs.append(int(runs))
                Balls1.append(1)
                over.append(runs)
                count +=1
                
            elif int(runs) == 4:
                print("1,Its a Four")
                Batsman1.append(int(runs))
                Fours1.append(int(runs))
                all_runs.append(int(runs))
                Balls1.append(1)
                over.append(runs)
                count += 1
            
            elif int(runs) == 3:
                print("1,Three Runs")
                Batsman1.append(int(runs))
                Tree_runs1.append(int(runs))
                all_runs.append(int(runs))
                Balls1.append(1)
                over.append(runs)
                count += 1
                main(count, out, ovr)
                break
            
            elif int(runs) == 2:
                print("1,Two Runs")
                Batsman1.append(int(runs))
                Two_runs1.append(int(runs))
                all_runs.append(int(runs))
                Balls1.append(1)
                over.append(runs)
                count += 1
            
            elif int(runs) == 1:
                print("1,Single Run")
                Batsman1.append(int(runs))
                Single1.append(int(runs))
                all_runs.append(int(runs))
                Balls1.append(1)
                over.append(runs)
                count += 1
                main(count, out, ovr)
                break
                
            elif int(runs) < 0 or int(runs) ==5 or int(runs) > 6:
                print("1.Invalid!, Please enter the valid Runs :")  

            else:
                break
    
    
    if out == 0:
        while True:
            
            if count == 6:
                ovr += 1
                count = 0
                print(str(ovr)+' '+' Over Completed')
                overs[str(ovr)] = over
                print(overs)
                over.clear()
                main1(count, out, ovr)
                
            runs = run()
            if not runs:
                Balls.append(1)
                print('Batsman',a, ': OUT ')
                over.append('OUT')
                count +=1
                out += 1
                
                break
            
            elif runs == '.':
                print("Ohh Dot ball")
                Batsman.append(0)
                Dot_balls.append(1)
                all_runs.append(0)
                Balls.append(1)
                over.append('0')
                count += 1
                
                
            elif int(runs) == 6:
                print("WOW IT'S SIX")
                Batsman.append(int(runs))
                Sixes.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                over.append(runs)
                count +=1
                
                
            elif int(runs) == 4:
                print("Its a Four")
                Batsman.append(int(runs))
                Fours.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                over.append(runs)
                count += 1
                
            elif int(runs) == 3:
                print("Three Runs")
                Batsman.append(int(runs))
                Tree_runs.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                over.append(runs)
                count += 1
                
                main1(count, out, ovr)

            elif int(runs) == 2:
                print("Two Runs")
                Batsman.append(int(runs))
                Two_runs.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                over.append(runs)
                count += 1
                

            elif int(runs) == 1:
                print("Single Run")
                Batsman.append(int(runs))
                Single.append(int(runs))
                all_runs.append(int(runs))
                Balls.append(1)
                over.append(runs)
                count += 1
                
                main1(count, out, ovr)

            elif int(runs) < 0 or int(runs) ==5 or int(runs) > 6:
                print("Invalid!, Please enter the valid Runs :")  

            
    print("")
    print (over)
    print("Great well played here is your score detais : \n")
    print("Batsman     :",a)
    print("Total_score :",sum(Batsman))
    print("Ball_forced :",sum(Balls))
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




main(0,0,0)
            
