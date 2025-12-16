# Système de location de véhicules (Python)

## Présentation

Ce dépôt contient un mini-système de location basé sur la programmation orientée objet.  
Le projet est découpé en modules Python : véhicules, clients, locations, et un point d’entrée (`main.py`) qui démontre l’utilisation de l’ensemble.

Le cahier des charges de base correspond à un système permettant de gérer un parc de véhicules, des clients, et de créer des locations avec calcul automatique du coût. :contentReference[oaicite:0]{index=0}

## Structure du dépôt

- `cars.py` : hiérarchie des véhicules (`Vehicle`, `Car`, `Truck`, `Motorcycle`) :contentReference[oaicite:1]{index=1}  
- `customer.py` : gestion des clients (`Customer`) :contentReference[oaicite:2]{index=2}  
- `rental.py` : gestion des locations (`Rental`) : validation des dates, coût total, pénalités, statut :contentReference[oaicite:3]{index=3}  
- `main.py` : point d’entrée, instanciation de clients/véhicules et création d’une location :contentReference[oaicite:4]{index=4}

## Détails des modules

### 1) Véhicules (`cars.py`)

#### Classe `Vehicle`
Représente un véhicule générique.

Attributs :
- `id` : identifiant du véhicule
- `marque`
- `modele`
- `categorie`
- `tarif` : prix journalier
- `etat` : par exemple `disponible`, `loué`, `entretien`

Méthodes :
- `__str__()` : affichage lisible du véhicule

#### Classes filles
- `Car`
- `Truck`
- `Motorcycle`

Ces classes héritent de `Vehicle` et réutilisent l’initialisation de la classe parente via `super().__init__`.

### 2) Clients (`customer.py`)

#### Classe `Customer`
Représente un client.

Attributs :
- `id_client`
- `nom`, `prenom`
- `age`
- `permis`
- `historique_locations` : liste des locations effectuées

Méthodes :
- `__str__()` : affichage du client
- `verifier_age(age_minimum)` : renvoie `True` si l’âge du client respecte l’âge minimum
- `ajouter_location_historique(location)` : ajoute une location à l’historique

### 3) Locations (`rental.py`)

#### Classe `Rental`
Représente une location entre un client et un véhicule, sur une période donnée.

Attributs :
- `client` : instance de `Customer`
- `vehicule` : instance de `Vehicle` (ou `Car`/`Truck`/`Motorcycle`)
- `date_debut`, `date_fin` : dates (objets `datetime`)
- `penalite` : montant ajouté au total (par défaut 0)
- `cout_total` : calculé automatiquement
- `statut` : `active` ou `terminée`

Méthodes :
- `est_valide()` : vérifie que `date_fin > date_debut`
- `calculer_cout_total()` :
  - calcule la durée en jours (minimum 1)
  - multiplie par le `tarif` journalier du véhicule
  - ajoute la pénalité
- `ajouter_penalite(montant)` : incrémente la pénalité et recalcule le total
- `terminer_location()` : passe le statut à `terminée` et affiche le total
- `__str__()` : affichage court de la location

## Exécution

Lancer le programme :

```bash
python main.py
