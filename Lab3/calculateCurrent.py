# Victor
# 2025-09-14
# Lab 3 - calculateCurrent.py
# Description: calculate current I = V / R
#Return current I = V / R. If resistance is zero, raise ValueError.
# Citation: Ohm's law.

def calculateCurrent(voltage, resistance):
    return voltage / resistance
def main():
    voltage = float(input("Enter voltage (V) in volts: "))
    resistance = float(input("Enter resistance (R) in ohms: "))
    answer = calculateCurrent(voltage, resistance)
    print("The current I is:", round(answer, 3))
if __name__ == "__main__":
    main()