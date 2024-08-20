from random import randint

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
cpu_choice = randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()

if difficulty == 'easy':
  chances = 10
  while chances > 0:
    print(f"You have {chances} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess > cpu_choice:
      print("Too high.")
      print("Guess again")
      chances-=1
    elif user_guess < cpu_choice:
      print("Too low")
      print("Guess again")
      chances-=1
    else:
      print(f"You got it, the answer was {cpu_choice}")
      break
  if chances == 0:
    print("You have lost")

elif difficulty == 'hard':
  chances = 5
  while chances > 0:
    print(f"You have {chances} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess > cpu_choice:
      print("Too high.")
      print("Guess again")
      chances-=1
    elif user_guess < cpu_choice:
      print("Too low")
      print("Guess again")
      chances-=1
    else:
      print(f"You got it, the answer was {cpu_choice}")
      break
  if chances == 0:
    print("You have lost")
else:
  print("Wrong input")