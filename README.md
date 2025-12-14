# Car Rental System

## Description

Ce projet est une application de gestion de location de voitures développée selon les principes de la programmation orientée objet.
Elle permet à une agence de location de gérer son parc automobile, ses clients et ses locations, tout en assurant le calcul des coûts et la génération de rapports.

## Objectifs

- Gérer une flotte de véhicules
- Gérer les clients
- Effectuer et suivre les locations
- Calculer le coût total d’une location
- Générer des rapports et statistiques

## Fonctionnalités

### 1. Gestion de la flotte automobile

- Hiérarchie de classes :
  - `Vehicle`
  - `Car`
  - `Truck`
  - `Motorcycle`
- Attributs :
  - `id`
  - `marque`
  - `modele`
  - `categorie`
  - `tarif`
  - `etat`
- Option avancée :
  - Gestion de l’entretien des véhicules

### 2. Gestion des clients

- Classe `Customer`
- Attributs :
  - `id`
  - `nom`
  - `prenom`
  - `age`
  - `permis`
  - `historique`
- Règles métier :
  - Âge minimum requis selon le type de véhicule

### 3. Système de réservation (Location)

- Classe `Rental`
- Données :
  - Client
  - Véhicule
  - Dates de début et de fin
  - Coût total
- Règles :
  - Vérification de la disponibilité
  - Validation des dates
  - Gestion des pénalités en cas de retard

### 4. Système central

- Classe principale `CarRentalSystem`
- Responsabilités :
  - Gestion des véhicules
  - Gestion des clients
  - Gestion des locations
  - Recherche et filtrage
  - Génération de rapports

## Rapports

- Véhicules disponibles
- Locations en cours
- Chiffre d’affaires
- Statistiques générales

## Structure du projet

- Code organisé en modules
- Diagramme UML des classes
- Tests unitaires
- Documentation

## Technologies

- Programmation orientée objet
- Langage : selon l’implémentation du projet

## Livrables

- Dépôt GitHub contenant le code source
- Diagramme UML
- Fichier README
- Tests unitaires

## Auteur

GOASDUFF Pierre / SOICHET Quentin
