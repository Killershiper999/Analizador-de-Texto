texto = input("Por favor ingresa el texto en minusculas: ")
letras = []
texto = texto.lower()

letras.append(input("Escribe la primera letra ").lower())
letras.append(input("Escribe la segunda letra ").lower())
letras.append(input("Escribe la tercera letra ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras = texto.count(letras[0])
cantidad_letras = texto.count(letras[1])
cantidad_letras = texto.count(letras[2])

print(f"Hemos encontrado las letras '{letras[0]}' repetida {cantidad_letras} veces")
print(f"Hemos encontrado las letras '{letras[1]}' repetida {cantidad_letras} veces")
print(f"Hemos encontrado las letras '{letras[2]}' repetida {cantidad_letras} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letras_inicio = texto[0]
letras_final = texto[-1]
print(f"la letra de inicio es '{letras_inicio}' y la letra final es '{letras_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves va a decir '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'python'{dic[buscar_python]} se encuentra en el texto")


























