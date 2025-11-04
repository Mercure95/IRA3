trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 0, 'passagers': set()},
}

for trajet, info in trains.items():
    places_total=info['places_total']
    places_restante=info['places_restantes']
    passager=info['passagers']
    print(f"Trajet {trajet} : {places_restante} places restantes /{places_total}")




def demander_code_trajet(trains):
    trajet = input("Code trajet : ").strip().upper()
    if trajet not in trains:
        print("trajet existe pas")
        return None
    return trajet


#fonction reserver
def reserver(trains):
    code = demander_code_trajet(trains)
    if code is None:
        return
    info = trains[code]

    if info['places_restantes'] == 0:
        print("plus de place")
        return

    nom = input("Nom du passager : ").strip()
    if nom == "":
        print("nom vide")
        return
    
    if nom in info['passagers']:
        print("nom deja dans liste")
        return

    info['passagers'].add(nom)
    info['places_restantes'] -= 1

    print("Passager :", nom)
    print("Trajet :", code)
    print(info['places_restantes'])

reserver(trains)




def afficher_passagers(trains):
    code = demander_code_trajet(trains)
    if code is None:
        return 
    
    passagers = trains[code]['passagers']
    
    print(f"\n===Passagers pour {code} ===")
    if not passagers:
        print("Aucun passager n'est encore enregistré pour ce trajet.")
        return
    
    liste_tri = sorted(list(passagers))
    print(f"Total des passagers : {len(liste_tri)}")
    for i, nom in enumerate(liste_tri, 1):
        print(f"{i}. {nom}")

afficher_passagers(trains)



def afficher_complet(trains):
    for trajet, info in trains.items():
        places_restante=info['places_restantes']
        if places_restante==0:
            print(f"===le train {trajet} est complet ===")
            
        else :
            print("il reste des places pour touts les trains")
            
        
afficher_complet(trains)

















