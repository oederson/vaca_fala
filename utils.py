def formatar_array(array_desformatado):
    lista = array_desformatado
    maior_item_do_array = max(lista, key=len)
    lista = list(map(lambda x: x + " " * (len(maior_item_do_array) - len(x)), lista))
    return lista
