import random
from core_functionality import AtaqueComFraqueza, AtaqueNormal, AtaqueComForca

def test_boundary_conditions():
    # Testing with minimum and maximum values
    min_valor_ataque_base = 0
    max_valor_ataque_base = 1000
    min_level_atual = 0
    max_level_atual = 100

    ataque_com_fraqueza = AtaqueComFraqueza()
    ataque_normal = AtaqueNormal()
    ataque_com_forca = AtaqueComForca()

    print("Testing AtaqueComFraqueza with min and max values:")
    print(ataque_com_fraqueza.calcular_ataque(min_valor_ataque_base, min_level_atual))
    print(ataque_com_fraqueza.calcular_ataque(max_valor_ataque_base, max_level_atual))

    print("Testing AtaqueNormal with min and max values:")
    print(ataque_normal.calcular_ataque(min_valor_ataque_base, min_level_atual))
    print(ataque_normal.calcular_ataque(max_valor_ataque_base, max_level_atual))

    print("Testing AtaqueComForca with min and max values:")
    print(ataque_com_forca.calcular_ataque(min_valor_ataque_base, min_level_atual))
    print(ataque_com_forca.calcular_ataque(max_valor_ataque_base, max_level_atual))

if __name__ == "__main__":
    test_boundary_conditions()
