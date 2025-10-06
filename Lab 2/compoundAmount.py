# Name: Victor Mmunga
# Date: 9, 11, 2025
# Lab #: 2
# Description: this programm Calculates total amount with compound interest.

# CITATION - Formula: A = P * (1 + (r/n))^(n*t)
# CITATION - URL: https://www.investopedia.com/terms/c/compoundinterest.asp
# CITATION - Author: Investopedia Team
# CITATION - Date Written/Posted: (updated 2024)
# CITATION - Date Accessed: 9, 11, 2025

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (as a percentage): "))
number_compounds = int(input("Enter the number of times interest compounds per year: "))
time = float(input("Enter the time in years: "))
accrued_amount = principal * (1 + (rate / 100) / number_compounds) ** (number_compounds * time)
print(f"The  amount after {time} years is {accrued_amount}")
