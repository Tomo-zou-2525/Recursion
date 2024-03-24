def how_much_is_your_debt(principal, annual_interest_rate, years):
    """
    Calculate the total debt after a given number of years with compound interest.

    Parameters:
    - principal: Initial amount of debt
    - annual_interest_rate: Annual interest rate (as a decimal)
    - years: Number of years

    Returns:
    - Total debt after the specified number of years (rounded down to the nearest whole number)
    """
    # Convert annual interest rate to a decimal
    interest_rate = annual_interest_rate / 100.0

    # Calculate the total debt using the compound interest formula
    total_debt = principal * pow(1 + interest_rate, years)

    # Round down to the nearest whole number
    total_debt = int(total_debt)

    return total_debt

# Example usage:
principal_amount = 10000
annual_interest_rate = 20
years = 2

result = how_much_is_your_debt(principal_amount, annual_interest_rate, years)
print(f"Total debt after {years} years: ${result}")
