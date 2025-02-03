class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def piocher(self, paquet):
        carte = paquet.tirer_carte()
        if carte:
            self.main.append(carte)

    def montrer_main(self):
        return ', '.join(map(str, self.main))