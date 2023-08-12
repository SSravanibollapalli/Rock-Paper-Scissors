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

img = [rock, paper, scissors]
inp = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if inp > 2:
  print("You chose invalid number. You Lose!!")
else:
  print(img[inp])
  comp = random.randint(0,2)
  print(f"Computer Chose :{comp}")
  print(img[comp])


  if comp == inp:
    print("It's a Draw")
  elif comp == 1 and inp == 0 :
    print("You Lose!!")
  elif comp == 0 and inp == 2:
    print("You Lose!!")
  elif comp == 2 and inp == 1:
    print("You Lose!!")
  else: 
    print("You Win!!")

