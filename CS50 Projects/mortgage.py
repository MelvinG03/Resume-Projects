"""Mortgage calculator (fixed rate)"""

from argparse import ArgumentParser
import math
import sys

def get_min_payment(principal, annual_interest_rate, term=30, payments_per_year=12):
    """Minimum mortgage payment:

    Args:
        principal (float): Total mortgage
        annual_interest_rate (float): Annual interest (between 0 and 1)
        term (int): Number of years for mortgage (default: 30)
        payments_per_year (int): Payments (months) per year (default: 12)

    Returns:
        int: The minimum mortgage payment (math.ceil makes it to the next highest integer value)
    """
    r = annual_interest_rate / payments_per_year
    n = term * payments_per_year
    A = (principal * r * (1 + r)**n) / ((1 + r)**n - 1)
    return math.ceil(A)

def interest_due(balance, annual_interest_rate, payments_per_year=12):
    """Interest for next payment

    Args:
        balance (float): The balance (principal that hasn't been paid yet)
        annual_interest_rate (float): Annual interest (between 0 and 1)
        payments_per_year (int): Payments (months) per year (default: 12)

    Returns:
        float: The amount of interest due for next payment
    """
    r = annual_interest_rate / payments_per_year
    return balance * r

def remaining_payments(balance, annual_interest_rate, target_payment, payments_per_year=12):
    """Number of payments to make

    Args:
        balance (float): The balance (principal that hasn't been paid yet)
        annual_interest_rate (float): Annual interest (between 0 and 1)
        target_payment (float): How much user wants to pay per payment
        payments_per_year (int): Payments (months) per year (default: 12)

    Returns:
        int: The number of payments needed to pay the mortgage
    """
    counter = 0
    while balance > 0:
        interest = interest_due(balance, annual_interest_rate, payments_per_year)
        principal_payment = target_payment - interest
        balance -= principal_payment
        counter += 1
    return counter

def main(principal, annual_interest_rate, term=30, payments_per_year=12, target_payment=None):
    """Main function to calculate and display results

    Args:
        principal (float): Total mortgage
        annual_interest_rate (float): Annual interest (between 0 and 1)
        term (int): Number of years for mortgage (default: 30)
        payments_per_year (int): Payments (months) per year (default: 12)
        target_payment (float): How much user wants to pay per payment (default: None)
    """
    min_payment = get_min_payment(principal, annual_interest_rate, term, payments_per_year)
    print(f"Minimum payment: ${min_payment}")

    if target_payment is None:
        target_payment = min_payment

    if target_payment < min_payment:
        print("Target payment is less than minimum payment")
    else:
        total_payments = remaining_payments(principal, annual_interest_rate, target_payment, payments_per_year)
        print(f"With payments of ${target_payment}, the mortgage will be paid in {total_payments} payments.")

def parse_args(arglist):
    """Parse and validate command-line arguments.

    Args:
        arglist (list of str): List of command-line arguments.

    Returns:
        namespace: The parsed arguments (see argparse documentation for more information).

    Raises:
        ValueError: Encountered an invalid argument.
    """
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float, help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float, help="the annual interest rate, as a float between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30, help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12, help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float, help="the amount you want to pay per payment (default: the minimum payment)")
    
    args = parser.parse_args(arglist)
    if args.mortgage_amount <= 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years <= 0:
        raise ValueError("years must be positive")
    if args.num_annual_payments <= 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment is not None and args.target_payment <= 0:
        raise ValueError("target payment must be positive")

    return args

if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years, args.num_annual_payments, args.target_payment)
