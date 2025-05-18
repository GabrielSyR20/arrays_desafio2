from verificar_variables import es_alfabetico

list_user1 = input("Ingrese los productos del usuario 1 separados por comas: ").split(",")
list_user2 = input("Ingrese los productos del usuario 2 separados por comas: ").split(",") 
list_produc_comun = [] # Se crea una lista vacia para los productos en comun
list_produc_no_comun = [] # Se crea una lista vacia para los productos no en comun
list_productos_total = [] # Se crea una lista vacia para los productos totales
list_recomendados = [] # Se crea una lista vacia para los productos recomendados para el usuario 1
list_recomendados_2 = [] # Se crea una lista vacia para los productos recomendados para el usuario 2

list_user1 = [x.strip() for x in list_user1] # Se eliminan los espacios en blanco de la lista
list_user2 = [x.strip() for x in list_user2] # Se eliminan los espacios en blanco de la lista
list_user1 = [x.lower() for x in list_user1] # Se convierten los elementos de la lista a minusculas
list_user2 = [x.lower() for x in list_user2] # Se convierten los elementos de la lista a minusculas

if all(es_alfabetico(list_user1[k]) for k in range(len(list_user1))):
    
    if all(es_alfabetico(list_user2[l]) for l in range(len(list_user2))):
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

else:
    print("ingresa valores alfanumericos correctamente")

print(f"Los productos del usuario 1 son: {list_user1}")
print(f"Los productos del usuario 2 son: {list_user2}") 
print("Los productos que tienen en comun son:", list_produc_comun)
print("Los productos que no tienen en comun son:", list_produc_no_comun)
print("Los productos totales son:", list_productos_total)
print("Los productos recomendados para el usuario 1 son:", list_recomendados)
print("Los productos recomendados para el usuario 2 son:", list_recomendados_2)