"""EJERCICIO 01 - Resumen de ventas

ENUNCIADO
Recibes una lista de tuplas (producto, cantidad). Devuelve un diccionario con:
- productos: set con los nombres vendidos.
- unidades: total de unidades vendidas.
- por_producto: diccionario con las cantidades acumuladas por producto.
Usa ciclos, un set y un diccionario. No modifiques la entrada.
Las cantidades son enteros positivos. Para [] devuelve estructuras vacías y total 0.

Ejemplo:
Entrada: [("cafe", 2), ("te", 1), ("cafe", 3)]
Resultado: {"productos": {"cafe", "te"}, "unidades": 6,
            "por_producto": {"cafe": 5, "te": 1}}
El orden de los elementos del set puede cambiar.

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 01".
"""


def resumir_ventas(ventas):
    productos = set()
    unidades = 0
    por_producto = {}

    for producto, cantidad in ventas:
        # Añadir al conjunto de productos
        productos.add(producto)
        
        # Sumar al total general de unidades
        unidades += cantidad
        
        # Acumular la cantidad en el diccionario por producto
        if producto in por_producto:
            por_producto[producto] += cantidad
        else:
            por_producto[producto] = cantidad

    return {
        "productos": productos,
        "unidades": unidades,
        "por_producto": por_producto
    }


# Ejemplo de uso:
ventas = [("cafe", 2), ("te", 1), ("cafe", 3)]
print(resumir_ventas(ventas))

# Ejemplo adicional:
# Resultado esperado:
# {'productos': {'manzana', 'pan'}, 'unidades': 12, 'por_producto': {'pan': 7, 'manzana': 5}}
ventas_ejemplo2 = [("pan", 4), ("manzana", 5), ("pan", 3)]
print(resumir_ventas(ventas_ejemplo2))