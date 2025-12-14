from datetime import datetime
from customer import Customer 

class MockVehicle:
    def __init__(self, marque, tarif):
        self.marque = marque
        self.tarif = tarif

        
class Rental:
    def __init__(self, client, vehicule, date_debut, date_fin):
        self.client = client      
        self.vehicule = vehicule  
        self.date_debut = date_debut 
        self.date_fin = date_fin    
        self.cout_total = 0.0    
        self.statut = "active" 

    def calculer_duree(self):
        pass

    def est_valide(self):
        return self.date_fin > self.date_debut

    def calculer_cout_total(self):
        delta = self.date_fin - self.date_debut
        jours = max(1, delta.days)
        tarif_journalier = self.vehicule.tarif 
        self.cout_total = (jours * tarif_journalier) + self.penalite
        return self.cout_total

    def ajouter_penalite(self, montant):
        self.penalite += montant
        self.calculer_cout_total()

    def terminer_location(self):
        self.statut = "terminée"
        self.calculer_cout_total()
        print(f"Location terminée. Total à payer : {self.cout_total}€")

    def __str__(self):
        return f"Loc {self.vehicule.marque} pour {self.client.nom} ({self.cout_total}€)"