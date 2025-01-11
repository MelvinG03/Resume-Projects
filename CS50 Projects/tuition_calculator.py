from argparse import ArgumentParser
import sys

def calculate_tuition(credits=12, resident=True, dt=False):
    
    """ Calculates tuition for one semester of UMD

    Takes into consideration the number of credits the student is taking,
    whether they are a resident of Maryland, and whether they pay
    differential tuition.

    Args:
        credits (integer): the number of credits the student is taking (default: 12)
        resident (boolean): If student is in-state or out of state (default: True/In-state)
        dt (boolean): If student pays differential tuition (default: False)

    Raises:
        ValueError: must be a positive value

    Output:
        float: final fee of the student """
    
    if credits < 0:
        raise ValueError("Credits must be positive")

    if credits == 0:
        return 0

    # Tuition rates and fees
    resident_tuition_per_credit = 367.00
    nonresident_tuition_per_credit = 1456.00
    resident_full_time_tuition = 4412.00
    nonresident_full_time_tuition = 17468.00
    differential_tuition_per_credit = 118.00
    differential_full_time_tuition = 1428.00
    full_time_fees = 977.50
    part_time_fees = 455.00

    if credits >= 12:
        # Full-time students
        tuition = resident_full_time_tuition if resident else nonresident_full_time_tuition
        if dt:
            tuition += differential_full_time_tuition
        fees = full_time_fees
    else:
        # Part-time students
        tuition = resident_tuition_per_credit * credits if resident else nonresident_tuition_per_credit * credits
        if dt:
            tuition += differential_tuition_per_credit * credits
        fees = part_time_fees

    return tuition + fees

def parse_args(arglist):
    
    """ Arguments for parse command line

    -c / --credits (int): the number of credits the student is taking (default: 12)
    -nr / --nonresident: indicates the student is not a Maryland resident (True/False, action: 'store_true')
    -dt / --differentialtuition: indicates the student pays differential tuition (True/False, action: 'store_true')

    Args:
        arglist (list of str): a list of command-line arguments.

    Output:
        namespace: a namespace with variables credits, nonresident, and differentialtuition """
    
    parser = ArgumentParser()
    parser.add_argument('-c', '--credits', type=int, default=12, help="the number of credits the student is taking")
    parser.add_argument('-nr', '--nonresident', action='store_true', help="indicates the student is not a Maryland resident")
    parser.add_argument('-dt', '--differentialtuition', action='store_true', help="indicates the student pays differential tuition")
    
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    resident = not args.nonresident
    total_cost = calculate_tuition(credits=args.credits, resident=resident, dt=args.differentialtuition)
    print(f"Your final tuition is ${total_cost}")