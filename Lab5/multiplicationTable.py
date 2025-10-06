def main():
  lowNum= int(input("Enter your low number: "))
  highNum= int(input("Enter your high number: "))
  MultiplicationTable(lowNum, highNum)

def MultiplicationTable (lowNum, highNum):
  for i in range(lowNum, highNum+1):
    for j in range(lowNum, highNum+1):
      product= i*j
      print(str(product).rjust(4), end="")
    print()
if __name__=="__main__":
  main()  


