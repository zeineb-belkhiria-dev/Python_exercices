import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self,firstweekday=0):
        super().__init__(firstweekday)
    def count_weekday_in_year(self,year,weekday):
        counter = 0
        for month in range(1,13):
            weeks = self.monthdays2calendar(year,month)
            for week in weeks :
                for day ,week_day in week :
                    if day != 0 and week_day == weekday :
                        counter += 1
        return counter
        
my_cal = MyCalendar()

print(my_cal.count_weekday_in_year(2019, 0))  
print(my_cal.count_weekday_in_year(2000, 6))
