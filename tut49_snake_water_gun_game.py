import random
lst=['s','w','g']

chances=10
no_of_chance=0
computer_score=0
human_score=0

print("\t______SNAKE WATER GUN GAME______")
print("\ns for snake\nw for water\ng for gun")

while no_of_chance<chances:
    _input=input("\nSnake,Water,Gun:")
    _random=random.choice(lst)

    if _input == _random:
        print("TIE BOTH SCORED 0 POINT TO EACH")

    elif _input == "s" and _random == "g":
        computer_score+=1
        print(f"YOUR GUESS {_input} COMPUTER GUESS {_random}")
        print("COMPUTER GETS 1 POINT")
        print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

    elif _input == "s" and _random == "w":
        human_score += 1
        print(f"YOUR GUESS {_input} COMPUTER GUESS {_random}")
        print("HUMAN GETS 1 POINT")
        print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

    elif _input == "s" and _random == "g":
        computer_score+=1
        print(f"YOUR GUESS {_input} COMPUTER GUESS {_random}")
        print("COMPUTER GETS 1 POINT")
        print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

    elif _input == "w" and _random == "g":
        human_score+=1
        print(f"YOUR GUESS {_input} COMPUTER GUESS {_random}")
        print("HUMAN GETS 1 POINT")
        print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

    elif _input == "w" and _random == "s":
        computer_score+=1
        print(f"YOUR GUESS {_input} COMPUTER GUESS {_random}")
        print("COMPUTER GETS 1 POINT")
        print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

    elif _input == "g" and _random == "s":
        human_score+=1
        print(f"YOUR GUESS {_input} COMPUTER GUESS {_random}")
        print("HUMAN GETS 1 POINT")
        print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

    elif _input == "g" and _random == "w":
        computer_score+=1
        print(f"YOUR GUESS {_input} COMPUTER GUESS {_random}")
        print("COMPUTER GETS 1 POINT")
        print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

    else:
        print("YOU GAVE WRONG INPUT")

    no_of_chance+=1
    print(f"CHANCES USED {no_of_chance} CHANCES LEFT {chances-no_of_chance}")

print("\nGAME OVER")

if computer_score>human_score:
    print("\nCOMPUTER WINS")
    print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

elif human_score>computer_score:
    print("\nHUMAN WINS")
    print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")

else:
    print("\nTIE")
    print(f"YOUR SCORE {human_score} COMPUTER SCORE {computer_score}")