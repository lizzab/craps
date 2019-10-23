# Ben Lizza
# 10/22/19

import random
# Balance


def balance():
    print("""
    Welcome to Craps!
    You will be asked to enter your bankroll
    This is the amount of money you will be playing with""")
    print("ENTER bankroll:")
    bal = int(input("> "))


balance()


def bet():
    print("Enter the amount you want to bet")
    betting = int(input("> "))


while bet() <= balance():
    def dice_roll():
        total_amount = balance() - bet()
        roll = random.randint(2,12)
        print(f"You rolled a {roll}")
        if roll == 2 or roll == 3 or roll == 12:
            lose_bet = total_amount - bet()
            print(f"You rolled a {roll}: You Lose!")
        elif roll == 7 or roll == 11:
            win_bet = total_amount + bet()
            print(f"You rolled a {roll}: You Win!")
        else:
            print(f"You rolled a {roll}: This is point")
            print("If you roll your point than you win! If you roll a 7 you lose")
    decision = input("Would you like to play again? \n1: Yes \n2: No")
    if decision == 1:
        dice_roll()
    else:
        print("Good luck with the rest of your day!")
    break



