def startRightTriangle (num):
    for i in range (1,  num+1):
        print(" "*(num-1), end="  ")
        for j in range(1, i+1):
         print(j, end= "  ")
        print()
def main():
    num= int(input("Enter your number: "))
    startRightTriangle(num)
if __name__=="__main__":
    main()
