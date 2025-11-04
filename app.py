import streamlit as st
import pandas as pd
import sys # Pour l'exit propre (remplace le 'Quitter' du menu)

# --- 1. CONFIGURATION ET INITIALISATION DES DONNÉES ---

st.set_page_config(layout="wide", page_title="Réservation Train")
st.title("🚆 Système de Réservation de Trains (Streamlit)")

# Utilisation de st.session_state pour persister les données 'trains'
if 'trains' not in st.session_state:
    st.session_state.trains = {
        'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
        'TUN-ROM': {'places_total': 3, 'places_restantes': 0, 'passagers': set()},
        'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
    }

trains = st.session_state.trains

# --- 2. FONCTIONS DE PRÉSENTATION UTILITAIRES ---

def get_trains_df(current_trains):
    """Prépare un DataFrame pour l'affichage tabulaire."""
    data = []
    for trajet, info in current_trains.items():
        data.append({
            'Trajet': trajet,
            'Places Totales': info['places_total'],
            'Places Restantes': info['places_restantes'],
            'Passagers (Qté)': len(info['passagers']),
            'Statut': '🛑 Complet' if info['places_restantes'] == 0 else '✅ Disponible'
        })
    return pd.DataFrame(data)


# --- 3. MISE EN PLACE DE L'INTERFACE (ONGLETS) ---

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1️⃣ Afficher Trains", 
    "2️⃣ Réserver", 
    "3️⃣ Annuler", 
    "4️⃣ Passagers", 
    "5️⃣ Trains Complets"
])

# ====================================================================
# TAB 1 : AFFICHAGE DES TRAINS (Méthode 1)
# ====================================================================
with tab1:
    st.header("1️⃣ Afficher les trains")
    st.dataframe(get_trains_df(trains), use_container_width=True, hide_index=True)

    st.markdown("---")
    st.subheader("Format Console (Méthode 1 originale)")
    # Réplication de votre fonction d'affichage pour information
    for trajet, info in trains.items():
        st.write(f"Trajet **{trajet}** : **{info['places_restantes']}** places restantes / {info['places_total']}")

# ====================================================================
# TAB 2 : RÉSERVER UNE PLACE (Méthode 2)
# ====================================================================
with tab2:
    st.header("2️⃣ Réserver une place")
    
    # 1. Sélection du trajet
    trajet_choisi = st.selectbox(
        "Choisissez le trajet :", 
        options=list(trains.keys()),
        key="res_trajet"
    )
    
    # Affichage en temps réel du statut
    current_info = trains[trajet_choisi]
    st.info(f"Places restantes pour **{trajet_choisi}** : {current_info['places_restantes']}/{current_info['places_total']}")
    
    # 2. Entrée du nom du passager
    nom_passager = st.text_input("Nom du passager :", key="res_nom")
    
    # 3. Lancement de la réservation
    if st.button("Confirmer la réservation", key="btn_reserver"):
        
        # Vérification 1 : Nom vide
        if not nom_passager.strip():
            st.error("❌ Le nom du passager ne peut pas être vide.")
            sys.exit() # Simule l'arrêt du flux comme votre 'return'
        
        # Vérification 2 : Places restantes
        if current_info['places_restantes'] == 0:
            st.error(f"❌ Désolé, le trajet {trajet_choisi} est complet.")
        
        # Vérification 3 : Double réservation (utilisé 'not in' dans votre code)
        elif nom_passager.strip() in current_info['passagers']:
            st.warning(f"❌ {nom_passager} a déjà une réservation sur ce trajet.")
            
        else:
            # Opération de réservation réussie
            current_info['passagers'].add(nom_passager.strip())
            current_info['places_restantes'] -= 1
            
            st.success(f"✅ Réservation OK ! Passager: {nom_passager.strip()}, Trajet: {trajet_choisi}")
            st.info(f"Nouvelles places restantes: {current_info['places_restantes']}")

# ====================================================================
# TAB 3 : ANNULER UNE RÉSERVATION (Méthode 3)
# ====================================================================
with tab3:
    st.header("3️⃣ Annuler une réservation")

    trajet_annul = st.selectbox(
        "Choisissez le trajet pour l'annulation :", 
        options=list(trains.keys()),
        key="annul_trajet"
    )
    
    info_annul = trains[trajet_annul]
    
    # Crée une liste des passagers pour ce trajet pour l'utilisateur
    passagers_existants = list(info_annul['passagers'])
    
    # 1. Sélection du passager (on ajoute une option vide pour la sélection initiale)
    passager_annul = st.selectbox(
        "Passager à annuler :", 
        options=[''] + passagers_existants, 
        key="annul_nom"
    )

    if st.button("Confirmer l'annulation", key="btn_annuler"):
        
        # Vérification 1 : Passager sélectionné
        if not passager_annul:
             st.error("Veuillez sélectionner un passager à annuler.")
        
        # Vérification 2 : Passager inscrit (normalement géré par le selectbox, mais sécurité)
        elif passager_annul not in info_annul['passagers']:
            st.error(f"❌ Le passager {passager_annul} n'a pas de réservation sur {trajet_annul}.")
            
        else:
            # Opération d'annulation
            info_annul['passagers'].remove(passager_annul)
            
            # Votre logique vérifie si places_restantes < places_total avant d'incrémenter
            if info_annul['places_restantes'] < info_annul['places_total']:
                info_annul['places_restantes'] += 1
            
            st.success(f"✅ Annulation OK pour **{passager_annul}** sur **{trajet_annul}**.")
            st.info(f"Places restantes : {info_annul['places_restantes']} / {info_annul['places_total']}")

# ====================================================================
# TAB 4 : AFFICHAGE DES PASSAGERS (Méthode 4)
# ====================================================================
with tab4:
    st.header("4️⃣ Afficher les passagers d’un train")
    
    trajet_passagers = st.selectbox(
        "Sélectionnez un trajet :", 
        options=list(trains.keys()), 
        key="list_passagers"
    )
    
    passagers = trains[trajet_passagers]['passagers']
    
    st.subheader(f"Passagers pour {trajet_passagers}")
    if passagers:
        # Afficher la liste triée
        liste_triee = sorted(list(passagers))
        st.markdown(f"**Total des passagers : {len(liste_triee)}**")
        # Affichage sous forme de liste numérotée
        st.code('\n'.join([f"{i}. {nom}" for i, nom in enumerate(liste_triee, 1)]))
    else:
        st.info("Aucun passager n'est encore enregistré pour ce trajet.")

# ====================================================================
# TAB 5 : TRAINS COMPLETS (Méthode 5)
# ====================================================================
with tab5:
    st.header("5️⃣ Voir les trains complets")

    trains_complets_trouves = [
        trajet for trajet, info in trains.items() 
        if info['places_restantes'] == 0
    ]
    
    if trains_complets_trouves:
        st.error("🛑 Les trains suivants sont **COMPLETS** :")
        for trajet in trains_complets_trouves:
            st.markdown(f"**- {trajet}**")
    else:
        st.success("Bonne nouvelle ! Aucun train n'est actuellement complet.")

# Ajout d'un bouton de Quitter (0) hors des onglets
if st.button("0️⃣ Quitter l'application", type="primary"):
    st.balloons()
    st.stop() # Arrête l'exécution de l'application Streamlit