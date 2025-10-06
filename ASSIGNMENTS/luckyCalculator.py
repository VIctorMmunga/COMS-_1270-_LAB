#Victor Mmunga    9-20-2025
#Assigment #2
#This a calculator app that can do different operations and generate a lucky number

print("Lucky Number")
print("By: Victor Mmunga")
print("COM S 127 #3")

import random

while True:
 choice = input("choose  choice of yours: [c] calculator, [l]lucky number, [q] quit: ").lower()

 if choice== 'l':
    user2= int(input("Please Enter a number: "))
    user3= int(input("Please Enter a number: "))
    number1= min(user2, user3)
    number2= max(user2, user3)
    luck_number= random.randint(number1, number2)
    print(f"Your lucky number is: {luck_number}")

 elif choice== 'c':
    user_input  = input("please choose a calculation [+],[-],[*],[/],[//],[%],[**]: ")
    if user_input not in ("+","-","*","/","//","%","**"):
      print(f"ERROR: you must choose:( +,  -, *, /, //, %, **)")
    else:
        user2= int(input("Please Enter a number: "))
        user3= int(input("Please Enter a number: "))
    
    if  user_input in ("//", "/", "%")  and user3 == 0: 
         
        print(f"ERROR in {user_input} function: b = 0")
        print(f"The result of your calculation was:{user2}")

    elif choice =='c' and  user_input in("+","-","*","/","//","%","**"):
        print(f"The result is :{eval(f'{user2}{user_input}{user3}')} ")
    
 elif choice=='q':
    print("Goodbye!")
    break
 else:
    print("I did not understand your input...please try again....")
    

