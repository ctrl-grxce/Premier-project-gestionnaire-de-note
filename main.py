from fonctions import moyenne, a_reussi, afficher_etudiant

etudiant = { "Alice": [12, 15, 16, 17],
             "Gradi": [15, 16, 12, 20]
}
# Menu principale du programme 
while True:
    print("____gestionnaire de notes_____ - main.py:8")
    print("1.Affichier tout les étudiants - main.py:9")
    print("2. Affichier un étudiant - main.py:10")
    print("3. Ajouter un etudiant - main.py:11")
    print("4. Quitter - main.py:12")
    
    choix = input("Choissisez une option(entrer un chiffre): ")
    # si  l'utulisateur choisi 1, on affiche tout les étudiants
    if choix == "1":
        for nom, notes in etudiant.items():
            print(afficher_etudiant(nom, notes))
    # si l'utulisateur choisi 2, on lui donne une liste d'etudiant et il entre le nom de celui qu'il cherche et ensuite il aura les resutat
    if choix == "2":
        print(etudiant.keys())
        nom = input("choissisez l'étudiant dont vous voulez l'information :  ")
        if nom in etudiant:
            afficher_etudiant(nom, etudiant[nom])
        else:
            print("Nom introuvable - main.py:26")
    # si l'utilisateur choisi le nombre 3, il pourra ajouter un eleve dans la base de donné
    if choix == "3":
        new = input("Entrez le nom du nouvel étudiant que vous voulez rajouter :")
        nombre_note = int(input("Entrez le nombre de note que vous voulez rajouter :"))
        notes = []
        count = 0
        while count != nombre_note:
            note = int(input("Entrez une note : "))
            notes.append(note)
            count += 1
        if new in etudiant:
            print("il y'a déjà un étudiant de ce nom - main.py:38""")    
        else:
            etudiant.update({new: notes})
    if choix == "4":
        break

        
        
    
