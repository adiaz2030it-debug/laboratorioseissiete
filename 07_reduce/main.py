"""EJERCICIO 07 — Total de ventas

ENUNCIADO
Cada pedido es una tupla (producto, precio_unitario, cantidad).
Usa map con lambda para obtener los subtotales y reduce con lambda para sumarlos.
Importa reduce del módulo functools. Usa 0 como valor inicial de reduce.
No uses sum, ciclos ni comprensiones. Los valores son enteros no negativos.
Para [] devuelve 0.

Entrada: [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
Resultado esperado: 69

ENTREGA
Completa la implementación sin cambiar los nombres ni los parámetros.
Ejecuta el archivo y compara lo impreso con el resultado del enunciado.
Añade al menos otro ejemplo usando print y escribe en un comentario qué esperas.
Al terminar: git commit -m "Resuelve ejercicio 07".

"""

from functools import reduce


def total_ventas(pedidos):
    subtotales = map(lambda pedido: pedido[1] * pedido[2], pedidos)
    return reduce(lambda acumulado, subtotal: acumulado + subtotal, subtotales, 0)


# Ejemplo de uso:
pedidos = [("cafe", 10, 2), ("te", 8, 3), ("torta", 25, 1)]
print(total_ventas(pedidos))  

# Otros ejemplos 
print(total_ventas([("jugo", 15, 2), ("galleta", 4, 0), ("pan", 6, 3)]))  
print(total_ventas([])) 