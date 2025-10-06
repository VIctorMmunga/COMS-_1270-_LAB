# Name: Victor Munga
# Date: 9, 11, 2025
# Lab #: 2
# Description: this program Calculates APR of a loan.


# CITATION - Formula: APR = (((interest + fees) / loan_amount) / days_in_term) * 100
# CITATION - URL: https://www.consumerfinance.gov/ask-cfpb/what-is-the-annual-percentage-rate-apr-en-102/
# CITATION - Author: Consumer Financial Protection Bureau
# CITATION - Date Written/Posted: (updated 2023)
# CITATION - Date Accessed: 9, 11, 2025

interest_charges = float(input("Enter the interest charges: "))
fees = float(input("Enter the fees: "))
loan_amount = float(input("Enter the loan amount: "))
days_in_term = float(input("Enter the number of days in the loan term "))
apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
print(f"The APR for this loan is {apr}%")
