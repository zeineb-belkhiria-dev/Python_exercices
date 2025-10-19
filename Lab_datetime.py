from datetime import date
from datetime import datetime
d = datetime(2020,11,4,14,53)
delta1 = d.strftime("%Y/%m/%d %H:%M:%S")
print(delta1)



delta2 = d.strftime("%y/%B/%d %H:%M:%S %p")
print(delta2)



delta3 = d.strftime("%a,%Y %b %d")
print(delta3)



delta4 = d.strftime("%A,%Y %B %d")
print(delta4)


delta5 = d.strftime("Weekday : %u")
print(delta5)


delta6 = d.strftime("DAY OF THE YEAR : %j")
print(delta6)


delta7 = d.strftime("week number of the year : %W")
print(delta7)


