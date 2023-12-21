import math


def haversine_distance(point1, point2):
    # Formule de la distance haversine entre deux points GPS
    R = 6371  # Rayon moyen de la Terre en kilomètres
    lat1, lon1 = math.radians(point1[0]), math.radians(point1[1])
    lat2, lon2 = math.radians(point2[0]), math.radians(point2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance


def farthest_insertion(points):
    # Initialiser le chemin avec le premier point
    current_path = [points[0]]
    remaining_points = set(points[1:])

    while remaining_points:
        # Trouver le point le plus éloigné du chemin actuel
        farthest_point = max(
            remaining_points,
            key=lambda point: min(
                haversine_distance(point, path_point) for path_point in current_path
            ),
        )

        # Trouver l'indice du point le plus proche dans le chemin actuel
        nearest_index = min(
            range(len(current_path)),
            key=lambda i: haversine_distance(farthest_point, current_path[i]),
        )

        # Insérer le point le plus éloigné dans le chemin
        current_path.insert(nearest_index + 1, farthest_point)

        # Mettre à jour les points restants
        remaining_points.remove(farthest_point)

    return current_path


# Exemple de coordonnées GPS fictives
latitude1, longitude1 = 37.7749, -122.4194  # San Francisco, CA
latitude2, longitude2 = 34.0522, -118.2437  # Los Angeles, CA
latitude3, longitude3 = 40.7128, -74.0060  # New York, NY
latitude4, longitude4 = 41.8781, -147.6298  # Chicago, IL

# Liste de points GPS
points_gps = [
    (latitude1, longitude1),
    (latitude2, longitude2),
    (latitude3, longitude3),
    (latitude4, longitude4),
]

# Appeler la fonction farthest_insertion avec ces points
optimized_path = farthest_insertion(points_gps)

# Afficher le chemin optimisé
print(points_gps)
print(optimized_path)
