# Victor
# 2025-09-14
# Lab 3 - areaOfCircle.py
# Description: compute area of a circle using areaOfCircle()
#Return area = pi * r^2.
#Citation: Runestone (thinkcspy).
#Source: https://runestone.academy/ns/books/published/thinkcspy/index.html?mode=browsing
# Accessed: 2023-02-02
    
import math
def areaOfCircle(radius):
    return math.pi * radius * radius
def main():
    radius = float(input("Enter circle radius: "))
    answer = areaOfCircle(radius)
    print("The area of the circle is:", answer)
if __name__ == "__main__":
    main()
