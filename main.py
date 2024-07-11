import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

gameImages=[rock,paper,scissor]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>=2 or user_choice<0:
   print("Invalid input")
else:
    print(gameImages[user_choice])
    
    comp_choice=random.randint(0,2)
    print("Computer chose :")
    print(gameImages[comp_choice])
    
    
    if user_choice==0 and comp_choice==2:
        print("YOU WIN!")
    elif comp_choice==0 and user_choice==2:
        print("YOU LOSE!")
    elif user_choice>comp_choice:
        print("YOU WIN!")
    elif comp_choice>user_choice:
        print("YOU LOSE!")
    elif user_choice==comp_choice:
        print("Draw! Try again")
