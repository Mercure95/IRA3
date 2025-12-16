from datetime import datetime

from cars import Car, Motorcycle, Truck
from customer import Customer
from rental import Rental


def main():
    client1 = Customer(1, "B", "Alban", 30, "B123456")
    client2 = Customer(2, "O", "Mike", 22, "C654321")

    v1 = Car(1, "Bugatti", "Chiron Super Sport", "Hypercars", 3000, "disponible")
    v2 = Car(2, "Koenigsegg", "Jesko Absolut", "Hypercars", 3500, "disponible")
    v3 = Car(3, "Pagani", "Huayra BC", "Hypercars", 2800, "disponible")
    v4 = Car(4, "McLaren", "Speedtail", "Hypercars", 2700, "loué")
    v5 = Car(5, "Lamborghini", "Sián FKP 37", "Hypercars", 2600, "disponible")
    v6 = Truck(2, "Mercedes", "Actros", "Camion", 120, "disponible")
    v7 = Motorcycle(3, "Yamaha", "MT-07", "Moto", 60, "loué")

    date_debut = datetime(2024, 6, 1)
    date_fin = datetime(2024, 6, 5)

    location1 = Rental(client1, v1, date_debut, date_fin)

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
