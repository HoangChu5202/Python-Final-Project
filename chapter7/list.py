letters = ["a","b"]
letters.extend(["c","d"]) #extend():  Adds the list passed in as a parameter onto the end of the first list. This can also be accomplished using +=
print(letters) # ['a', 'b', 'c', 'd']
letters += ["e", "f"]
print(letters) # ['a', 'b', 'c', 'd', 'e', 'f']

letters.insert (0,"$")
letters.insert (4,"$") #insert(): Inserts a specific element at the list index location specified in the first argument inside the parentheses.
print(letters) # ['$', 'a', 'b', 'c', '$', 'd', 'e', 'f']

letters.remove("$") #remove(): Removes only the first instance of the element specified inside of the parentheses; can be combined with a while loop to remove multiple instances of an element in a list.
print(letters) # ['a', 'b', 'c', '$', 'd', 'e', 'f']

del letters[2] #del: Removes an element from a specific index, regardless of what element is stored at that index
print(letters) # ['a', 'b', '$', 'd', 'e', 'f']




letter_removed = letters.pop(0) #pop(): Removes an element located at the index number given inside the parentheses. It also returns the element that was removed. When used without any arguments, pop() removes and returns the last element in a list.
print(letter_removed) # 'a'
letter_removed = letters.pop()
print(letter_removed) # 'f'
print(letters) # ['b', '$', 'd', 'e']

letters.reverse() #Flip the order
print(letters) # ['e', 'd', '$', 'b']

letters.sort(reverse=True) #sort(): String elements are put into alphabetical order (Python coverts characters to binary and compares values) and numerical elements are put into numerical order.
                           #Note: To order a list from the highest value to the lowest, the reverse=True argument can be added between the parentheses.
print(letters) # ['e', 'd', 'b', '$']

letters.sort()
print(letters) # ['$', 'b', 'd', 'e']