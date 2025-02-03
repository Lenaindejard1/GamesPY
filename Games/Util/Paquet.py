import random
from Games.Util.Carte import *

class Paquet:
    couleurs = ["♥️", "♦️", "♣️", "♠️"]
    valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    joker = "🃏"  # Icone Windows pour le Joker

    def __init__(self, nombre_joueurs, cartes_par_joueur):
        self.nombre_cartes = nombre_joueurs * cartes_par_joueur
        self.nombre_paquets = self.calculer_nombre_paquets()
        self.cartes = []
        self.generer_cartes()
        random.shuffle(self.cartes)

    def calculer_nombre_paquets(self):
        cartes_standard = len(self.couleurs) * len(self.valeurs) + 2  # 52 cartes + 2 jokers
        nombre_paquets = (self.nombre_cartes + cartes_standard - 1) // cartes_standard
        return nombre_paquets

    def generer_cartes(self):
        cartes_standard = [Carte(couleur, valeur) for couleur in self.couleurs for valeur in self.valeurs]
        jokers = [Carte(self.joker, "Joker") for _ in range(2)]
        cartes_totales = cartes_standard + jokers

        cartes_multiples = cartes_totales * self.nombre_paquets
        random.shuffle(cartes_multiples)

        if self.nombre_cartes > len(cartes_multiples):
            raise ValueError("Nombre de cartes demandé dépasse le nombre de cartes disponibles même avec plusieurs paquets.")

        self.cartes = cartes_multiples[:self.nombre_cartes]

    def tirer_carte(self):
        return self.cartes.pop() if self.cartes else None

    def afficher_nombre_paquets(self):
        print(f"Nombre de paquets générés : {self.nombre_paquets}")