# Executar a demonstração do CRM

from servicos import buscar_marcas_do_cliente

cliente = [
    {
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
]

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

resultado = buscar_marcas_do_cliente(marcas, 1)

for marca in resultado:
    print(marca["nome"])