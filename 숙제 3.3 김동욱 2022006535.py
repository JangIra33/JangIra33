from datetime import date

def check_adult(years,months,days):
    from datetime import date
    today = date.today()
    return years <= today.year -20 or\
        years == today.year - 19 and months < today.month or\
            years == today.year - 19 and months == today.month and days <= today.day

today = date.today()
year = today.year
month = today.month
day = today.day
print(today)
print(check_adult(year-20,12,31))       # True
print(check_adult(year-19,month-1,1))   # True
print(check_adult(year-19,month,day-1)) # True
print(check_adult(year-19,month,day))   # True
print(check_adult(year-19,month,day+1)) # False
print(check_adult(year-19,month+1,1))   # False