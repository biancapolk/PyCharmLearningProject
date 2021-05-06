"""
PRICE CHECKER
"""
list = [1,2,3,4,5,6]
evens_list = []
def return_evens(list):
    for number in list:
        if number % 2 == 0:
            evens_list.append(number)
        else:
            pass
    return evens_list


if __name__ == "__main__":
    print(return_evens(list))

stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(ticker, price + (0.1*price))


"""
EMPLOYEE OF THE MONTH
"""



def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for name, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = name

        else:
            pass

    return (employee_of_month, current_max)


if __name__ == "__main__":
    work_hours = [('Abby', 100), ('Billy', 22222), ('Jess', 500)]
    print(employee_check(work_hours))


"""SHUFFLE A LIST AT RANDOM"""
# EXTERNAL DEPENDENCIES
from random import shuffle

# INITIAL LIST
# DEFINE STATE
list = [' ', 'O', ' ']

def shuffle_list(list):
    shuffle(list)
    return list

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("PICK A NUMBER: 0, 1, or 2")
    return int(guess)


def check_guess(list, guess):
    if list[guess] == 'O':
        print('Correct')
    else:
        print("Wrong guess!")
        print(list)


# FUNCTIONS
if __name__ == "__main__":

    # SHUFFLE LIST
    mixedup_list = shuffle_list(list)
    print(f"The current list is: {list}")
    print(f"This is where the cup is:{mixedup_list}")

    # USER GUESS
    guess = player_guess()

    # # CHECK GUESS
    check_guess(mixedup_list, guess)

"""*args and **kwargs"""

def a_func(*args):
    return sum(*args)

# FUNCTIONS
if __name__ == "__main__":
    list = [1,2,3,4,4]
    a_func(list)
    print(a_func(list))


def another_func(**kwargs):
    #abritrary # of key: value pairs
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is: {}'.format(kwargs['fruit']))
    else:
        print('I do not see fruit here')

if __name__ == "__main__":
    another_func(fruit='apple', veggie='broccli')


def last_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


if __name__ == "__main__":
    last_func(10, 20, 20, food='broccoli')

""" RETURNS EVEN NUMBERS IN FROM AN ARBITRARY LIST"""
def myfunc(*args):
        return [n for n in args if n%2 ==0]

if __name__ == "__main__":
    print(myfunc(10,20,30,47,53))

"""Return a matching string where every even letter is uppercase and every odd letter is lowercase. But the code doesn't show this exact result, any solution?"""


def myfunc(string):
    index = 0
    old_string = string
    new_string = ''
    # access every even letter
    for letter in old_string:
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        index += 1
    print(new_string)


if __name__ == "__main__":
    myfunc('BiancaBiaB')


""" COUNT PRIMES"""
def count_primes(num):
    # check for 0 or 1
    if num < 2:
        return 0
    ## 2 or grater
    primes = [2]
    # counter
    x = 3
    # x will go thru every num  until it hits the input num
    while x <= num:
        # check if x is prime
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break

        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


if __name__ == "__main__":
    count_primes(10)

"""LAMDA EXPRESSIONS, MAP, AND FILTER FUNCTIONS """
def square(num):
    return num ** 2


if __name__ == "__main__":
    my_nums = [1,2,3,4,5,6]
    # Do this (function) this number of times
    print(map(square,my_nums))
    for item in map(square,my_nums):
        print(item)

""" SPLICING STRINGS"""
def splicer(string):
    if len(string) % 2 == 0:
        return 'EVEN'
    else:
        return str[0]


if __name__ == "__main__":

    names = ['Andy', 'Eve', 'Sally']
    list(map(splicer, names))

"""FILTER OUT ALL EVENS"""
def check_even(num):
    return num % 2 == 0
if __name__ == "__main__":
    mynums = [1,2,3,4,5,6,7,8,9]
    print(list(filter(check_even, mynums)))

"""MILESTONE PROJECT: TIC-TAC-TOE"""
# VISUAL REPRESENTATION
# Implementation of Two Player Tic-Tac-Toe game in Python

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' Printing the updated board after every move in the game  '''

# NEW VISUAL WHEN BOARD RESETS
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# USER INTERACTION
# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # UPDATES
        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" ********* " + turn + " ********* ")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" ********* " + turn + " ********* ")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" ********* " + turn + " ********* ")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" ********* " + turn + " ********* ")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" ********* " + turn + " ********* ")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()
