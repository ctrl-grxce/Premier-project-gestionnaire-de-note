def moyenne(notes):
    ''' pre: recois une liste de note
        post: renvoi la moyenne de cette liste 
    '''
    for note in notes:
        moy = sum(notes) / len(notes)
        return moy

def a_reussi(notes):
    if moyenne(notes) >= 10:
        return  True
    return False

def afficher_etudiant(nom, notes):
    print("Nom: ", nom)
    print("Notes:", notes)
    print("Moyenne :", moyenne(notes))
    
    if a_reussi(notes) is True:
        print("status :Réussi")
    else:
        print("status : Echec")
