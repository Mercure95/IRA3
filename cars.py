class Vehicle:
    def __init__(self, vid, marque, modele, categorie, tarif, etat):
        self.id = vid
        self.marque = marque
        self.modele = modele
        self.categorie = categorie
        self.tarif = tarif
        self.etat = etat  # "disponible", "loué", "entretien"

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.categorie})"


class Car(Vehicle):
    def __init__(self, vid, marque, modele, categorie, tarif, etat):
        super().__init__(vid, marque, modele, categorie, tarif, etat) #appel classe parente depuis enfant


class Truck(Vehicle):
    def __init__(self, vid, marque, modele, categorie, tarif, etat):
        super().__init__(vid, marque, modele, categorie, tarif, etat)


class Motorcycle(Vehicle):
    def __init__(self, vid, marque, modele, categorie, tarif, etat):
        super().__init__(vid, marque, modele, categorie, tarif, etat)
