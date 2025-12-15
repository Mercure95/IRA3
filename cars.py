class Vehicle:
    def __init__(self, id_vehicule, marque, modele, categorie, tarif, etat="disponible"):
        self.id_vehicule = id_vehicule
        self.marque = marque
        self.modele = modele
        self.categorie = categorie
        self.tarif = tarif
        self.etat = etat

    def est_disponible(self):
        return self.etat == "disponible"


class Car(Vehicle):
    def __init__(self, id_vehicule, marque, modele, tarif):
        super().__init__(id_vehicule, marque, modele, "Voiture", tarif)


class Truck(Vehicle):
    def __init__(self, id_vehicule, marque, modele, tarif):
        super().__init__(id_vehicule, marque, modele, "Camion", tarif)


class Motorcycle(Vehicle):
    def __init__(self, id_vehicule, marque, modele, tarif):
        super().__init__(id_vehicule, marque, modele, "Moto", tarif)
