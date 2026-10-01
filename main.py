cliente = {
    "id": 1,
    "nome": "Camila Lima",
    "tipo": "PF",
    "telefone": "",
    "email": "",
    "ativo": True
},
{
    "id": 2,
    "nome": "Carlos Silva",
    "tipo": "PF",
    "telefone": "",
    "email": "",
    "ativo": True
}

marcas = [
    {
        "id": 1,
        "nome": "Casa dos Cookies",
        "cliente_id": 1
    },
    {
        "id": 2,
        "nome": "Pequenos Discípulos",
        "cliente_id": 1
    },
    {
        "id": 3,
        "nome": "Reformas Certas",
        "cliente_id": 2
    }
]

def buscar_marcas_do_cliente(marcas, cliente_id):
    marcas_encontradas = []

    for marca in marcas:
        if marca["cliente_id"] == cliente_id:
            marcas_encontradas.append(marca)

    return marcas_encontradas


resultado = buscar_marcas_do_cliente(marcas, 1)

for marca in resultado:
    print(marca["nome"])

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