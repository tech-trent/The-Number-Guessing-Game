"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
For this first project we will be using Workspaces. 
NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.
"""
   
   #Psuedo-code Hints
   
   #When the program starts, we want to:
   #------------------------------------
   #1. Display an intro/welcome message to the player.
   #2. Store a random number as the answer/solution.
   #3. Continuously prompt the player for a guess.
   #  a. If the guess greater than the solution, display to the player "It's lower".
   #  b. If the guess is less than the solution, display to the player "It's higher".
   
   #4. Once the guess is correct, stop looping, inform the user they "Got it"
   #     and show how many attempts it took them to get the correct number.
   #5. Let the player know the game is ending, or something that indicates the game is over.
   
   #( You can add more features/enhancements if you'd like to. )

import random

high_score = 15

def start_game():
    global high_score
    print('-----------------------------------')
    print('Welcome To The Number Guessing Game')
    print('-----------------------------------')
    print('Current Highscore = ' + str(high_score))

    secret_number = (round(random.random() * 100))
    attempts = 1
    user_guess = input('Guess a number between 1 and 100: ')
    keep_looping = True

    while keep_looping:
        try:
            if int(user_guess) < 0 or int(user_guess) > 100:
                user_guess = input('Error: Please guess a number between 0 and 100: ')
            else:
                if int(user_guess) == secret_number:
                        print("You guessed the correct number! The number was {} and it took you {} attempt(s).".format(
                            secret_number, attempts))
                        if attempts < high_score:
                            print('You set a new highscore! Congrats!')
                            high_score = attempts
                        try:
                            if str(input('Play again? y/N: ')).upper() == 'Y':
                                start_game()
                        except ValueError:
                            print('Exiting Game')
                        print('Exiting Game') 
                        keep_looping = False
                elif int(user_guess) < secret_number:
                    user_guess = int(input('The number is higher. Keep trying! '))
                    attempts += 1
                elif int(user_guess) > secret_number:
                    user_guess = int(input('The number is lower. Keep trying! '))
                    attempts += 1
        except ValueError:
            user_guess = int(input('Error: Please enter a number: '))

if __name__ == '__main__':
    # Start the program by calling the start_game function.
    start_game()
