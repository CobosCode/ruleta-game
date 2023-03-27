import random
import tkinter as tk

# Crear la lista de números de la ruleta y asignar el número de inicio y fin
ruleta = [0] + [i for i in range(1, 37)]
inicio = 0
fin = 36

# Función para girar la ruleta y elegir un número al azar
def girar_ruleta():
    return random.choice(ruleta)

# Función para verificar si el jugador ganó o perdió
def verificar_ganador(numero_elegido, numero_ganador, label_resultado):
    if numero_elegido == numero_ganador:
        label_resultado.config(text="¡Felicitaciones, ganaste!")
    else:
        label_resultado.config(text="Lo siento, perdiste.")

# Función para manejar el evento de hacer clic en el botón "Girar"
def on_girar_click(numero_elegido, label_resultado):
    # Girar la ruleta y mostrar el número ganador
    numero_ganador = girar_ruleta()
    label_ruleta.config(text=f"La ruleta se detiene en el número {numero_ganador}.")

    # Verificar si el jugador ganó o perdió
    verificar_ganador(numero_elegido.get(), numero_ganador, label_resultado)

# Función para manejar el evento de hacer clic en el botón "Jugar de nuevo"
def on_jugar_de_nuevo_click(numero_elegido, label_resultado):
    # Limpiar la entrada de número elegido y el resultado anterior
    numero_elegido.delete(0, tk.END)
    label_resultado.config(text="")

    # Reiniciar el juego
    label_ruleta.config(text="Gira la ruleta y elige un número entre 0 y 36.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de la ruleta")

# Crear los widgets de la interfaz gráfica
label_bienvenida = tk.Label(ventana, text="¡Bienvenido a la ruleta!")
label_instrucciones = tk.Label(ventana, text="Elige un número entre 0 y 36.")
label_numero_elegido = tk.Label(ventana, text="Número elegido:")
numero_elegido = tk.Entry(ventana)
label_ruleta = tk.Label(ventana, text="Gira la ruleta y elige un número entre 0 y 36.")
boton_girar = tk.Button(ventana, text="Girar", command=lambda:on_girar_click(numero_elegido, label_resultado))
label_resultado = tk.Label(ventana, text="")
boton_jugar_de_nuevo = tk.Button(ventana, text="Jugar de nuevo", command=lambda:on_jugar_de_nuevo_click(numero_elegido, label_resultado))

# Colocar los widgets en la ventana
label_bienvenida.pack()
label_instrucciones.pack()
label_numero_elegido.pack()
numero_elegido.pack()
label_ruleta.pack()
boton_girar.pack()
label_resultado.pack()
boton_jugar_de_nuevo.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()