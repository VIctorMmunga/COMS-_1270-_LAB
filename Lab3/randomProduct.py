# Victor M
# 2025-09-18
# Lab 3 - randomProduct.py
# Description: compute product of 'a' random integers between b and c (inclusive)

import random

def randomProduct(a, b, c):
    product=1
    for i in range(a):
        num = random.randrange(b, c + 1)  
        product *=num
    return product
def main():
    a = int(input("Enter a (how many random numbers): "))
    b = int(input("Enter b (lower bound): "))
    c = int(input("Enter c (upper bound: "))
    answer = randomProduct(a, b, c)
    print("The answer is:", answer)
if __name__ == "__main__":
    main()


