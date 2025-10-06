# Victor
# 2025-09-14
# Lab 3 - annualPercentageRate.py
# Description: compute effective annual rate given nominal rate and compounding periods

   # Calculate APR given interest charges, fees, loan amount, and loan term days.
    #Formula: APR = ((interest + fees) / loan / days) * 365 * 100

def annualPercentageRate(interest_charges, fees, loan_amount, days_in_term):
    
    daily_rate = (interest_charges + fees) / loan_amount / days_in_term
    apr = daily_rate * 365 * 100
    return apr
def main(): 
    interest_charges = float(input("Enter the interest charges: "))
    fees = float(input("Enter the fees: "))
    loan_amount = float(input("Enter the loan amount: "))
    days_in_term = float(input("Enter the number of days in the loan term: "))
    answer = annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)
    print(f"The APR for this loan is {answer:.2f}%")
if __name__ == "__main__":
    main()
