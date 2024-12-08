""" Módulo com funções para gerar combinações de elementos. """


from typing import Generator


def product(operators, positions):
    """
    Gera todas as combinações possíveis de operadores usando recursão.

    :param operators: Lista de operadores disponíveis (ex: ['+', '*', '||']).
    :param positions: Número de posições onde os operadores podem ser colocados.
    :return: Lista de combinações de operadores.
    """
    # caso base: nenhuma posição restante, retorne lista vazia (uma combinação)
    if positions == 0:
        return [[]]
    # passo recursivo: adicionar cada operador à combinação e recorra
    combinations = []
    for op in operators:
        for rest in product(operators, positions - 1):
            combinations.append([op] + rest)
    return combinations


def custom_product(*iterables, repeat=1) -> Generator:
    """
    Implementa um produto cartesiano semelhante ao itertools.product.
    
    :param iterables: Iteráveis cujos produtos cartesianos serão gerados.
    :param repeat: Quantas vezes o produto deve ser repetido.
    :return: Um gerador que produz as combinações.
    """
    pools = [tuple(pool) for pool in iterables] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
    return result
