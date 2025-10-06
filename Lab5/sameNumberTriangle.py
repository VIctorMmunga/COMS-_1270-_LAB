
def sameNumberTriangle(num):
   for i in range(1, num+1):
      for j in range(i):
        print(i, end="  ")
      print()
def main():
   num= int(input("Enter your number: "))
   sameNumberTriangle(num)       
if __name__=="__main__":
   main()