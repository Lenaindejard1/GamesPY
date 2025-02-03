class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"