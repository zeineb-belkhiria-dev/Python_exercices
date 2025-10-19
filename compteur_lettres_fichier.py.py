from os import strerror
mon_dict = {}
compteur = 0
file = input("input the file name : ")
for line in open(file,'rt'):
     for ch in line :
             if 'a'<=ch.lower()<='z':
                     mon_dict[ch.lower()]=mon_dict[ch.lower()] = mon_dict.get(ch.lower(), 0) + 1  
sorted_by_key = sorted(mon_dict.items())
for key, value in sorted_by_key:
    if value != 0:
        print(f"{key} -> {value}")
