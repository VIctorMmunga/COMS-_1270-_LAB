# Victor
# 2025-09-14
# Lab 3 - compoundAmount.py
# Description: compute compound amount A = P*(1 + r/n)^(n*t)
#Return amount after compounding.
#Citation: Runestone (thinkcspy).
#Source: https://runestone.academy/ns/books/published/thinkcspy/index.html?mode=browsing
#Accessed: 2023-02-02

def compoundAmount(principal, annual_rate_percent, years, compounding_periods_per_year):
    r = annual_rate_percent / 100.0
    n = compounding_periods_per_year
    return principal * (1 + r / n) ** (n * years)
def main():
    P = float(input("Enter principal amount: "))
    r = float(input("Enter annual rate (percent, e.g., 5): "))
    t = float(input("Enter years: "))
    n = int(input("Enter compounding periods per year (e.g., 12): "))
    A = compoundAmount(P, r, t, n)
    print("Amount after compounding =", A)
if __name__ == "__main__":
    main()