from os import name


#Read character status (Hp and ATK)
def get_status(character):
    result = []
    with open("./data/status.txt", "r") as file:
        for line in file:
          line_as_list = line.split(",")
          name = line_as_list[0]
          hp = int(line_as_list[1])
          atk = int(line_as_list[2].strip())
          if name == character:
              result.append(hp)
              result.append(atk)
    return result

def get_history():
    result = []
    with open("./data/history.txt", "r") as file:
        for line in file:
          line_as_list = line.split(",")
          prompt = line_as_list[0]
          histoty = int(line_as_list[1].strip())
          result.append([prompt, histoty])
    return result

def update_history(winOrLose):
    history = get_history()
    prompt_win = history[0][0]
    win = int(history[0][1])
    prompt_lose = history[1][0]
    lose = int(history[1][1])
    if winOrLose == "win":
        win += 1
    elif winOrLose == "lose":
        lose += 1
    with open("./data/history.txt", "w") as file:
        file.write(prompt_win + ", " + str(win) +"\n")
        file.write(prompt_lose + ", " + str(lose))
    print(win, lose)

# update_history("win")


