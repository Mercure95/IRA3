class Customer:
    def __init__(self, id_client,nom,prenom,age,permis):
        self.id_client=id_client
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.permis=permis
        self.historique_locations=[]
    
    def __str__(self):
        return f"Client {self.id_client}: {self.nom} {self.prenom} ({self.age} ans) - Permis: {self.permis}"
    
    def verifier_age(self, age_minimum):
        return self.age >= age_minimum
    
    def ajouter_location_historique(self, location):
        self.historique_locations.append(location)

    
        