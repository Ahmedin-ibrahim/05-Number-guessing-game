import random

# Number guessing game
print("Welcome to number guessing game!!!")

difficulty = input("Choose a level. (Easy, medium, hard)").lower().strip()
if difficulty == "easy":
    max_number = 25
elif difficulty == "medium":
    max_number = 50
else:
    max_number = 100
secret_number = random.randint(1, max_number)

trials = 0

while True:
    try:
        player_guess = int(input("\nGuess the number: "))
    except ValueError:
        print("Oops! That is not a number. Please type a whole number.")
        continue 

    trials = trials + 1

    if player_guess < secret_number:
        print("Higher!")
    elif player_guess > secret_number:
        print("Lower!")
    else:
        print(f"\n🎉 Congratulations! You guessed the secret number in {trials} trials!")
        break