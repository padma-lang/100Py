# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 09:27:45 2021

@author: SRI
"""
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


game_images = [rock,paper,scissors]
user_choice = int(input('What do you want to choose: 0 for rock,1 for paper & 2 for scissors:- \n'))
print('Your choice:')
print(game_images[user_choice])

comp_choice = random.randint(0,2)
print('comp_choice: ')
print(game_images[comp_choice])

print(f'Computer choice: {comp_choice}')
print(f'your choice: {user_choice}')

if user_choice >=3 or user_choice < 0:
    print('you chose an invalid number')
elif user_choice ==0 and comp_choice == 2:
    print('You win!!!')
elif comp_choice == 0 and user_choice ==2:
    print('You loose!!')
elif comp_choice > user_choice:
    print('You loose!!')
elif comp_choice == user_choice:
    print('You have a draw!!')
elif comp_choice < user_choice:
    print('You loose!!')

          



