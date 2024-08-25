# output_consistency.py
from core_functionality import Batalha
from pokemon import Onix, Pikachu

def test_batalhar_output():
    batalha_teste = Batalha(Onix(50), Pikachu(1))
    assert batalha_teste.batalhar() == 'Player'

    batalha_teste = Batalha(Pikachu(1), Onix(50))
    assert batalha_teste.batalhar() == 'Inimigo'
