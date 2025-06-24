from datetime import datetime

def calculate_age(dob_str):
    try:
        dob = datetime.strptime(dob_str, '%d/%m/%Y')
    except:
        return 0
    today = datetime.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))