import streamlit as st
import pandas as pd

# --- CONFIGURATION ET INITIALISATION DES DONNÉES ---
st.set_page_config(layout="wide")
st.title("Système de Réservation de Trains (Code Original)")

# Utilisation de st.session_state pour persister les données 'trains'
if 'trains' not in st.session_state:
    st.session_state.trains = {
        'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
        'TUN-ROM': {'places_total': 3, 'places_restantes': 0, 'passagers': set()},
        'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
    }

trains = st.session_state.trains

# --- FONCTIONS UTILITAIRES POUR STREAMLIT ---

def get_trains_df(current_trains):
    """Crée un DataFrame pour l'affichage tabulaire."""
    data = []
    for trajet, info in current_trains.items():
        data.append({
            'Trajet': trajet,
            'Places Totales': info['places_total'],
            'Places Restantes': info['places_restantes'],
            'Statut': 'Complet' if info['places_restantes'] == 0 else 'Disponible'
        })
    return pd.DataFrame(data)

# --- 1. AFFICHAGE DES TRAINS (Méthode 1) ---
def afficher_trains(current_trains):
    st.header("1. Afficher les trains")
    st.dataframe(get_trains_df(current_trains), use_container_width=True, hide_index=True)
    
    st.subheader("Format détaillé")
    for trajet, info in current_trains.items():
        places_total = info['places_total']
        places_restante = info['places_restantes']
        # passager = info['passagers'] # La variable n'est pas utilisée, donc on la retire
        st.write(f"Trajet **{trajet}** : **{places_restante}** places restantes /{places_total}")

# --- 2. RÉSERVATION (Méthode 2) ---
def reserver(current_trains):
    st.header("2. Réserver une place")
    
    # Remplacement de demander_code_trajet par st.selectbox
    code = st.selectbox(
        "Code trajet :", 
        options=list(current_trains.keys()),
        key="res_trajet"
    )
    
    info = current_trains[code]

    # Remplacement de input("Nom du passager : ").strip() par st.text_input
    nom = st.text_input("Nom du passager :", key="res_nom")
    
    if st.button("Confirmer la réservation", key="btn_reserver"):
        
        if not nom.strip():
            st.error("nom vide")
            return
            
        if info['places_restantes'] == 0:
            st.error("plus de place")
            return
        
        # Logique de vérification inversée dans votre code original (nom not in)
        if nom.strip() not in info['passagers']:
            info['passagers'].add(nom.strip())
            info['places_restantes'] -= 1
            st.success(f"Réservation OK. Passager: {nom.strip()}, Trajet: {code}")
            st.write("Place restantes:", info['places_restantes'])
        else:
            st.warning("nom deja dans liste") # Message original adapté

# --- 3. ANNULATION (Méthode 3 - Votre nom de fonction était 'supprimer_passager') ---
def supprimer_passager(current_trains):
    st.header("3. Annuler une réservation")
    
    # Remplacement de demander_code_trajet par st.selectbox
    code = st.selectbox(
        "Code trajet :", 
        options=list(current_trains.keys()),
        key="annul_trajet"
    )
    
    info = current_trains[code]
    passagers_existants = list(info['passagers'])
    
    # Remplacement de input() par st.selectbox pour une meilleure UI
    nom = st.selectbox(
        "Nom du passager à supprimer :", 
        options=[''] + passagers_existants, 
        key="annul_nom"
    )

    if st.button("Confirmer l'annulation", key="btn_annuler"):
        
        if not nom: # Vérifie si la sélection est vide ('')
            st.error("nom vide")
            return
            
        if nom in info['passagers']:
            info['passagers'].remove(nom)
            
            # Votre logique d'incrémentation
            if info['places_restantes'] < info['places_total']:
                info['places_restantes'] += 1
            
            st.success(f"Annulation ok pour {nom} sur {code}")
            st.write("Places restantes :", info['places_restantes'], "/", info['places_total'])
        else:
            st.error(f"Le passager {nom} n'est pas dans ce train.") # Message d'erreur ajouté

# --- 4. AFFICHAGE PASSAGERS (Méthode 4) ---
def afficher_passagers(current_trains):
    st.header("4. Afficher les passagers d’un train")
    
    # Remplacement de demander_code_trajet par st.selectbox
    code = st.selectbox(
        "Code trajet :", 
        options=list(current_trains.keys()),
        key="list_passagers"
    )
    
    passagers = current_trains[code]['passagers']
    
    st.subheader(f"Passagers pour {code}")
    if not passagers:
        st.write("Aucun passager n'est encore enregistré pour ce trajet.")
        return
    
    liste_tri = sorted(list(passagers))
    st.write(f"Total des passagers : {len(liste_tri)}")
    
    # Affichage adapté du print original (liste numérotée)
    st.code('\n'.join([f"{i}. {nom}" for i, nom in enumerate(liste_tri, 1)]))

# --- 5. TRAINS COMPLETS (Méthode 5) ---
def afficher_trains_complets(current_trains):
    st.header("5. Voir les trains complets")
    
    train_complet_trouve = False

    for trajet, info in current_trains.items():
        places_restante = info['places_restantes']
        
        if places_restante == 0:
            st.error(f"===le train {trajet} est complet ===")
            train_complet_trouve = True
            
    if not train_complet_trouve:
        st.success("Bonne nouvelle ! Aucun train n'est actuellement complet.")

# --- INTERFACE ET MENU PRINCIPAL (Remplacement de la fonction menu) ---

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Afficher Trains", 
    "2. Réserver", 
    "3. Annuler", 
    "4. Passagers", 
    "5. Trains Complets"
])

with tab1:
    afficher_trains(trains)
with tab2:
    reserver(trains)
with tab3:
    supprimer_passager(trains) # Note: nom de fonction corrigé ici
with tab4:
    afficher_passagers(trains)
with tab5:
    afficher_trains_complets(trains)

# Bouton Quitter (remplace l'option '0')
if st.button("0. Quitter l'application", type="primary"):
    st.stop()