import random
from core_functionality import AtaqueComFraqueza, AtaqueNormal, AtaqueComForca

def test_output_consistency():
    valor_ataque_base = 50
    level_atual = 10

    ataque_com_fraqueza = AtaqueComFraqueza()
    ataque_normal = AtaqueNormal()
    ataque_com_forca = AtaqueComForca()

    results_fraqueza = [ataque_com_fraqueza.calcular_ataque(valor_ataque_base, level_atual) for _ in range(10)]
    results_normal = [ataque_normal.calcular_ataque(valor_ataque_base, level_atual) for _ in range(10)]
    results_forca = [ataque_com_forca.calcular_ataque(valor_ataque_base, level_atual) for _ in range(10)]

    print("Results for AtaqueComFraqueza:")
    print(results_fraqueza)

    print("Results for AtaqueNormal:")
    print(results_normal)

    print("Results for AtaqueComForca:")
    print(results_forca)

if __name__ == "__main__":
    test_output_consistency()

