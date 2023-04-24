# Progarma que encuentra la cantidad 
# de veces en las cuales ser repite una palabra


# Variables

Palabra = input("Ingres su texto: ") # Se ingresa el texto
Palabra = Palabra.lower().replace(",", "").replace(".","") 
# Se convierte el texto a minusculas para evitar errores
# Se eliminan los caracteres especiales
Palabra = Palabra.split() # Se convierte el texto en un arreglo

# Busacador

Buscado = input("Ingrese la palabra a buscar: ") # Se ingresa la palabra a buscar
Buscado = Buscado.lower() # Se convierte la palabra a minusculas para evitar errores

# Cantidad de repiticiones

Repeticiones = 0 # Se inicializa la variable en 0

# Proceso

for i in Palabra: # Se itera en el arreglo
    if i == Buscado: # Si el valor es igual al buscado se suma 1 a la variable
        Repeticiones += 1
print("La palabra se repite: ", Repeticiones, " veces")
