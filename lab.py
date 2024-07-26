from datetime import date

date_obj = date.today()
date_obj = date_obj.replace(day=1)
print(date_obj) # This will output the date with the day set to the 1st of the current month
