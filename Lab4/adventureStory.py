#Victor Mmunga
#code: 09-24-2025
#Lab: 4, Adventure Story
# This program tells a short interactive adventure story
# using if statements and user input.

def main():
    print("Welcome to the Adventure Story!")
    print("By: Victor Mmunga")
    print("You wake up in a mysterious cave with two tunnels ahead of you.")

    choice1 = input("Do you want to go [left] or [right]?: ").lower()
    if choice1 == "left":
        print("You walk down the left tunnel and see a glowing chest.")
        choice2 = input("Do you want to [open] the chest or [ignore] it?: ").lower()
        if choice2 == "open":
            print("The chest is full of gold! You are now rich!")
        else:
            print("You ignore the chest and keep walking until you find the exit. You are safe!")
    elif choice1 == "right":
        print("You walk into a dark tunnel and hear growling sounds...")
        choice3 = input("Do you want to [run] away or [fight] the creature?: ").lower()
        if choice3 == "fight":
            print("You bravely fight the creature and win! You find treasure behind it!")
        else:
            print("You run back to the cave entrance. You are safe, but empty-handed.")
    else:
        print("You stand still and do nothing. Suddenly, the cave collapses and you barely escape!")

    print("The adventure is over. Thanks for playing!")
if __name__ == "__main__":
    main()