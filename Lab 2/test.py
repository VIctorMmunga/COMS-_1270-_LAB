import random

randam= random.randint(1, 10)
carry= input("Enter the number you want to play(3): ")
for i in carry:
    if carry== 10:
        i+=1
        print("the number exist")
    else:
        print("keep quessing, till you hit the righ number!")

