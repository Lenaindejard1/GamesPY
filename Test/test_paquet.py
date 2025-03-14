import pytest
import coverage
from Games.Util.Paquet import Paquet

def test_calculer_nombre_paquets():
    paquet = Paquet(4, 13)
    assert paquet.calculer_nombre_paquets() == 1

def test_generer_cartes():
    paquet = Paquet(4, 13)
    assert len(paquet.cartes) == 52

def test_tirer_carte():
    paquet = Paquet(4, 13)
    carte = paquet.tirer_carte()
    assert carte is not None
    assert len(paquet.cartes) == 51

def test_afficher_nombre_paquets(capfd):
    paquet = Paquet(4, 13)
    paquet.afficher_nombre_paquets()
    captured = capfd.readouterr()
    assert "Nombre de paquets générés : 1" in captured.out

def test_nombre_cartes_insuffisant():
    with pytest.raises(ValueError):
        Paquet(10, 10)

if __name__ == "__main__":
    pytest.main()