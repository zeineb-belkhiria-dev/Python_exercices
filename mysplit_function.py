
def mysplit(ch):
    liste = []
    mot_temporaire = ""
    for i in range(len(ch)) :
        if ch[i] != " ":
            mot_temporaire += ch[i]
        elif ch[i] == " " and mot_temporaire != "" :
            liste.append(mot_temporaire)
            mot_temporaire = ""

    if mot_temporaire != "" :
       liste.append(mot_temporaire)
       
    return liste
    

        



print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
