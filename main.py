# Snake Water Gun
import random

lst = ["Snake", "Water", "Gun"]
my_count = 0
comp_count = 0

def win(me, comp):
    global my_count
    global comp_count
    if me == "s" and comp == "Water":
        my_count += 1
        print(f"You Win!!({my_count})")
    elif me == "s" and comp == "Gun":
        comp_count += 1
        print(f"Computer win!!({comp_count})")
    elif me == "w" and comp == "Snake":
        comp_count += 1
        print(f"Computer win!!({comp_count})")
    elif me == "w" and comp == "Gun":
        my_count += 1
        print(f"You Win!!({my_count})")
    elif me == "g" and comp == "Snake":
        my_count += 1
        print(f"You Win!!({my_count})")
    elif me == "g" and comp == "Water":
        comp_count += 1
        print(f"Computer win!!({comp_count})")
    else:
        print("Match tie!!")

    if my_count > comp_count:
        return my_count
    else:
        return comp_count



print("Welcome to the Game!!\nSnake Water Gun")

i = 1
w = my_count
while(i <= 10):
    print("Enter your choice..\n"
          "\ts for Snake\n"
          "\tw for Water\n"
          "\tg for Gun\n")
    my_choice = input()
    my_choice.lower()

    if my_choice != "s" and my_choice != "w" and my_choice != "g":
        print("Wrong choice!!\nTry again")
        my_choice = input()

    comp_choice = random.choice(lst)

    print(f"Computer selected {comp_choice}")
    w = win(my_choice, comp_choice)

    i = i + 1



if w == my_count:
    print("10 matches are over!!\nYou won the match!!")
else:
    print("10 matches are over!!\nComputer won the match!!")

