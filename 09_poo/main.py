"""EJERCICIO 09 — Clase Producto

ENUNCIADO
Implementa Producto con atributos de instancia nombre, precio y stock.
El constructor recibe esos tres valores. Precio y stock son enteros no negativos.
- valor_inventario(): devuelve precio * stock, sin modificar los atributos.
- vender(cantidad): si cantidad > 0 y hay suficiente stock, descuenta esa
  cantidad y devuelve True. En caso contrario devuelve False sin cambiar stock.
Las cantidades son enteras; no necesitas validar otros tipos.
Comprueba con print que dos instancias mantienen su stock de forma independiente.
No se requiere herencia ni métodos especiales adicionales al constructor.

ENTREGA
Completa la clase, ejecuta y compara los resultados con los comentarios.
Añade otro ejemplo con print y su resultado esperado en un comentario.
Haz un commit: "Resuelve ejercicio 09".
"""


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def valor_inventario(self):
        return self.precio * self.stock

    def vender(self, cantidad):
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False


cafe = Producto("cafe", 10, 5)
te = Producto("te", 8, 3)
print(cafe.valor_inventario())  
print(cafe.vender(2))        
print(cafe.valor_inventario())  
print(cafe.vender(4))       
print(cafe.vender(0))        
print(cafe.vender(-1))       
print(cafe.valor_inventario()) 
print(te.valor_inventario())  
print(cafe.vender(3))         
print(cafe.valor_inventario()) 

# Otro ejemplo 
torta = Producto("torta", 25, 4)
print(torta.vender(2))         
print(torta.stock)             
print(te.stock)                
print(torta.valor_inventario()) 