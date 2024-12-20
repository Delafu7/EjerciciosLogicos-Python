"""/*
 * Crea un programa que detecte cuando el famoso "Código Konami" se ha
 * introducido correctamente desde el teclado.
 * Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
 */"""
import keyboard

def codigo_konami():
    # Secuencia del código Konami
    codigo = ["up", "up", "down", "down", "left", "right", "left", "right", "b", "a"]
    indice = 0  # Para rastrear el progreso del usuario

    print("Introduce el código Konami (Usa las flechas, 'b' y 'a').")
    try:
        while True:
            # Leer una tecla presionada
            tecla = keyboard.read_event(suppress=True)  # suppress=True para evitar que las teclas lleguen al sistema
            
            # Verificar si es un evento de tecla presionada
            if tecla.event_type == "down":
                # Comprobar si la tecla es la correcta en la secuencia
                if tecla.name == codigo[indice]:
                    print(f"Tecla correcta: {tecla.name}")
                    indice += 1  # Avanzar en la secuencia

                    # Si se completa el código
                    if indice == len(codigo):
                        print("¡Felicidades! Has introducido el código Konami correctamente.")
                        break
                else:
                    # Si la tecla es incorrecta, reiniciar la secuencia
                    print(f"Tecla incorrecta: {tecla.name}. Reiniciando...")
                    indice = 0
    except KeyboardInterrupt:
        print("\nPrograma detenido manualmente. ¡Hasta luego!")

# Ejecutar la función
codigo_konami()
