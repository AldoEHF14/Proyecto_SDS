# UEA: Seminario De Seguridad

## 🔐 Proyecto de Cifrado Vigenère 

Este proyecto implementa un sistema de cifrado y descifrado basado en dos capas de seguridad:

1. **Cifrado Vigenère personalizado**, utilizando un alfabeto extendido con caracteres latinos, números y espacios.
2. **Cifrado XOR bit a bit**, aplicando una clave aleatoria generada dinámicamente.

---

### 🛠️ Funcionalidades principales

- **Cifrado Vigenère** con una clave repetida para igualar la longitud del texto de entrada.
- **Cifrado XOR** utilizando una clave aleatoria y operaciones a nivel de bits.
- **Gestión automática de claves**: las claves se almacenan y leen desde archivos `key.txt` y `key2.txt`.
- **Interfaz por consola** para seleccionar entre cifrar, descifrar o salir del programa.
- **Limpieza automática** de archivos temporales tras finalizar.

---

### 📌 Uso del programa

Al ejecutar el script, el menú ofrece tres opciones:

1. **Cifrar Mensaje**  
   - Solicita un texto de entrada y una clave.
   - Realiza el cifrado Vigenère.
   - Aplica un cifrado XOR sobre el resultado.
   - Guarda claves y resultados en archivos (`key.txt`, `key2.txt`, `cifradoxor.txt`).

2. **Descifrar Mensaje**  
   - Solicita los nombres de los archivos con el texto cifrado y la clave.
   - Aplica XOR inverso.
   - Descifra con el algoritmo Vigenère original.
   - Muestra el mensaje original.

3. **Salir del Programa**  
   - Elimina automáticamente todos los archivos temporales generados.

---

### ⚠️ Consideraciones

- El texto de entrada solo puede contener caracteres presentes en el alfabeto definido.
- El cifrado XOR es reversible siempre que se mantenga la clave generada aleatoriamente.
- Es importante no perder los archivos `key.txt` y `key2.txt` si deseas recuperar el mensaje original.

---
### ▶️ Ejecución

```bash
python3 Proyecto.py
