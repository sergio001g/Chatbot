import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

class ChistesProgBot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ChistesProgBot")
        self.root.geometry("400x600")
        self.root.configure(bg="#128C7E")
        
        self.setup_gui()
        self.load_chistes()
        
    def setup_gui(self):
        header = tk.Frame(self.root, bg="#075E54", pady=10)
        header.pack(fill=tk.X)
        
        tk.Label(header, text="ChistesProgBot", font=("Arial", 16, "bold"), bg="#075E54", fg="white").pack()
        
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, bg="#ECE5DD", font=("Arial", 11))
        self.chat_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.chat_area.config(state=tk.DISABLED)
        
        input_frame = tk.Frame(self.root, bg="#128C7E")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.input_field = tk.Entry(input_frame, font=("Arial", 12))
        self.input_field.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        self.input_field.bind("<Return>", self.send_message)
        
        send_button = tk.Button(input_frame, text="Enviar", command=self.send_message, bg="#075E54", fg="white")
        send_button.pack(side=tk.RIGHT)
        
        self.display_message("¡Hola! Soy ChistesProgBot. Escribe cualquier cosa para un chiste de programación. 😄🖥️", "bot")
        
    def load_chistes(self):
        self.chistes = [
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
        
    def display_message(self, message, sender):
        self.chat_area.config(state=tk.NORMAL)
        timestamp = datetime.datetime.now().strftime("%H:%M")
        
        if sender == "user":
            self.chat_area.insert(tk.END, f"\n{timestamp} Tú: ", "user")
            self.chat_area.insert(tk.END, f"{message}\n", "user_message")
        else:
            self.chat_area.insert(tk.END, f"\n{timestamp} ChistesProgBot: ", "bot")
            self.chat_area.insert(tk.END, f"{message}\n", "bot_message")
        
        self.chat_area.tag_config("user", foreground="#075E54", font=("Arial", 10, "bold"))
        self.chat_area.tag_config("user_message", foreground="black", font=("Arial", 11))
        self.chat_area.tag_config("bot", foreground="#075E54", font=("Arial", 10, "bold"))
        self.chat_area.tag_config("bot_message", foreground="black", font=("Arial", 11))
        
        self.chat_area.see(tk.END)
        self.chat_area.config(state=tk.DISABLED)
        
    def send_message(self, event=None):
        message = self.input_field.get().strip()
        if message:
            self.display_message(message, "user")
            self.input_field.delete(0, tk.END)
            self.tell_joke()
        
    def tell_joke(self):
        joke = random.choice(self.chistes)
        self.display_message(joke, "bot")
        self.display_message("¿Otro chiste? ¡Escribe lo que sea! 😄", "bot")
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    bot = ChistesProgBot()
    bot.run()
