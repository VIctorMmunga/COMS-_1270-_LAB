#Name: Victor Mmunga
#Date: 9-24-2025
#Lab #5- Student Loan Amortization
#This program calculates loan payments and prints a table showing how the laon is paid off over time.

def studentLoanAmortization(principal, yearlyInterestRate, numberOfYears):
    monthlyInterestRate = yearlyInterestRate / 12
    numberOfMonths = numberOfYears * 12
    monthlyPayment = principal * (monthlyInterestRate * (1 + monthlyInterestRate)**numberOfMonths) / ((1 + monthlyInterestRate)**numberOfMonths - 1)

    print("Period|Total Payment| Interest|Principal|Balance")
    print("________________________________________________")
    balance = principal
    for month in range(1, numberOfMonths + 1):
        interest = balance * monthlyInterestRate
        principalDue = monthlyPayment - interest
        balance -= principalDue
        if balance < 0:
            balance = 0
        print(f"{month:<7}{monthlyPayment:<15.2f}{interest:<10.2f}{principalDue:<10.2f}{balance:.2f}")
def main():
    principal = float(input("Please Input the Principal: "))
    yearlyInterestRate = float(input("Please Input the Yearly Interes: "))
    numberOfYears = int(input("Please Input the Number of Years: "))
    studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)
if __name__ == "__main__":
    main()