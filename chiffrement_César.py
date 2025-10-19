while True:
    text_non_chiffrée = input("entrez un text : ")
    try:
        nombre_de_décalage = int(input("entrer un nombre entier entre 1 et 25 : "))
    except ValueError:
        print("Veuillez entrer un nombre valide")
        continue
        
    if nombre_de_décalage < 1 or nombre_de_décalage > 25:
        print("entrer un nombre dans l'intervalle : ")
        continue
        
    text_chiffré = ''
    
    for ch in text_non_chiffrée:
        if ch.isalpha():
            if ch.isupper():
                if ord(ch) + nombre_de_décalage <= ord('Z'):
                    text_chiffré += chr(ord(ch) + nombre_de_décalage)
                else:
                    text_chiffré += chr(ord(ch) + nombre_de_décalage - 26)
            else:
                if ord(ch) + nombre_de_décalage <= ord('z'):
                    text_chiffré += chr(ord(ch) + nombre_de_décalage)
                else:
                    text_chiffré += chr(ord(ch) + nombre_de_décalage - 26)
        else:
            text_chiffré += ch

    print(text_chiffré)
            

            
            
            
            
        
