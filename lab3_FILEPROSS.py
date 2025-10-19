import sys
from os import strerror 

class StudentsDataException(Exception):
    """Classe de base pour les exceptions liées aux données des étudiants."""
    pass


import sys
from os import strerror 

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, line_number, content):
        super().__init__(f"Ligne {line_number} invalide: {content}")

class FileEmpty(StudentsDataException):
    def __init__(self, filename):
        super().__init__(f"Le fichier '{filename}' est vide.")

file_prof = input("donner le nom du fichier : ")
if file_prof != "D:\\file_prof.txt":
    print("nom invalide")
    sys.exit()

students_dict = {}
try:
    with open("file_prof.txt", "rt", encoding="utf-8") as f:
        data = f.readlines()
        if not data:
            raise FileEmpty(filename)

        for i, line in enumerate(data, start=1):
            parts = line.strip().split()
            if len(parts) != 3:
                raise BadLine(i, line)

            prenom, nom, number_point_str = parts
            try:
                number_point = float(number_point_str)  
            except ValueError:
                raise BadLine(i, line)

            fullname = f"{prenom} {nom}"
            if fullname in students_dict:
                students_dict[fullname] += number_point
            else:
                students_dict[fullname] = number_point

    
    for student, total in sorted(students_dict.items()):
        print(f"{student}\t{total}")


except (BadLine, FileEmpty) as e:
    print(e)
    sys.exit(1)
except IOError as e:
    print("Erreur d'ouverture du fichier :", strerror(e.errno))
    sys.exit(e.errno)
