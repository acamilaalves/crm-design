# Guardar a função de busca.

def buscar_marcas_do_cliente(marcas, cliente_id):
    marcas_encontradas = []

    for marca in marcas:
        if marca["cliente_id"] == cliente_id:
            marcas_encontradas.append(marca)

    return marcas_encontradas