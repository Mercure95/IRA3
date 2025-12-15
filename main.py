from datetime import datetime

from cars import Car, Motorcycle, Truck
from customer import Customer
from rental import Rental


def main():
    client1 = Customer(1, "Dupont", "Jean", 30, "B123456")
    client2 = Customer(2, "Martin", "Alice", 22, "C654321")

    car1 = Car(1, "Peugeot", "208", 45)
    truck1 = Truck(2, "Renault", "Master", 80)
    moto1 = Motorcycle(3, "Yamaha", "MT-07", 35)

    date_debut = datetime(2024, 6, 1)
    date_fin = datetime(2024, 6, 5)

    location1 = Rental(client1, car1, date_debut, date_fin)

    if location1.est_valide():
        cout = location1.calculer_cout_total()
        client1.ajouter_location_historique(location1)

        print("Location créée avec succès")
        print(location1)
        print(f"Coût total : {cout} €")
    else:
        print("Erreur : dates de location invalides")

    location1.terminer_location()
    print("\nHistorique des locations du client :")
    for loc in client1.historique_locations:
        print(loc)


if __name__ == "__main__":
    main()
