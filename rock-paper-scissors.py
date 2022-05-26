import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


player_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_number = random.randint(0,2)

if player_number == 0:
  print(rock)
  print("computer chose:")

  if computer_number == 0:
    print(rock)
    print("It's a tie")
  
  if computer_number == 1:
    print(paper)
    print("You lose")

  if computer_number == 2:
    print(scissors)
    print("You win")


elif player_number == 1:
  print(paper)
  print("computer chose:")

  if computer_number == 0:
    print(rock)
    print("You win")
  
  if computer_number == 1:
    print(paper)
    print("It's a tie")

  if computer_number == 2:
    print(scissors)
    print("You lose")

elif player_number == 2:
  print(scissors)
  print("computer chose:")

  if computer_number == 0:
    print(rock)
    print("You lose")
    
  if computer_number == 1:
    print(paper)
    print("You win")

  if computer_number == 2:
    print(scissors)
    print("It's a tie")
