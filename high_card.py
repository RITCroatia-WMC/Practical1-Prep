PLAYER1_WINS = "Player 1 wins!"
PLAYER2_WINS = "Player 2 Wins!"
TIE = "Tie!"

def card_value(rank):
    if rank == "A":
        return 11
    
    if rank == "K" or rank == "Q" or rank == "J":
        return 10
    
    return int(rank)

def high_card_wins(player1_rank,player2_rank):
    player1_value = card_value(player1_rank)
    player2_value = card_value(player2_rank)

    if player1_value > player2_value:
        return PLAYER1_WINS
    
    if player2_value > player1_value:
        return PLAYER2_WINS
    
    return TIE

def main():
    print(high_card_wins("J","10"))

if __name__ == "__main__":
    main()
