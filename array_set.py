list_user1 = ["gabinete", "monitor", "ram", "teclado", "joystick", "mouse"]
list_user2 = ["play", "joystick", "monitor", "teclado", "auriculares"]
list_produc_comun = [] # Se crea una lista vacia para los productos en comun
list_produc_no_comun = [] # Se crea una lista vacia para los productos no en comun
list_productos_total = [] # Se crea una lista vacia para los productos totales
list_recomendados = [] # Se crea una lista vacia para los productos recomendados para el usuario 1
list_recomendados_2 = [] # Se crea una lista vacia para los productos recomendados para el usuario 2

# Se crea una lista con los productos que tienen en comun
list_produc_comun = set(list_user1) & set(list_user2)

# Se crea una lista con los productos que no tienen en comun
list_produc_no_comun = set(list_user1) ^ set(list_user2)

# Se crea una lista con todos los productos
list_productos_total = set(list_user1) | set(list_user2)

# Se crea una lista con los productos recomendados para el usuario 1
list_recomendados = set(list_user1) - set(list_user2)

# Se crea una lista con los productos recomendados para el usuario 2
list_recomendados_2 = set(list_user2) - set(list_user1)

print("Los productos que tienen en comun son: ", list_produc_comun)
print("Los productos que no tienen en comun son: ", list_produc_no_comun)
print("Los productos totales son: ", list_productos_total)
print("Los productos recomendados para el usuario 1 son: ", list_recomendados)
print("Los productos recomendados para el usuario 2 son: ", list_recomendados_2)