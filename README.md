# Final Project
This is the final project for my CIS-207 Fundamentals of Web Programming course at [Kirkwood Community College](https://www.kirkwood.edu)
## Introduction
This week I learn about Git, Github and Visual Code. This is my fisrt time to learn it and it really fun.

This is what I learned in GitHub:

    - Create a new project
    - How to add a file from my computer to GitHub
    - How to pull and push a file to GitHub

I also learn some basic thing in markdown too.

## Chapter 1 - Introduction to Computers and Programming
This week I learned about how a computer work, part requied to make a device call a computer.
The way that computer work is:
-   Get input from any input devices.
-   Processing infomation: this will happen in Central processing unit (CPU) and Main memory/Random Access Memory (RAM).
-   Output: This will display result to your output devices, usually is monitor.
I also learned about binary number how to change from demical to binary.

I also know about some popular language like:
- Java
- Html
- Python
- C#
And so on.

## Chapter 2 - Input, Processing, and Output
In this chapter I learned about some basic step when a programer write their code.
Fist they'll read the task and try to see what do they need to do. Then they will create a pseudocode, after that they will draw a flowchart, then they will make a Algorithms.
I aslo learned about some data type like: int, float, string and boolean.
Output(or display), comments and formatting is the next thing that i learned.
To Concatenation 2 string I have to write code like this:

```Python
first_name = "Marc"
last_name = "Hauschildt"
room = 503
print(first_name + last_name + " is staying in room number " + str(room))
```
Anything read by `input()` alway in string data type. If I want to read it as a number I have to write `int(input())` or `float(input())`
Mathematical Operators:
-   \+ plus, - minus,  * multiplication

-   / float division, // integer division, % remainder division

-   ** exponent

Short cut to Increase/Decrease Numerical Variables:
variable += N
"+" can be replace by "-" to Minus or "*" to Mutiple.

## Chapter 3 - Decision Structures
In this chapter we learned about if statement.

```Python
if True:
    # do this
    # then this
    # then this
# The program continues
```
There are 6 Boolean expressions:
- ==    equal to  
- !=     not equal to
- \>=    greater than or equal to
- <=    less than or equal to
- \>      greater than
- <      less than

The next thing we learned is if-else statement and if-elif-else statement.

if-else example: 
```Python
if True:
    # do this
    # then this
    # then this
else:
    # do this
    # then this
    # then this
# The program continues
```
if-elif-else example:
```Python
if True:
    # do this
    # then this
    # then this
elif True:
    # do this
    # then this
    # then this
else:
    # do this
    # then this
    # then this
```

**Logical operators**: The words "and" and "or" can be added to evaluate two or more boolean expressions.
- "and" Both sub-expressions must be true for the compound expression to be true.
- "or"  One or both sub-expressions must be true for the compound expression to be true.
- "not" can be added to a boolean expression to find the opposite.

**Short-circuit Evaluation**: an expression is stopped being evaluated as soon as its outcome is determined. We use short circuit evaluation to prevent errors.
- When using the "or" logical operator, if the first condition is true, the second condition is not tested.
- When using the "and" logical operator, if the first condition is false, the second condition is not tested.

## Chapter 4 - Repetition Structures
In this chapter we learned about while loop and for loop.

**While loop**

- While loop required a count control. If you forget that it will result at an infinite loop.
- While loops are best used when you don't know ahead of time how many times the loop should run.

**For loop**

- For loop is a count control loop. 
- For loops are best used when you know ahead of time how many times the loop should run.

**Range function**

The range function will create a list for you. For example if you write `range(3)` it mean it will create a list for you look like this: `[0, 1, 2]`

**Sentinal**

- A sentinel is a value that signals when there are no more items from a list of items to be processed.
- We can also stop the loop by using `break`

**Input Validation Loops**

- Garbage in, Garbage out
    - ​Python can't tell the difference between good data and bad data being input. You need to write validation loops so that when you take garbage in, you throw the garbage out.
- Numerical Input Validation
    - The integrity of a program's output is only as good as the integrity of the program's input. To trap errors, we use validation loops to keep asking the input question until the user responds correctly.
    - If you request numerical input from the user and they give you a string, the result will be a ValueError exception. In this case we should use `try-except` stament.
- String Input Validation
    - If you request string input from the user any input will be accepted. You can convert the input to lowercase and remove leading/trailing spaces to clean up the input. `.lower()` to convert string to lowercase. `.upper()` to convert string to uppercase. And `.strip()` to remove all extra space.
- Nested Loops
    - You can use a loop inside a loop.

## Chapter 5 - Functions

**Function**

A <u>*function*</u> is a group of statements that exists within a program for the purpose of performing a specific task. In Java, we call them <u>*methods*</u>. Benefits of using functions include:

- Code is simpler to understand
- Less duplicate code (no necessarily less code).
- Code can be reused in multiple programs.
- Fewer errors
- Code is easier to test and debug.
- Facilitates teamwork and collaboration

**Defining a function**

You can make your own function. The code for a function is known as a <u>*function definition*</u>.

 The first line of a function definition is known as the <u>header</u> or <u>signature</u>.  The function header begins with the keyword <u>def</u> and is followed by the name of the function.

 <u>Example</u>:

 ```python
    def function_name():
        statement
        statement
 ```

 **Calling a function**

 To run a function, we call it by using its name with a set of parenthesis. When a function is called by its name it is then executed.

```python
def message():
    print('I am Arthur,')
    print('King of the Britons.')

message()
```

The function don't return anything call a <u>void</u> function.

**Local Variables**

A local variable is a variable created inside a function. It can only be accessed from inside the function. The variable does not persist elsewhere.

**Scope**

The scope of a local variable is the function in which that variable is created. The scope is the part of the program in which a variable may be accessed. A variable is available only to statements in the variable's scope.

**Parameters**

A parameter is a variable that represents required input into a function. Parameters are placed inside the parenthesis of the function header/signature.

Multiple parameters must be separated by commas.

**Arguments**

When we call a function, we pass values, called arguments, by position to the corresponding parameter variables in a function. An argument is any piece of data that is passed into a function when the function is called.

Multiple arguments must be separated by commas.

**Ternary Operator**

The ternary expression syntax is: *a if condition else b*. One of either a or b is evaluated and returned based on the Boolean value of condition.

- If the condition evaluates to True, a is returned (and concatenated to the variable) and b is ignored
- If the condition evaluates to False, b is returned (and concatenated to the variable) and a is ignored

```python
result = "a" if i == 0 else "b"
```

**Global Variables**

A <u>global variable</u> is declared outside of functions and is accessible to all the functions in a program. A <u>global</u> constant is a name that references a value that should not be changed while the program runs.

It is recommended that programmers avoid using global variables in a program whenever possible.

**Random Number Functions**

The <u>import</u> statement causes the interpreter to load the contents of a module into memory. 

`import random` imports all functions

`from random import randrange` imports individual functions
```python
import random
rand = random.randint(1, 10)
``` 
Will create a random number between 1 and 10.

**Value-Returning Functions**

A value-returning function is a function that will return a value back to the part of the program that called it.
```python
def sum(num1, num2):
    result = num1 + num2
    return result
```

A value-returning function must have a return statement that sends a value back to the part of the program that called it.
```python
total = sum(1, 2)
print(total) # 3

total = sum(1)
print(total)
```

You can return mutipline value by commas separated them.
```Python
def roll_2_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2
```
In Python you can have a list of variables on the left side of the argument operator.
```python
dice1, dice2= roll_2_dice()
print(dice1)
print(dice2)
```

