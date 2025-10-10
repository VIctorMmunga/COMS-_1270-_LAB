# Victor Mmunga   9 -20-2024
 # Assignment#3- nimGrab
# Displays a menu (play / rules / quit).
#  Supports 1-player (human vs computer) and 2-player (human vs human) modes.
#  Uses a random starting pile size (20-25 items).
#  Players take turns removing 1-3 items .
#  The player who takes the last item LOSES.
# 
print("NIMGRAB!")
print("By:Victor Mmunga")
print("[COM S 127 3]")
print()
import random

def main():
    min_point = 1
    max_point = 3
    while True:
        user_input = input("Do you want to [p]lay, read the [r]ules, or [q]uit?: ").lower()
        if user_input == "q":
            print("Goodbye!")
            break
        elif user_input == "r":
            
            print("""This is a NimGrab game!
                   On your turn you must take between one(1) and (3)three 
                   items ,You cannot take more items than are left.
                  The player who takes the last item loses.""")
            continue
        elif user_input == "p":
            player_choice = input("Do you want to play with [h]uman or [c]omputer?: ").lower()
            if player_choice not in ("h", "c"):
                print("Invalid input\n")
                continue

            num_point = random.randrange(20, 25)
            player = 1
            print(f"\nTotal points: {num_point}")
            print("| " * num_point + "\n")

            if player_choice == "c":
                while True:
                    
                    user_choice = int(input("How many points do you want to spend (1-3): "))
                    if user_choice < min_point or user_choice > max_point:
                        print("Invalid! Try again\n")
                        continue
                    elif user_choice > num_point:
                        print("Out of bounds, try again...\n")
                        continue
                    num_point -= user_choice
                    if num_point == 0:
                        print("You took the last point! You lose.\n")
                        break
                    print(f"Points left: {num_point}")
                    print("| " * num_point + "\n")
                    if num_point == 1:
                        comp = 1
                    elif num_point <= max_point + 1:
                        comp = num_point - 1
                    else:
                        left_point = (num_point - 1) % (max_point + 1)
                        if left_point == 0:
                            comp = random.randint(min_point, min(max_point, num_point - 1))
                        else:
                            comp = left_point
                    print(f"Computer takes: {comp}")
                    num_point -= comp
                    if num_point == 0:
                        print("Computer took the last point. Human wins!\n")
                        break
                    print("Points left:", num_point)
                    print("| " * num_point + "\n")

            else:
                player_turn = input("Who goes first? Enter 1 or 2: ").strip()
                if player_turn == "2":
                    player = 2
                else:
                    player = 1

                while True:
                    print("Points left:",num_point)
                    print("| " * num_point + "\n")
                    choice = int(input(f"Player {player} How many points do you wan to take(1-3): "))
                    if choice < min_point or choice > max_point:
                        print("Invalid! Try again\n")
                        continue
                    elif choice > num_point:
                        print("Out of bounds, try again...\n")
                        continue
                    num_point -= choice
                    if num_point == 0:
                        print(f"Player {player} took the last point and loses!")
                        winner = 1 if player == 2 else 2
                        print(f"Player {winner} wins!\n")
                        break
                    player = 2 if player == 1 else 1
        else:
            print("Invalid input\n")

if __name__ == "__main__":
    main() 