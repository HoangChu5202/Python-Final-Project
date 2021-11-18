from helper import getNum

# STEP 5: Define a function called drawBoard that takes one parameter, a 2-dimensional array called board
def drawBoard(board): 
  print(board[0][0], " | ", board[0][1], " | ", board[0][2])
  print(board[1][0], " | ", board[1][1], " | ", board[1][2])
  print(board[2][0], " | ", board[2][1], " | ", board[2][2])
    # STEP 6: Print the values of the board array parameter, formatting the output to look like a tic-tac-toe board
    # Example: 
    # 0 | 1 | 2
    # ---------
    # 3 | 4 | 5
    # ---------
    # 6 | 7 | 8

def switchPlayer(player): # STEP 8: Define a function called switchPlayer that takes one parameter, a string called player
    # STEP 9: Write an if-else statement (or ternary operator) to change the player from "X" to "O", and vice versa.
    if player == "O":
      player = "X"
    else:
      player = "O"
    print("The current player is ", player) # STEP 10: Print a message indicating who the current player is.
    # STEP 11: Return the player variable.
    return player

def markBoard(board, player, location): # STEP 14: Define a function called markBoard that takes three parameters, a 2-dimensional array called board, a string called player, and an integer called location.
    # STEP 15: Assign False to a variable called marked
    marked = False
    row, col = getLocation(location) # STEP 20: Call the getLocation function, passing the location parameter as an argument. Assign the result to the variables row and col (comma separated)
    # STEP 21: Write an if-else statement that checks if the board variable doesn't already have an "X" or "O" assigned to the row and col selected. If true, assign the player variable to that space and assign True to the variable called marked. If false, print a message saying that location has already been marked.
    if (board[row][col] != "X") and (board[row][col] != "O"):
      board[row][col] = player
    else:
      marked = True
    return marked # STEP 16: Return the marked variable.

# STEP 17: Define a function called getLocation that takes one parameter, an integer called location.
def getLocation(location):
    row = location // 3
    col = location % 3
    # STEP 18: Create two variables row and col. Write the code needed to col determine the row and column that the player chose. For example: 
    # 0 => row 0, col 0
    # 1 => row 0, col 1
    # 2 => row 0, col 2
    # 3 => row 1, col 0
    # 4 => row 1, col 1
    # 5 => row 1, col 2
    # 6 => row 2, col 0
    # 7 => row 2, col 1
    # 8 => row 2, col 2
    # STEP 19: Return the row and col variables (comma separated)
    return row, col
def checkWinner(board, player): # STEP 24: Define a function named checkWinner that takes two parameters, a 2-dimensional array called board and a string called player.
    # STEP 25: Assign False to a variable called winner
    winner = False
    # STEP 27: Write an if statement to check if there are 3 consecutive matching board values. For example, there are 8 different combinations to win: [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], and [2, 4, 6]. If true, call the drawBoard function, passing the board variable as an argument, print a message to congratulate the current player, and assign True to the winner variable.
    for row in range(3):
      if board[row][0] == board[row][1] == board[row][2]:
        winner = True
    for col in range(3):
      if board[0][col] == board[1][col] == board[2][col]:
        winner = True
    if board[0][0] == board[1][1] == board[2][2]:
      winner = True
    if board[0][2] == board[1][1] == board[2][0]:
      winner = True
    return winner 
    # STEP 26: Return the winner variable.

def checkTie(board):
  count = 0
  tie = False
  for row in range(3):
    for col in range(3):
      if (board[row][col] == "X") or (board[row][col] == "O"):
        count += 1
  if count == 9:
    tie = True
  return tie

def main():
    # STEP 1: Assign a 2-dimensional array with 3 rows and 3 columns to a variable called board. Assign numbers 0-2 to the first row, 3-5 to the second row, and 6-8 to the third row.
    board = [[0,1,2],
             [3,4,5],
             [6,7,8]]
    # STEP 2: Assign the string "O" to a variable called currentPlayer
    currentPlayer = "O"
    # STEP 3: Assign False to a variable called gameOver
    gameOver = False
    # STEP 4: Write a while loop that will run continuously if the gameOver variable is false.
    while gameOver == False:
        # STEP 7: Call the drawBoard function, passing the board variable as an argument. No value will be returned.
        drawBoard(board)
        # STEP 12: Call the switchPlayer function, passing the currentPlayer variable as an argument. Assign the result returned from the function back to the currentPlayer variable.
        currentPlayer = switchPlayer(currentPlayer) 
        # STEP 13: Using the Helpers getNum function, prompt the current player for a number between 0 and 8. Give them an infinite amount of attempts. Convert the numerical input to an integer. Assign the player's response a variable named choice.
        choice = getNum("What number you want to mark?", 0, 8, 1, True)
        # STEP 21: Create an infinite while loop
        while True:
            # STEP 22: Call the markBoard function, passing the board, currentPlayer, and choice variables as parameters. Assign the result returned from the function to a marked variable.
            marked = markBoard(board, currentPlayer, choice) 
            # STEP 23: Write an if-else statement that checks if the marked variable is True. If true, break out of the loop. If false, prompt the current player for another number between 0 and 8. Assign the player's response a variable named choice.
            if marked == False:
              break
            else:
              choice = getNum("This one already marked. Please select other one", 0, 8, float("inf"), True)
        # STEP 28: Call the checkWinner function. Pass the board array and the currentPlayer variables to the function. Assign the result returned to the gameOver variable.
        gameOver = checkWinner(board, currentPlayer) 
        if gameOver == True:
          drawBoard(board)
          print("Player", currentPlayer, "won")
        tie = checkTie(board)
        if tie == True:
          gameOver = True
          drawBoard(board)
          print("Tie!!!Congratulation both of you!!!")

main()