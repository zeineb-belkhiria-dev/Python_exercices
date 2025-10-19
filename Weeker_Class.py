class WeekDayError(Exception):
    pass
	

class Weeker:
    def __init__(self, day):
        self.__day = day
        

    def __str__(self):
        if len(self.__day) == 3 :
            return self.__day
        else :
            raise WeekDayError
    

    def add_days(self, n):
        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        current_index = days.index(self.__day)
        nv_index = (n + current_index) % 7
        self.__day = days[nv_index]
            

    def subtract_days(self, n):
        days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        current_index = days.index(self.__day)
        nv_index = (current_index - n) % 7
        self.__day = days[nv_index]
            
        

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
    print(weekday)
except WeekDayError:
    print("Sorry, I can't serve your request.")

