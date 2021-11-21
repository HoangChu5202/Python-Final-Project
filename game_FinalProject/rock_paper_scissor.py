import random 

def ranChoice(choices):
    return random.choice(choices)

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

def rk_pr_sr(choice):
    choices = ["ROCK","PAPER","SCISSOR"]
    compChoice = ranChoice(choices)
    playerChoice = choice
    winner = decideWinner(playerChoice, compChoice)
    print("Player pick:", playerChoice)
    print("Computer pcik:", compChoice)
    
    return winner


