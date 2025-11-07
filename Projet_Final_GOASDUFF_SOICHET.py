trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 0, 'passagers': set()},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}

### METHODEs ###

## Methode Outil ##

def demander_code_trajet(trains):
    trajet = input("Code trajet : ").strip().upper()
    if trajet not in trains:
        print("trajet existe pas")
        return None
    return trajet

## 1 ##
def afficher_trains(trains):
    for trajet, info in trains.items():
        places_total=info['places_total']
        places_restante=info['places_restantes']
        passager=info['passagers']
        print(f"Trajet {trajet} : {places_restante} places restantes /{places_total}")

## 2 ##

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
    
    if nom not in info['passagers']:
        info['passagers'].add(nom)
        info['places_restantes'] -= 1
        numero_place = info['places_total'] - info['places_restantes']
        ticket = (nom, code, numero_place)

    print(ticket)


    print("Passager:", nom)
    print("Trajet:", code)
    print("Place restantes:", info['places_restantes'])

## 3 ##

def supprimer_passager(trains):
    code = demander_code_trajet(trains)
    if code is None:
        return
    
    info = trains[code]
    
    nom = input("Nom du passager : ").strip()
    if nom == "":
        print("nom vide")
        return
    
    if nom in info['passagers']:
        info['passagers'].remove(nom)
        if info['places_restantes'] < info['places_total']:
            info['places_restantes'] += 1
    
    print("Annulation ok pour", nom, "sur", code)
    print("Places restantes :", info['places_restantes'], "/", info['places_total'])

## 4 ##

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

## 5 ##

def afficher_trains_complets(trains):

    train_complet_trouve=False

    for trajet, info in trains.items():
        places_restante=info['places_restantes']
        
        if places_restante==0:
            print(f"===le train {trajet} est complet ===")
            train_complet_trouve=True
            

    if not train_complet_trouve:
        print("Bonne nouvelle ! Aucun train n'est actuellement complet.")

## MENU ##

def menu(trains):
    choix = ""
    while choix != "0":
        print("=== MENU RÉSERVATION TRAIN ===")
        print("1️⃣  Afficher les trains")
        print("2️⃣  Réserver une place")
        print("3️⃣  Annuler une réservation")
        print("4️⃣  Afficher les passagers d’un train")
        print("5️⃣  Voir les trains complets")
        print("0️⃣  Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            afficher_trains(trains)
        elif choix == "2":
            reserver(trains)
        elif choix == "3":
            supprimer_passager(trains)
        elif choix == "4":
            afficher_passagers(trains)
        elif choix == "5":
            afficher_trains_complets(trains)
        elif choix == "0":
            print("Au revoir.")
        else:
            print("Choix invalide, réessaie.\n")

menu(trains)
