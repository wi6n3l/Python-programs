import calendar
while True:
    try:
        yr1=int(input("Enter the year: "))
        cal1=calendar.calendar(yr1)
        print(cal1)
    except:
        print("Oops")
        continue
        

