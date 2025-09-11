def imprimir_tipos(lista):
    for elemento in lista:
        print(f"{elemento} - Tipo:{type(elemento).__name__}")

minha_lista = [1, "texto", 3.14, True, [1, 2, 3], {"chave": "valor"}]
imprimir_tipos(minha_lista)
print(minha_lista)
