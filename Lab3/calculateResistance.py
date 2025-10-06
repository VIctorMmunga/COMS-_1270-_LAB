# Victor
# 2025-09-14
# Lab 3 - calculateResistance.py
# Description: calculate resistance R = V / I
#Return resistance R = V / I. If current is zero, raise ValueError.
# Citation: Ohm's law.

def calculateResistance(voltage, current):
    return voltage / current
def main():
    voltage = float(input("Enter voltage (V) in volts: "))
    current = float(input("Enter current (I) in amperes: "))
    answer = calculateResistance(voltage, current)
    print("The resistance R is:",round(answer, 2), "ohms")

if __name__ == "__main__":
    main()