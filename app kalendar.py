import calendar
def createCalendar(year):
    for month in range(1, 13):
        print(calendar.month(year, month))
        
try:
    entry = int(input())
    createCalendar(entry)
    
except:
    print("Enter a valid year")
