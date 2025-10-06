# Victor
# 2025-09-14
# Lab 3 - distanceSpeedTime.py
# Description: compute distance = speed * time
#Return distance traveled given speed and time.
#Citation: basic physics relation d = s * t.

def distanceSpeedTime(speed, time):
    return speed * time
def main():
    speed = float(input("Enter speed (units per time): "))
    time = float(input("Enter time (same units): "))
    answer = distanceSpeedTime(speed, time)
    print("The distance traveled is:", answer)
if __name__ == "__main__":
    main()