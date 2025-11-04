import builtins
import contextlib
from copy import deepcopy

import streamlit as st

st.set_page_config(page_title="Réservations Train", layout="centered")


### PARTIE CODE ###

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

### PARTIE STREAMLIT ###

if "trains" not in st.session_state:
    st.session_state.trains = deepcopy(trains)

class IOShim:
    def __init__(self, inputs):
        self.inputs = list(inputs)  # queue
        self.outputs = []

    def input(self, prompt=""):
        if not self.inputs:
            raise RuntimeError("Input manquant pour le flux Streamlit.")
        return self.inputs.pop(0)

    def print(self, *args, **kwargs):
        txt = " ".join(str(a) for a in args)
        self.outputs.append(txt)

@contextlib.contextmanager
def patch_io(shim: IOShim):
    old_input = builtins.input
    old_print = builtins.print
    builtins.input = shim.input
    builtins.print = shim.print
    try:
        yield
    finally:
        builtins.input = old_input
        builtins.print = old_print

st.title("Réservations de trains")

action = st.selectbox(
    "Choisir une action",
    (
        "Afficher les trains",
        "Réserver une place",
        "Annuler une réservation",
        "Afficher les passagers d’un train",
        "Voir les trains complets",
    )
)

codes = list(st.session_state.trains.keys())
col1, col2 = st.columns(2)

if action == "Afficher les trains":
    if st.button("Exécuter"):
        shim = IOShim(inputs=[])
        with patch_io(shim):
            afficher_trains(st.session_state.trains)
        for line in shim.outputs:
            st.write(line)

elif action == "Réserver une place":
    code = col1.selectbox("Code trajet", options=codes)
    nom  = col2.text_input("Nom du passager")
    if st.button("Réserver"):
        shim = IOShim(inputs=[code, nom])
        with patch_io(shim):
            reserver(st.session_state.trains)
        for line in shim.outputs:
            st.write(line)

elif action == "Annuler une réservation":
    code = col1.selectbox("Code trajet", options=codes)
    existants = sorted(st.session_state.trains[code]['passagers'])
    nom = col2.selectbox("Nom du passager", [""] + existants)
    if st.button("Annuler"):
        shim = IOShim(inputs=[code, nom])
        with patch_io(shim):
            supprimer_passager(st.session_state.trains)
        for line in shim.outputs:
            st.write(line)

elif action == "Afficher les passagers d’un train":
    code = st.selectbox("Code trajet", options=codes)
    if st.button("Afficher"):
        shim = IOShim(inputs=[code])
        with patch_io(shim):
            afficher_passagers(st.session_state.trains)
        for line in shim.outputs:
            st.write(line)

elif action == "Voir les trains complets":
    if st.button("Lister"):
        shim = IOShim(inputs=[])
        with patch_io(shim):
            afficher_trains_complets(st.session_state.trains)
        for line in shim.outputs:
            st.write(line)

st.divider()
st.subheader("État actuel")
for k, v in st.session_state.trains.items():
    st.write(k, "→", f"{v['places_restantes']}/{v['places_total']} | Passagers:", sorted(v['passagers']))
