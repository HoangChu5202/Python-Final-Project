from helper import getString
import random

def get_game_data(file_name):
    result = []
    with open(file_name, "r") as file:
      for line in file:
          line_as_list = line.split(",")
          actor = line_as_list[0]
          character = line_as_list[1].strip()
          result.append([actor,character])
    return result

def ask_question(character, score):
    user_guess = getString("What character did " + character[0] + " play?")
    if(user_guess.lower() == character[1].lower()):
        score += 1
        statement = "That's correct! You have " + str(score)
        statement += " point." if (score == 1) else " points."
        print(statement)
    else:
        print("Incorrect. It was " + character[1] + ".")
    return score

def new_highest_score(score, file_name):
    with open(file_name, "w") as file:
        file.write(str(score))
    print("Congratulations, you beat the highest score!")

def check_highest_score(score, file_name):
    with open(file_name, "r") as file:
        highest_score = int(file.read())
        if(score > highest_score):
            new_highest_score(score, "chapter6/high_score.txt")

def play_game():
    game_data = get_game_data("chapter6/office_actors.csv")
    score = 0
    count = 0
    while(len(game_data) > 0):
        random_character = random.randint(0, len(game_data) - 1)
        character = game_data.pop(random_character)
        score = ask_question(character, score)
        count += 1
    print("Game over. Your final score was " + str(score) + " out of " + str(count) + ".")
    check_highest_score(score, "chapter6/high_score.txt")
    
play_game()