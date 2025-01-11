import datetime
import pandas as pd
import re

def main():
    print("Welcome to the Motorcycle Maintenance Record System")

    current_date = input_date("Enter the current date (YYYY-MM-DD): ")
    current_mileage = input("Enter the current mileage: ")

    records = pd.DataFrame(columns=['date', 'type', 'mileage'])
    while True:
        action = input("Choose an action: 'add' to add a new record, 'view' to view records, 'check' to check maintenance requirements, or 'exit' to exit: ")
        if action.lower() == 'add':
            date = input_date("Enter the date of maintenance (YYYY-MM-DD): ")
            maintenance_type = input("Enter the type of maintenance: ")
            mileage = input("Enter the mileage at the time of maintenance: ")
            records = add_record(records, date, maintenance_type, mileage)
        elif action.lower() == 'view':
            view_records(records)
        elif action.lower() == 'check':
            check_maintenance(records, current_mileage, current_date)
        elif action.lower() == 'exit':
            break
        else:
            print("Invalid action. Please choose 'add', 'view', 'check', or 'exit'.")

def input_date(prompt):
    """Function to get and validate date input using regular expressions."""
    while True:
        date_str = input(prompt)
        correct_date = parse_date(date_str)
        if correct_date is not None:
            return correct_date
    

def parse_date(date_str):
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
    else:
        print("Invalid format. Please enter the date in the format YYYY-MM-DD.")

def add_record(records, date, maintenance_type, mileage):
    new_record = pd.DataFrame({
        'date': [date],
        'type': [maintenance_type],
        'mileage': [int(mileage)]
    })

# This was done because for some reason initially my integer values in the code and test code were not matching (int32 vs int64) 
# and kept producing an error and after doing some research online and in Youtube I saw that if the records were not intialized then everything converts to a string even if 
# specified otherwise, so I need to intialize the records variable with the one new entry so that this does not occur
    if records.shape[0] == 0:  
        records = new_record
        return records

    records = pd.concat([records, new_record], ignore_index=True)
    
    print("Record added successfully.")
    return records


def view_records(records):
    if records.empty:
        print("No records available.")
        return
    print(records)

def check_maintenance(records, current_mileage, current_date):
    
    if records.empty:
        print("No records available to check.")
        return
    
    # latest data
    latest_mileage = max(records['mileage'].max(), int(current_mileage))

    # last mileage and date record chenum
    latest_record = records.groupby("type")[["date", "mileage"]].max().reset_index()

    # get delta mileage
    latest_record["mileage"] = latest_mileage - latest_record["mileage"]
    latest_record["date"] = (current_date - pd.to_datetime(latest_record["date"])).dt.days
    latest_record.set_index("type", inplace=True)

    # check mileage
    do_maintenance = False
    if ("tire change" not in latest_record.index) or latest_record.loc["tire change", "mileage"] >= 10000:
        print("Tire change is due.")
        do_maintenance = True
    if ("air filter" not in latest_record.index) or latest_record.loc["air filter", "mileage"] >= 7500:
        print("Air filter replacement is due.")
        do_maintenance = True
    if ("clutch replacement" not in latest_record.index) or latest_record.loc["clutch replacement", "mileage"] >= 25000:
        print("Clutch replacement is due.")
        do_maintenance = True
    if ("chain replacement" not in latest_record.index) or latest_record.loc["chain replacement", "mileage"] >= 10000:
        print("Chain replacement is due.")
        do_maintenance = True
    if ("valve adjustment" not in latest_record.index) or latest_record.loc["valve adjustment", "mileage"] >= 20000:
        print("Valve adjustment is due.")
        do_maintenance = True
    if ("brake pad" not in latest_record.index) or latest_record.loc["brake pad", "mileage"] >= 20000:
        print("Brake pad check/replacement is due.")
        do_maintenance = True
    if ("oil change" not in latest_record.index) or latest_record.loc["oil change", "mileage"] >= 5000:
        print("Oil change is due.")
        do_maintenance = True

    # check timings
    if ("tire change" not in latest_record.index) or latest_record.loc["tire change", "date"] >= 1825:
        print("Tire change is due, due to time.")
        do_maintenance = True
    if ("air filter" not in latest_record.index) or latest_record.loc["air filter", "date"] >= 1460:
        print("Air filter replacement is due, due to time.")
        do_maintenance = True
    if ("registration" not in latest_record.index) or latest_record.loc["registration", "date"] >= 730:
        print("Registration is due, due to time.")
        do_maintenance = True
    if ("oil change" not in latest_record.index) or latest_record.loc["oil change", "date"] >= 180:
        print("Oil change is due, due to time.")
        do_maintenance = True

    print(latest_record)
    print(latest_mileage)
    print(records)
        
    # none required
    if not do_maintenance:
        print("No maintenance due! Eat some ice cream...")


if __name__ == "__main__":
    main()
