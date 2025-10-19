import os
def Find(path,dir):
    liste_files = os.listdir(path)
    for item in liste_files:
        path_absolute = os.path.join(path,item)
        if os.path.isdir(path_absolute) and item == dir :
            print(os.path.abspath(path_absolute))
        Find(path_absolute,dir)

resultat = Find("D:\\tree","python")
print(resultat)
