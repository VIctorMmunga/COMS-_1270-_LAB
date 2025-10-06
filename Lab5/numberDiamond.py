def numberDiamond(num):
 for i in range(1,num+1 ):
     print(" "*(num-i), end=" ")
     for j in range(1, i+1):
        print(f"\033[91m{j}\033[0m", end="  ")
     print()
 for i in range(num - 1, 0, -1):
        print(" "*(num-i), end=" ")
        for j in range(1, i +1):
          print(f"\033[94m{j}\033[0m", end="  ") 
        print()
def main():
   num= int(input("Enter your integer: ")) 
   numberDiamond(num)

if __name__=="__main__":
   main()