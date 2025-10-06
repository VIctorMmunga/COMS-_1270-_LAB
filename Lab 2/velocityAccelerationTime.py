# Name: Victor Mmunga
# Date: 9, 11, 2025
# Lab #: 2
# Description: this programm Calculates final velocity from initial velocity, acceleration, and time.

# CITATION - Formula: v = u + (a * t)
# CITATION - URL: https://www.cuemath.com/physics/velocity-formula/
# CITATION - Author: Cuemath
# CITATION - Date Written/Posted: (no date provided)
# CITATION - Date Accessed: 9, 11, 2025



initial_velocity= int(input("Enter the velocity: "))
acceleration= int(input("Enter the accelaration: "))
time= int(input("Enter the time: "))
final_velocity= initial_velocity +(acceleration * time)
print(f"The final velocity is {final_velocity}")