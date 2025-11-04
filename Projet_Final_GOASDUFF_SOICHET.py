#import streamlit

trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()},
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


## 5 ##

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
            annuler(trains)
        elif choix == "4":
            afficher_passagers(trains)
        elif choix == "5":
            afficher_trains_complets(trains)
        elif choix == "0":
            print("Au revoir.")
        else:
            print("Choix invalide, réessaie.\n")

menu(trains)