import random as rd 

def roller():    
    dice1 = rd.randint(1,6)
    dice2 = rd.randint(1,6)
    sum_dices = dice1 + dice2
    return sum_dices, dice1, dice2

def game():
    sum_dices, dice1, dice2 = roller()
    print(f'Your sum of dice is {dice1} + {dice2} = {sum_dices}')

    if sum_dices in (7,11):
        print("You won!")
    elif sum_dices in (2,3,12):
        print("You lose!")
    else:
        new_goal = sum_dices
        print(f'Your new goal is {new_goal}')
        situation = True

        while situation:
            sum_dices, dice1, dice2 = roller()
            print(f'Your sum of dice is {dice1} + {dice2} = {sum_dices}')
            if sum_dices == new_goal:
                print("You won!")
                situation = False
            elif sum_dices == 7:
                print("You lose!")
                situation = False

game()
