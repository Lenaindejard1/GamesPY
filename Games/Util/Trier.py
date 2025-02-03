class TrierJeu:
    ordre_valeurs = {
        "Joker": 14, "As": 13, "Roi": 12, "Dame": 11, "Valet": 10,
        "10": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1
    }

    @staticmethod
    def trier(main):
        return sorted(main, key=lambda carte: TrierJeu.ordre_valeurs[carte.valeur], reverse=True)