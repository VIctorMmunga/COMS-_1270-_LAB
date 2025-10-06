# Victor
# 2025-09-14
# Lab 3 - calculateVoltage.py
# Description: compute voltage V = I * R
# Return V = I * R.
# Citation: Runestone (thinkcspy) - basic Ohm's law exercise.
# Source: https://runestone.academy/ns/books/published/thinkcspy/index.html?mode=browsing
#Accessed: 2023-02-02
    

def calculateVoltage(current, resistance):
    return current * resistance
def main():
    current = float(input("Enter current (I) in amperes: "))
    resistance = float(input("Enter resistance (R) in ohms: "))
    answer = calculateVoltage(current, resistance)
    print("Voltage =", answer)
if __name__ == "__main__":
    main()