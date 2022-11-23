# Three cup monte game

from random import shuffle

# generating random list of my_list using shuffle and returning the value using the function below


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

# taking the input as guess of the player in the provided positions


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input(
            'Please guess the position in the given 0,1 and 2 values: ')
    return int(guess)

# checking the results


def check_guess(mixed_list, guess):
    if mixed_list[guess] == 'O':
        print("You're Correct!")
    else:
        print("Maybe Next Time")
        print(mixed_list)


my_list = [' ', ' ', 'O']

mixed_list = shuffle_list(my_list)

guess = player_guess()

check_guess(mixed_list, guess)
