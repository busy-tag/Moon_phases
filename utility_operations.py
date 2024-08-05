import sys
from datetime import datetime

def get_user_or_system_date():
    user_input = input("Enter a date (DD/MM/YYYY) or press Enter to use the current system date: ")

    if user_input.strip() == "":
        return datetime.now()
    else:
        try:
            return datetime.strptime(user_input, "%d/%m/%Y")
        except ValueError:
            print("Invalid date format. Please use 'DD/MM/YYYY'.")
            return get_user_or_system_date()

def get_drive_letter():
    while True:
        user_confirmation = input("Is the Busy Tag device connected to your computer? (yes/no): ").strip().lower()
        if user_confirmation in ['yes', 'y']:
            drive_letter = input("Please enter the drive letter assigned to Busy Tag device (e.g., D): ").strip().upper()
            if len(drive_letter) == 1 and drive_letter.isalpha():
                return drive_letter
            else:
                print("Invalid drive letter. Please enter a single letter (e.g., D).")
        elif user_confirmation in ['no', 'n']:
            print("Connect the Busy Tag device and restart the app.")
            sys.exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")