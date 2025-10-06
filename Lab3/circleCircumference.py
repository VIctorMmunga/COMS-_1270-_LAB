# Victor
# 2025-09-14
# Lab 3 - circleCircumference.py
# Description: compute circumference using circleCircumference()
#Return circumference = 2 * pi * r.
#Citation: Runestone (thinkcspy).
#Source: https://runestone.academy/ns/books/published/thinkcspy/index.html?mode=browsing
#Accessed: 2023-02-02
    

import math

def circleCircumference(radius):
    return 2 * math.pi * radius
def main():
    radius = float(input("Enter circle radius: "))
    answer = circleCircumference(radius)
    print("The circumference is:", round(answer,2))
if __name__ == "__main__":
    main()