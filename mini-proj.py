trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}

for trajet, info_traj in trains.items():
    places_total=info_traj['places_total']
    places_restante=info_traj['places_restantes']
    passager=info_traj['passagers']
    print(f"Trajet {trajet} : {places_restante} places restantes /{places_total}")