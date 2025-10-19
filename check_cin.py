a = input("donner nombre avec 8 chiffres comme 1234567 : ")
taille = len(a)
if taille != 8 and (not a.isdigit()):
    print("donner un nombre avec 8 chiffres entier ")
else :
    if a[0]== 0 or a[0]== 1 :
        print("votre cin est valide ")
    else :
        print("votre cin n'est pas valide")






