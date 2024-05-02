# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import random

OppA=0.05                   ## oppurtunites for team A
OppB=0.05                  ## oppurtunites for team B
OppContested=0.05          ## oppurtunites contested by both teams
Opp=OppA+OppB+OppContested
Cards=0.05

AP=4

Aa=70
Ad=10
Am=10
Ba=5
Bd=10
Bm=10
Team_A_Poss=0   # total scoring oppurtunites of team A
Team_A_Goals=0   # total Goals of team A
Team_B_Poss=0
Team_B_Goals=0   # 
#file2 = open(r"C:\Scratch\zzz.txt","r")
#file2 = open(r"C:\Scratch\zzz.txt","rt")
#print("Output of Readlines after appending") 
#print(file2.readlines())
#print()
#file1.close()

AB_m=Am**3+Bm**3
A_B_a=Aa**AP+Bd**AP
B_A_a=Ba**AP+Ad**AP
Pos_A=Am**3/AB_m
Score_A=0.85*(Aa**AP)/A_B_a
Score_B=0.85*(Ba**AP)/B_A_a

######## If Goal #########
def if_goal(Score_AB):
    goals_team =random.random()
    if Score_AB>goals_team:
        return 1
    else:
        return 0
####################
######## Team Oppurtunites #########
def team_possessions(event):
    global Team_A_Poss, Team_B_Poss
    global Team_A_Goals, Team_B_Goals
    if OppA>event:
        print("A")    
        Team_A_Poss=Team_A_Poss+1
        goals=if_goal(Score_A)
        Team_A_Goals=Team_A_Goals+goals
    elif OppB+OppA>event:
        print("B")
        Team_B_Poss=Team_B_Poss+1
        goals=if_goal(Score_B)
        Team_B_Goals=Team_B_Goals+goals
        
####
for min in range(1,91):             #start of a match
    event=random.random()

    if Opp>event:
        print(event,end=" ")
        team_possessions(event)

        Att_team =random.random()
    # if Pos_A>Att_team:
    #     Team_A_Poss=Team_A_Poss+1
    #     goals=if_goal(Score_A)
    #     Team_A_Goals=Team_A_Goals+goals
    # else: 
    #     Team_B_Poss=Team_B_Poss+1
    #     goals=if_goal(Score_B)
    #     Team_B_Goals=Team_B_Goals+goals

        
##########################################           
# for x in range(1, 9):
#   print(x,end=" "),
#   print(random.randint(0,99),end=" "),
#   print(Pos_A,end=" "),print(Score_A),
print ("Team A Chances", Team_A_Poss,end=" ")
print ("Team A Goals", Team_A_Goals)
print ("Team B Chances", Team_B_Poss,end=" ")
print ("Team B Goals", Team_B_Goals)
print("ee")
        #print (round(event,3),end=" ")
        #print (Opp,end=" ")
        #print (round(Att_team,3),end=" ")
        #print (Pos_A,end=" ")
                    # goals_team =random.random()
            # if Score_A>goals_team:
            #     Team_A_Goals=Team_A_Goals+1    