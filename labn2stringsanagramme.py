text1 = input("donner un texte : ").lower()
text2 = input("donner un texte : ").lower()

# Nettoyer les textes (enlever espaces et caractères non alphabétiques)
text1_clean = ""
text2_clean = ""

for char in text1:
    if char.isalpha():
        text1_clean += char

for char in text2:
    if char.isalpha():
        text2_clean += char

long1 = len(text1_clean)
long2 = len(text2_clean)

# Vérifier la longueur
if long1 != long2:
    print("non anagrammes")
    exit()

# Solution avec une seule double boucle
est_anagramme = True

for i in range(long1):
    lettre = text1_clean[i]
    compteur1 = 0
    compteur2 = 0
    
    # Compter les occurrences dans les deux textes en une seule boucle
    for j in range(long1):
        if text1_clean[j] == lettre:
            compteur1 += 1
        if text2_clean[j] == lettre:
            compteur2 += 1
    
    # Vérifier si les compteurs sont égaux
    if compteur1 != compteur2:
        est_anagramme = False
        break

if est_anagramme:
    print("anagrammes")
else:
    print("non anagrammes")
