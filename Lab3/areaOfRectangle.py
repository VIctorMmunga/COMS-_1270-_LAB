# Victor
# 2025-09-14
# Lab 3 - areaOfRectangle.py
# Description: compute area of a rectangle using a function named areaOfRectangle
 
  #  Calculate and return area = width * height.
  #  Citation: Adapted exercise idea from Runestone (How to Think Like a Computer Scientist).
  #  Source: https://runestone.academy/ns/books/published/thinkcspy/index.html?mode=browsing
  #  Accessed: 2023-02-02

def areaOfRectangle(width, height):
    return width * height
def main():
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))
    answer = areaOfRectangle(width, height)
    print("The area is:", answer)
if __name__ == "__main__":
    main()