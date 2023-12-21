

class Zone:
    def __init__(
        self, nom, population, gps, liste_poubelles, calendrier_collecte, collecteurs
    ):
        self.nom = nom
        self.population = population
        self.gps = gps
        self.liste_poubelles = liste_poubelles
        self.calendrier_collecte = calendrier_collecte
        self.collecteurs = collecteurs

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {
            "nom": self.nom,
            "population": self.population,
            "gps": self.gps,
            "liste_poubelles": self.liste_poubelles,
            "calendrier_collecte": self.calendrier_collecte,
            "collecteurs": self.collecteurs,
        }
