# Victor
# 2025-09-17
# Lab 3 - velocityAccelerationTime.py
# Description: compute final velocity after constant acceleration: v = v0 + a * t
def velocityAccelerationTime(v, a, t):
    return v + a * t
def main():
    v = float(input("Enter initial velocity: "))
    a = float(input("Enter acceleration: "))
    t = float(input("Enter time: "))
    answer = velocityAccelerationTime(v, a, t)
    print("The final velocity is:", answer)
if __name__ == "__main__":
    main()