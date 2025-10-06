# Victor
# 2025-09-14
# Lab 3 - rectanglePerimeter.py
# Description: compute perimeter of a rectangle using rectanglePerimeter()
#Return perimeter = 2*(width + height).
#Citation: Runestone (thinkcspy) - concept adapted.
#Source: https://runestone.academy/ns/books/published/thinkcspy/index.html?mode=browsing
#Accessed: 2023-02-02
    
def rectanglePerimeter(width, height):
    return 2 * (width + height)
def main():
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))
    answer = rectanglePerimeter(width, height)
    print("The perimeter is:", answer)
if __name__ == "__main__":
    main()