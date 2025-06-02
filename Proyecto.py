import random,os


alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚáéíóúÜü0123456789 "

def cifrado__vigenere(texto_plano, key_repeated):
    resultado = ""

    with open('key.txt', 'w+', encoding='utf-8') as archivo:
        archivo.write(key_repeated)

    for i in range(len(texto_plano)):
        if texto_plano[i] in alfabeto:
            #if modo == "C":
            resultado += alfabeto[(alfabeto.index(texto_plano[i]) + alfabeto.index(key_repeated[i])) % 77]
        else:
            resultado += texto_plano[i]

    return resultado

def descifrado_vigenere(texto_cifrado):
    texto_descifrado = ""

    with open('key.txt', 'r', encoding='utf-8') as archivo:
        key_repeated = archivo.read()

    for i in range(len(texto_cifrado)):
        if texto_cifrado[i] in alfabeto:
            indice_letra_cifrada = alfabeto.index(texto_cifrado[i])
            indice_letra_clave = alfabeto.index(key_repeated[i])
            indice_letra_descifrada = (indice_letra_cifrada - indice_letra_clave) % len(alfabeto)
            texto_descifrado += alfabeto[indice_letra_descifrada]
        else:
            texto_descifrado += texto_cifrado[i]
    return texto_descifrado

def generar_clave_aleatoria_caracteres(tamaño):
    clave_aleatoria = ''.join(chr(random.randint(0, 255)) for _ in range(tamaño))
    return clave_aleatoria

def Vigenere_XOR(mensaje_cifrado):

    tamanio = len(mensaje_cifrado)
    clave_aleatoria = generar_clave_aleatoria_caracteres(tamanio)
    #print(clave_aleatoria)

    with open('key2.txt', 'w+', encoding='utf-8') as archivo:
        archivo.write(clave_aleatoria)

    mensaje_cifrado_bits = ''.join(format(ord(char), '08b') for char in mensaje_cifrado)
    #print(mensaje_cifrado_bits)

    clave_aleatoria_bits = ''.join(format(ord(char), '08b') for char in clave_aleatoria)
    #print(clave_aleatoria_bits)

    resultado_xor = ''.join(str(int(bit_clave) ^ int(bit_texto)) for bit_clave, bit_texto in zip(mensaje_cifrado_bits, clave_aleatoria_bits))
    #print(resultado_xor)

    resultado_caracteres = ''.join(chr(int(resultado_xor[i:i+8], 2)) for i in range(0, len(resultado_xor), 8))
   
    with open('cifradoxor.txt', 'w+', encoding='utf-8') as archivo:
        archivo.write(resultado_caracteres)

    return resultado_caracteres

def XOR_Vigenere (descifrado,key):

    with open(key, 'r', encoding='utf-8') as archivo:
        # Lee todo el contenido del archivo    
        contenido = archivo.read()
        
    mensaje_cifrado_bits = ''.join(format(ord(char), '08b') for char in contenido)
    #print(mensaje_cifrado_bits)

    with open(descifrado, 'r', encoding='utf-8') as archivo:
        # Lee todo el contenido del archivo    
        contenido_xor = archivo.read()
    
    clave_xor_bits = ''.join(format(ord(char), '08b') for char in contenido_xor)
    #print(clave_xor_bits)

    resultado_xor = ''.join(str(int(bit_clave) ^ int(bit_texto)) for bit_clave, bit_texto in zip(mensaje_cifrado_bits, clave_xor_bits))
    #print(resultado_xor)

    resultado_caracteres = ''.join(chr(int(resultado_xor[i:i+8], 2)) for i in range(0, len(resultado_xor), 8))
    # print(resultado_caracteres)

    return resultado_caracteres

def key_long(plaintext,key):
    repeticiones = len(plaintext) // len(key)
    resto = len(plaintext) % len(key)
    key_repeated = key * repeticiones + key[:resto]
    #print(plaintext,",",key_repeated)

    return key_repeated

def main():

    while  True:
		
        print ("|------------------------------|")
        print ("|  1. Cifrar  Mensaje          |")
        print ("|  2. Descifrar Mensaje        |")
        print ("|  3. Salir  del Programa      |")
        print ("|------------------------------|")
        opt = int(input("Ingrese una opcion: "))
        if (opt == 1):

            texto_plano = input("Ingrese el texto de entrada (plaintext): ")

            if not all(c in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyzÁÉÍÓÚáéíóúÜü0123456789 " for c in texto_plano):
                print("Error: El texto contiene caracteres no válidos.")
            
            clave_vigenere = input("Ingrese la cadena de caracteres de la llave (key): ")
            #La key debe de tener el mismo tamaño del texto de entrada 
            key_repeated = key_long(texto_plano, clave_vigenere)

            mensaje_cifrado = cifrado__vigenere(texto_plano, key_repeated)
            #print("Mensaje cifrado (ciphertext): ",mensaje_cifrado)

            mensaje_cifrado_xor = Vigenere_XOR(mensaje_cifrado)
            print("Mensaje cifrado xor: ",mensaje_cifrado_xor)            

        if (opt == 2):

            descifrado = input('Ingresa el nombre del archivo.txt (Texto a Descifrar): ')
            key = input ('Ingresa el nombre del archivo.txt (Key): ')
            plantex= XOR_Vigenere(descifrado,key)
            mensaje_descifrado = descifrado_vigenere(plantex)#, key_repeated)
            print("Descifrado vigenere:",mensaje_descifrado)

        if (opt == 3):

            # Lista de nombres de archivos a eliminar
            archivos_a_eliminar = ['key.txt', 'key2.txt', 'cifradoxor.txt']
            # Iterar sobre la lista de nombres de archivos y eliminar cada archivo
            for archivo in archivos_a_eliminar:
                if os.path.exists(archivo):
                    os.remove(archivo)
                    print(f"El archivo '{archivo}' ha sido eliminado.")
                else:
                    print(f"El archivo '{archivo}' no existe.")

            break

if __name__ == '__main__':
    main()