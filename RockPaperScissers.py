import random

ROCK = 0
PAPER = 1
SCISSORS = 2

#prints the output and returns the winner
def print_result(rollPlayer1, rollPlayer2):
  
    if rollPlayer1==0 and rollPlayer2 == 0:
        print("rock\t\trock\t\t0 Draw0")
        return 1
    if rollPlayer1==0 and rollPlayer2 == 1:
        print("rock\t\tpaper\t\tPaper beats rock")
        return 2
    if rollPlayer1==0 and rollPlayer2 == 2:
        print("rock\t\tscissors\t\tRock bears scissors")
        return 1
    if rollPlayer1==1 and rollPlayer2 == 0:
        print("paper\t\trock\t\tPaper beats rock")
        return 1
    if rollPlayer1==1 and rollPlayer2 == 1:
        print("paper\t\tpaper\t\tDraw")
        return 1
    if rollPlayer1==1 and rollPlayer2 == 2:
        print("paper\t\tscissors\t\tScissors bears paper")
        return 2
    if rollPlayer1==2 and rollPlayer2 == 0:
        print("scissors\t\trock\t\tRock bears scissors")
        return 2
    if rollPlayer1==2 and rollPlayer2 == 1:
        print("paper\t\tscissors\t\tScissors bears paper")
        return 1
    if rollPlayer1==2 and rollPlayer2 == 1:
        print("scissors\t\tscissors\t\tDraw")
        return 1

def rock_paper_scissors():
    winnerPlayerCount1=0
    winnerPlayerCount2=0

    #round 1
    rollP1 = random.randint(0,2)
    rollP2 = random.randint(0,2)
    if print_result(rollP1,rollP2)==1:
        winnerPlayerCount1+=1
    else:
        winnerPlayerCount2+=1
    
    #round 2
    rollP1 = random.randint(0,2)
    rollP2 = random.randint(0,2)
    if print_result(rollP1,rollP2)==1:
        winnerPlayerCount1+=1
    else:
        winnerPlayerCount2+=1


        
    #round 2
    rollP1 = random.randint(0,2)
    rollP2 = random.randint(0,2)
    if print_result(rollP1,rollP2)==1:
        winnerPlayerCount1+=1
    else:
        winnerPlayerCount2+=1
    
    print("Player1:", winnerPlayerCount1)
    print("Player2",winnerPlayerCount2)


  
   

def main():
    rock_paper_scissors()

if __name__ == "__main__":
    main()