import random

print("Welcome!!")
score = 0
options = {1: "rock", 2: "paper", 3: "scissors"}

def game():
  global score
  def playerOption():
    for key, value in options.items():
      print(key, value)
    player = int(input("Enter your choice: "))
    return player

  def computerOption():

    computer = random.randint(1, 3)
    return computer

  playerOptionValue = playerOption()
  computerOptionValue = computerOption()

  if (playerOptionValue == computerOptionValue):
    print("Draw")
  elif (playerOptionValue == 1 and computerOptionValue == 2):
    print("Computer wins")
    score = score - 1
  elif (playerOptionValue == 1 and computerOptionValue == 3):
    print("Player wins")
    score = score + 1
  elif (playerOptionValue == 2 and computerOptionValue == 1):
    print("Player wins")
    score = score + 1
  elif (playerOptionValue == 2 and computerOptionValue == 3):
    print("Computer wins")
    score = score - 1
  elif (playerOptionValue == 3 and computerOptionValue == 1):
    print("Computer wins")
    score = score - 1
  elif (playerOptionValue == 3 and computerOptionValue == 2):
    print("Player wins")
    score = score + 1
  else:
    print("Invalid choice. Try again")
  
for i in range(4):
  game()
  print("Your final score is: ", score)


print("1. Play Game")
print("2. Exit")
choice = int(input(""))
if choice == 1:
    game()
elif choice == 2:
    print("Thanks for playing")
