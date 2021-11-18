import random 

def ranChoice(choices):
    return random.choice(choices)

def getChoice():
    possibleChoice = ["ROCK", "PAPER", "SCISSOR", "R", "P", "S"]
    while True:
        playerChoice = input("What is your choice? [Rock, Paper, Scissor] or [r, p, s]: ").upper().strip()
        if playerChoice in possibleChoice:
            break
        else:
            print("Value not recognize! Please pick agian!")
    if playerChoice.upper().strip() == "R":
            playerChoice = "ROCK"
    elif playerChoice.upper().strip() == "P":
            playerChoice = "PAPER"
    elif playerChoice.upper().strip() == "S":
            playerChoice = "SCISSOR"   
    return playerChoice

def decideWinner(player, computer):
    if player == computer:
        winner = "Tie"
    else:
        if (player == "ROCK") and (computer == "SCISSOR"):
            winner = "Player"
        elif (player == "ROCK") and (computer == "PAPER"):
            winner = "Computer"
        elif (player == "SCISSOR") and (computer == "PAPER"):
            winner = "Player"
        elif (player == "SCISSOR") and (computer == "ROCK"):
            winner = "Computer"
        elif (player == "PAPER") and (computer == "ROCK"):
            winner = "Player"
        elif (player == "PAPER") and (computer == "SCISSOR"):
            winner = "Computer"
    return winner

def main():
    choices = ["ROCK","PAPER","SCISSOR"]
    compChoice = ranChoice(choices)
    playerChoice = getChoice().upper()
    winner = decideWinner(playerChoice, compChoice)
    print("Player pick:", playerChoice)
    print("Computer pcik:", compChoice)
    if winner == "Tie":
        print(winner)
    elif winner == "Player":
        print(winner, "won")
    else:
        print(winner, "won")
main()