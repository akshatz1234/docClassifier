from datetime import datetime
from flask import Response

def calc_age(dob):
    try:
        today = date.today()
        bdate = datetime.strptime(dob, "%d/%m/%Y")
        age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
        return age
    except:
        return None

def clean(dob):
    try:
        if len(dob)==4:        
            return "1-1-"+dob
        else:
            return(dob.replace('/','-'))
    except:
        return None

def main(dob):
    return(calc_age(clean(dob)))