def create_cast_list(file_name):
    result = []
    with open(file_name, "r") as file:
        count = 0
        for line in file:
            if(count > 0):
                line_as_list = line.split(",")
                actor = line_as_list[5]
                character = line_as_list[4]
                result.append(actor + "," + character)
            count += 1
    return result

def write_cast_to_file(list, file_name):
    with open(file_name, "w") as file:
        count = 0
        for line in list:
            result = line
            count += 1
            if(count != len(list)):
                result += "\n"
            file.write(result)

cast_list = create_cast_list("./chapter6/The Office cast.csv")
cast_list.sort()
write_cast_to_file(cast_list, "./chapter6/office_actors.csv")
