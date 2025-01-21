import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("ChistesProgBot")
    ventana.geometry("400x600")
    ventana.configure(bg="#128C7E")
    return ventana

def configurar_interfaz(ventana):
    cabecera = tk.Frame(ventana, bg="#075E54", pady=10)
    cabecera.pack(fill=tk.X)
    
    tk.Label(cabecera, text="ChistesProgBot", font=("Arial", 16, "bold"), bg="#075E54", fg="white").pack()
    
    area_chat = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, bg="#ECE5DD", font=("Arial", 11))
    area_chat.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    area_chat.config(state=tk.DISABLED)
    
    marco_entrada = tk.Frame(ventana, bg="#128C7E")
    marco_entrada.pack(fill=tk.X, padx=10, pady=10)
    
    campo_entrada = tk.Entry(marco_entrada, font=("Arial", 12))
    campo_entrada.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
    
    boton_enviar = tk.Button(marco_entrada, text="Enviar", command=lambda: procesar_mensaje(campo_entrada, area_chat), bg="#075E54", fg="white")
    boton_enviar.pack(side=tk.RIGHT)
    
    campo_entrada.bind("<Return>", lambda event: procesar_mensaje(campo_entrada, area_chat))
    
    return area_chat, campo_entrada

def cargar_chistes():
    return [
        "¿Por qué los programadores prefieren iOS? Porque no les gusta dating.",
        "¿Qué le dice un bit a otro bit? Nos vemos en el bus.",
        "¿Por qué los programadores odian la naturaleza? Tiene demasiados bugs.",
        "¿Cómo llaman los programadores a sus amigos? ¡Callback!",
        "¿Por qué los programadores son malos en las relaciones? Porque confunden '==' con '='.",
        "¿Qué le dice un programador a otro en un funeral? Descansa en código.",
        "¿Por qué los programadores prefieren el frío? Porque les gusta estar a 0 grados Kelvin.",
        "¿Cómo se llama un programador zombi? ¡Un código muerto viviente!",
        "¿Por qué los programadores siempre confunden Halloween con Navidad? Porque Oct 31 == Dec 25.",
        "¿Cuál es el objeto más usado por un programador? Café.objeto",
        "¿Qué hace un programador cuando se aburre? Abre las ventanas.",
        "¿Cómo se despiden los binarios? Adiós... 01000001 01100100 01101001 11000011 10110011 01110011",
        "¿Qué le dice un .GIF a un .JPEG? ¡Anímate, hombre!",
        "¿Qué es un terapeuta? 1024 gigapeutas.",
        "¿Por qué el programador renunció a su trabajo? Porque no obtuvo arrays.",
        "¿Cómo llaman los programadores a sus reuniones? Standup comedy.",
        "¿Qué hace un programador en el jardín? Git pull para sacar las malas hierbas.",
        "¿Por qué los programadores son tan malos en las peleas? Porque solo saben hacer scripts.",
        "¿Qué le dice un programador a otro? Te veo en el código.",
        "¿Por qué los programadores prefieren trabajar de noche? Porque es cuando los bugs duermen.",
        "¿Cómo se llama un programador en la playa? Sandy.",
        "¿Qué hace un programador en un barco? Navega por el C.",
        "¿Por qué los programadores son tan buenos en el ajedrez? Porque piensan varios movimientos adelante.",
        "¿Qué le dice un programador a su hijo rebelde? ¡Estás castigado, y sin herencia!",
        "¿Cómo se llama un programador que no usa Stack Overflow? Desempleado.",
        "¿Qué hace un programador en un funeral? Dar el último commit.",
        "¿Cómo se llama un programador sin cafeína? Decaffeinated.",
        "¿Por qué los programadores son malos cocineros? Porque sus recetas siempre tienen bugs.",
        "¿Por qué los programadores son tan buenos en las matemáticas? Porque usan su lógica.",
        "¿Cómo se llama un programador que no sabe programar? Usuario.",
        "¿Qué hace un programador en el gimnasio? Ejercicios de recursión.",
        "¿Por qué los programadores son tan malos en las citas? Porque siempre están buscando su match perfecto.",
        "¿Cómo se llama un programador sin trabajo? 404 not found.",
        "¿Qué le dice un programador a su espejo? Hello, world!",
        "¿Por qué los programadores son tan buenos en los juegos de cartas? Porque siempre están barajando.",
        "¿Cómo se llama un programador que solo trabaja con números? Contador de historias.",
        "¿Qué hace un programador cuando ve una araña? Debuggear la casa.",
        "¿Por qué los programadores odian las fiestas? Demasiados errores de sintaxis en la conversación.",
        "¿Qué le dice un programador a su pareja? Eres mi excepción.",
        "¿Por qué los programadores son tan buenos mintiendo? Porque saben manejar excepciones.",
        "¿Cómo coquetea un programador? '¿Quieres ser mi constante?'",
        "¿Por qué los programadores son malos amantes? Confunden el hardware con el software.",
        "¿Qué le dice un programador a su ex? Has sido eliminada de mi caché.",
        "¿Por qué los programadores son buenos en las relaciones? Saben cómo manejar los conflictos.",
        "¿Cómo llama un programador a su crush? Mi variable global.",
        "¿Por qué los programadores son buenos en la cama? Saben cómo maximizar el rendimiento.",
        "¿Qué le dice un programador a su pareja en la boda? Acepto (mientras true).",
        "¿Por qué los programadores son buenos besando? Tienen experiencia en lenguajes de marcado.",
        "¿Cómo termina un programador una relación? return false;",
        "¿Qué le dice un programador inseguro a su pareja? ¿Soy tu único instanceof?",
    ]

def mostrar_mensaje(area_chat, mensaje, remitente):
    area_chat.config(state=tk.NORMAL)
    timestamp = datetime.datetime.now().strftime("%H:%M")
    
    if remitente == "usuario":
        area_chat.insert(tk.END, f"\n{timestamp} Tú: ", "usuario")
        area_chat.insert(tk.END, f"{mensaje}\n", "mensaje_usuario")
    else:
        area_chat.insert(tk.END, f"\n{timestamp} ChistesProgBot: ", "bot")
        area_chat.insert(tk.END, f"{mensaje}\n", "mensaje_bot")
    
    area_chat.tag_config("usuario", foreground="#075E54", font=("Arial", 10, "bold"))
    area_chat.tag_config("mensaje_usuario", foreground="black", font=("Arial", 11))
    area_chat.tag_config("bot", foreground="#075E54", font=("Arial", 10, "bold"))
    area_chat.tag_config("mensaje_bot", foreground="black", font=("Arial", 11))
    
    area_chat.see(tk.END)
    area_chat.config(state=tk.DISABLED)

def procesar_mensaje(campo_entrada, area_chat):
    mensaje = campo_entrada.get().strip()
    if mensaje:
        mostrar_mensaje(area_chat, mensaje, "usuario")
        campo_entrada.delete(0, tk.END)
        contar_chiste(area_chat)

def contar_chiste(area_chat):
    chiste = random.choice(chistes)
    mostrar_mensaje(area_chat, chiste, "bot")
    mostrar_mensaje(area_chat, "¿Otro chiste? ¡Escribe lo que sea! 😄", "bot")

def iniciar_bot():
    ventana = crear_ventana()
    area_chat, campo_entrada = configurar_interfaz(ventana)
    mostrar_mensaje(area_chat, "¡Hola! Soy ChistesProgBot. Escribe cualquier cosa para un chiste de programación. 😄🖥️", "bot")
    ventana.mainloop()

chistes = cargar_chistes()
iniciar_bot()
