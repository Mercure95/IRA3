import streamlit as st
import pandas as pd

# --- INITIALISATION DES DONNÉES ---
st.set_page_config(layout="wide")
st.title("Système de Réservation de Trains")

if 'trains' not in st.session_state:
    st.session_state.trains = {
        'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
        'TUN-ROM': {'places_total': 3, 'places_restantes': 0, 'passagers': set()},
        'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
    }

trains = st.session_state.trains

# --- FONCTION UTILITAIRE ---
def get_trains_df(current_trains):
    data = []
    for trajet, info in current_trains.items():
        data.append({
            'Trajet': trajet,
            'Places Totales': info['places_total'],
            'Places Restantes': info['places_restantes'],
            'Statut': 'Complet' if info['places_restantes'] == 0 else 'Disponible'
        })
    return pd.DataFrame(data)

# --- INTERFACE ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. Afficher Trains", 
    "2. Réserver", 
    "3. Annuler", 
    "4. Passagers", 
    "5. Trains Complets"
])

# ====================================================================
# TAB 1 : AFFICHAGE DES TRAINS
# ====================================================================
with tab1:
    st.header("1. Afficher les trains")
    st.dataframe(get_trains_df(trains), use_container_width=True, hide_index=True)

# ====================================================================
# TAB 2 : RÉSERVER UNE PLACE
# ====================================================================
with tab2:
    st.header("2. Réserver une place")
    
    trajet_choisi = st.selectbox(
        "Trajet :", 
        options=list(trains.keys()),
        key="res_trajet"
    )
    
    nom_passager = st.text_input("Nom du passager :", key="res_nom")
    current_info = trains[trajet_choisi]

    if st.button("Confirmer la réservation", key="btn_reserver"):
        
        if not nom_passager.strip():
            st.error("Le nom du passager ne peut pas être vide.")
        elif current_info['places_restantes'] == 0:
            st.error(f"Le trajet {trajet_choisi} est complet.")
        elif nom_passager.strip() in current_info['passagers']:
            st.warning(f"{nom_passager} a déjà une réservation sur ce trajet.")
        else:
            current_info['passagers'].add(nom_passager.strip())
            current_info['places_restantes'] -= 1
            st.success(f"Réservation réussie pour {nom_passager.strip()} sur le trajet {trajet_choisi}.")
            
            place_num = current_info['places_total'] - current_info['places_restantes']
            st.write(f"Ticket : ({nom_passager.strip()}, {trajet_choisi}, place n°{place_num})")


# ====================================================================
# TAB 3 : ANNULER UNE RÉSERVATION
# ====================================================================
with tab3:
    st.header("3. Annuler une réservation")

    trajet_annul = st.selectbox(
        "Trajet pour l'annulation :", 
        options=list(trains.keys()),
        key="annul_trajet"
    )
    
    info_annul = trains[trajet_annul]
    passagers_existants = list(info_annul['passagers'])
    
    passager_annul = st.selectbox(
        "Passager à annuler :", 
        options=[''] + passagers_existants, 
        key="annul_nom"
    )

    if st.button("Confirmer l'annulation", key="btn_annuler"):
        
        if not passager_annul:
             st.error("Veuillez sélectionner un passager à annuler.")
        elif passager_annul not in info_annul['passagers']:
            st.error(f"Le passager {passager_annul} n'a pas de réservation sur {trajet_annul}.")
        else:
            info_annul['passagers'].remove(passager_annul)
            
            if info_annul['places_restantes'] < info_annul['places_total']:
                info_annul['places_restantes'] += 1
            
            st.success(f"Annulation réussie pour {passager_annul} sur {trajet_annul}.")
            st.write(f"Places restantes : {info_annul['places_restantes']} / {info_annul['places_total']}")

# ====================================================================
# TAB 4 : AFFICHAGE DES PASSAGERS
# ====================================================================
with tab4:
    st.header("4. Afficher les passagers d’un train")
    
    trajet_passagers = st.selectbox(
        "Sélectionnez un trajet :", 
        options=list(trains.keys()), 
        key="list_passagers"
    )
    
    passagers = trains[trajet_passagers]['passagers']
    
    st.subheader(f"Passagers pour {trajet_passagers}")
    if passagers:
        liste_triee = sorted(list(passagers))
        st.write(f"Total des passagers : {len(liste_triee)}")
        st.code('\n'.join([f"{i}. {nom}" for i, nom in enumerate(liste_triee, 1)]))
    else:
        st.write("Aucun passager enregistré pour ce trajet.")

# ====================================================================
# TAB 5 : TRAINS COMPLETS
# ====================================================================
with tab5:
    st.header("5. Voir les trains complets")

    trains_complets_trouves = [
        trajet for trajet, info in trains.items() 
        if info['places_restantes'] == 0
    ]
    
    if trains_complets_trouves:
        st.error("Les trains suivants sont complets :")
        for trajet in trains_complets_trouves:
            st.markdown(f"- **{trajet}**")
    else:
        st.success("Aucun train n'est actuellement complet.")

# Bouton Quitter
if st.button("0. Quitter l'application", type="primary"):
    st.stop()
