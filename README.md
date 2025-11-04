Mini Projet TD1


Objectif du projet 

L’objectif de ce projet est de concevoir un petit programme de gestion de réservations de trains. Le programme sera entièrement en console, et devra permettre de gérer plusieurs trajets, des passagers, et des places disponibles. Il s’agit de manipuler les structures de base du langage Python : dictionnaires, ensembles (set), tuples, listes, boucles et conditions. Aucune base de données, ni interface graphique n’est requise. 

Description générale 

Une société ferroviaire souhaite un programme simple pour gérer les réservations de ses trains. Chaque train est défini par un trajet de trajet (ex. 'TUN-PAR'), un nombre total de places, un nombre de places restantes, et la liste des passagers inscrits (sans doublons). Le programme doit permettre à un agent de : 

1. Afficher tous les trajets disponibles et leur nombre de places restantes. 
2. Réserver une place pour un passager donné sur un trajet choisi. 
3. Annuler une réservation existante. 
4. Afficher la liste des passagers d’un train donné. 
5. Afficher les trains complets. 
6. (Bonus) Générer un ticket de réservation sous forme de tuple. 

Structure de départ suggérée 

Vous pouvez utiliser la structure suivante : 

trains = { 
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()}, 
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()}, 
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()}, 
} 

Fonctionnalités attendues 

1️⃣ Afficher les trains 
- Afficher chaque trajet avec le nombre total de places et le nombre de places restantes. 
- Exemple : TUN-PAR → 3 places restantes / 5 

2️⃣ Réserver une place 
- Demander le nom du passager et le code du trajet. 
- Vérifier si le trajet existe et s’il reste des places. 
- Ajouter le passager et diminuer les places restantes. 
- Empêcher un même passager de réserver deux fois. 
- Afficher un message clair en cas d’erreur ou de succès. 

3️⃣ Annuler une réservation 
- Supprimer un passager de la liste et augmenter les places restantes. 

4️⃣ Afficher les passagers d’un train 
- Afficher la liste triée des passagers d’un trajet donné. 

5️⃣ Afficher les trains complets 
- Lister les trains dont le nombre de places restantes est égal à zéro. 

6️⃣ (Bonus) Génération de ticket 
- Lors d’une réservation, créer un tuple (nom, trajet, numéro_de_place). 

Menu principal  

Le programme doit tourner dans une boucle principale avec un menu textuel : 
 
=== MENU RÉSERVATION TRAIN === 
1️⃣  Afficher les trains 
2️⃣  Réserver une place 
3️⃣  Annuler une réservation 
4️⃣  Afficher les passagers d’un train 
5️⃣  Voir les trains complets 
0️⃣  Quitter 

Livrable attendu 

- Repo GitHub 

- Demo 
