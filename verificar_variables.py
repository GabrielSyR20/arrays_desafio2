
def es_entero(valor_int):
    if type(valor_int) == int:
        return True
    
    if valor_int[0] in ["+", "-"]:
        valor_int = valor_int[1:]
        
    if type(valor_int) == str and valor_int.isdigit():
        return True
    
    return False
# Comprobamos si el valor es un entero

def es_flotante(valor_float):
    if type(valor_float) == float:
        return True
    
    if valor_float[0] in ["+", "-"]:
        valor_float = valor_float[1:]

    if type(valor_float) == str and "." in valor_float: # Comprobamos si hay un punto
        parts = valor_float.split(".") # Separamos la cadena en dos partes
        return parts[0].isdigit() and parts[1].isdigit() # Comprobamos si ambas partes son dígitos
    
    return False

def es_alfanumerico(valor_alfa):
    '''if type(valor_alfa) == str and valor_alfa.isalnum():
            return True'''
    
    # Comprobamos si el valor es alfanumérico
    if all(c.isalnum() or c.isspace() for c in valor_alfa): # Comprobamos si todos los caracteres son alfanumericos o espacios
            return True
    return False

def es_alfabetico(valor_alfa): 
    '''if type(valor_alfa) == str:
        return True'''
    
    # Comprobamos si el valor es alfabético
    if all(c.isalpha() or c.isspace() for c in valor_alfa): # Comprobamos si todos los caracteres son alfabéticos o espacios
        return True
    return False

