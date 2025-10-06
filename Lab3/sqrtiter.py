# Victor
# 2025-09-16
# Lab 3 - sqrtIter.py
# Description: approximate sqrt(x) using iterative estimation method
#Compute an estimate of sqrt(x) using iteration:
#initial guess y = (x + 1) / 2
#then repeat y = ((x / y) + y) / 2 for 'iterations' times.
#Citation: Cuemath "Square Root of 2 by Estimation and Approximation Method"
#Source: https://www.cuemath.com/algebra/square-root-of-2/
#Accessed: 2023-02-02
    
def sqrtIter(x, iterations):
  
    y = (x + 1) / 2  
    for i in range(iterations):
      y= ((x / y) + y) / 2
    return y
def main():
    x = int(input("Enter x (number to find sqrt of): "))
    iterations = int(input("Enter number of iterations: "))
    answer = sqrtIter(x, iterations)
    print("Estimated square root:", round(answer, 2))
if __name__ == "__main__":
    main()