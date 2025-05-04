#Step 1: Generate a Random Number
import random
number_to_guess = random.randint(1, 100)

#Step 2: Prompt the User for Guesses
#Bonus Task:
#Limit the number of attempts to 10. If the user fails to guess in 10 attempts, end the game with a message like "Game over! Better luck next time!"
attempted_guess = 0
bonus_task_max = 10
while attempted_guess < bonus_task_max:
    user_input = int(input("Guess the random number between 1 and 100: "))
    if user_input > number_to_guess:
        print("Too high! Try again.")
    elif user_input < number_to_guess:
        print("Too low! Try again.")
    elif user_input == number_to_guess:
        attempted_guess += 1
        #print("Congratulations! You guessed it!")
        break
    else:
        print("Error")
    attempted_guess += 1

#Step 3: Count the Attempts
if attempted_guess < bonus_task_max:
    print("Congratulations! You guessed it in" , attempted_guess , "attempts!")
else:
    print("Game over! Better luck next time!")


