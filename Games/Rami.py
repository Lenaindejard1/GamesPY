from Games.Util.Trier import *
from Games.Util.Paquet import *
from Games.Util.Player import *

class JeuDeRami:
    def __init__(self, noms_joueurs, cartes_par_joueur):
        self.paquet = Paquet(len(noms_joueurs), cartes_par_joueur)
        self.joueurs = [Joueur(nom) for nom in noms_joueurs]
        self.distribuer_cartes()

    def distribuer_cartes(self):
        for _ in range(cartes_par_joueur):
            for joueur in self.joueurs:
                joueur.piocher(self.paquet)

    def montrer_mains(self):
        for joueur in self.joueurs:
            main_triee = TrierJeu.trier(joueur.main)
            print(f"Main de {joueur.nom} : {', '.join(map(str, main_triee))}")

noms_joueurs = ["Lenain", "Diabolofraise", "RaelMonty"]
cartes_par_joueur = 7
jeu = JeuDeRami(noms_joueurs, cartes_par_joueur)
jeu.paquet.afficher_nombre_paquets()
jeu.montrer_mains()