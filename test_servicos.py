# Conferir se a função funciona conforme esperado.

from servicos import buscar_marcas_do_cliente

marcas = [
    {"id": 1, "nome": "Marca A", "cliente_id": 1},
    {"id": 2, "nome": "Marca B", "cliente_id": 1},
    {"id": 3, "nome": "Marca C", "cliente_id": 2}
]

# Cliente 1: deve retornar exatamente as marcas 1 e 2
resultado = buscar_marcas_do_cliente(marcas, 1)

ids_encontrados = []

for marca in resultado:
    ids_encontrados.append(marca["id"])

assert ids_encontrados == [1, 2], "Erro ao buscar marcas do cliente 1"


# Cliente 2: deve retornar apenas a marca 3
resultado = buscar_marcas_do_cliente(marcas, 2)

assert len(resultado) == 1, "O cliente 2 deve ter uma marca"
assert resultado[0]["id"] == 3, "A marca retornada está incorreta"


# ID sem marcas: deve retornar uma lista vazia
resultado = buscar_marcas_do_cliente(marcas, 99)

assert resultado == [], "A busca deveria retornar uma lista vazia"


print("Todos os testes passaram!")