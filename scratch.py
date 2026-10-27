from datetime import date, datetime
birthdate = '28-10-2008'
MIN_AGE = 18

today_value = date.today()
birthdate_value = datetime.strptime(birthdate, "%d-%m-%Y").date()
age = today_value.year - birthdate_value.year
if (today_value.month, today_value.day) < (birthdate_value.month, birthdate_value.day):
    age -= 1
print(age)