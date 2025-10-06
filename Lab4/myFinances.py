
def annualPercentageRate(interest_charges, fees, loan_amount, days_in_term):
    
    daily_rate = (interest_charges + fees) / loan_amount / days_in_term
    apr = daily_rate * 365 * 100
    return apr

def compoundAmount(principal, annual_rate_percent, years, compounding_periods_per_year):
    r = annual_rate_percent / 100.0
    n = compounding_periods_per_year
    return principal * (1 + r / n) ** (n * years)