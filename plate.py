import re

def is_valid_number_plate(plate):
    
    pattern = r'^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$'
    
    if re.match(pattern, plate):
        return True
    else:
        return False


user_input = input("Enter the vehicle number plate: ").strip()


if is_valid_number_plate(user_input):
    print("The number plate is valid.")
else:
    print("The number plate is invalid.")
