import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk 
import os
import time
import json

matriz_user_in_code =[[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

matriz_pass_in_code = [[" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "]]

respuestas_hogar_in_code = [[] for _ in range(10)]
respuestas_numero_in_code = [[] for _ in range(10)]

ultimo_indice = -1
username_entry = None
password_entry = None
numero_entry = None
hogar_entry = None
canvas = None
carpeta_datos = "DATOS"

# Función para cargar datos desde archivos JSON
def cargar_datos():
    global matriz_user, matriz_pass, respuestas_numero, respuestas_hogar, ultimo_indice

    try:
        with open(os.path.join(carpeta_datos, "matriz_user.json"), "r") as f:
            matriz_user = json.load(f)
    except FileNotFoundError:
        matriz_user = [[" "] * 10 for _ in range(10)]

    try:
        with open(os.path.join(carpeta_datos, "matriz_pass.json"), "r") as f:
            matriz_pass = json.load(f)
    except FileNotFoundError:
        matriz_pass = [[" "] * 8 for _ in range(10)]

    try:
        with open(os.path.join(carpeta_datos, "respuestas_numero.json"), "r") as f:
            respuestas_numero = json.load(f)
    except FileNotFoundError:
        respuestas_numero = [[] for _ in range(10)]

    try:
        with open(os.path.join(carpeta_datos, "respuestas_hogar.json"), "r") as f:
            respuestas_hogar = json.load(f)
    except FileNotFoundError:
        respuestas_hogar = [[] for _ in range(10)]

    ultimo_indice = -1
    for i, row in enumerate(matriz_user):
        if "".join(row).strip() != "":
            ultimo_indice = i

    guardar_datos()

# Función para guardar datos en archivos JSON
def guardar_datos():
    os.makedirs(carpeta_datos, exist_ok=True)  # Crea la carpeta si no existe

    with open(os.path.join(carpeta_datos, "matriz_user.json"), "w") as f:
        json.dump(matriz_user, f)

    with open(os.path.join(carpeta_datos, "matriz_pass.json"), "w") as f:
        json.dump(matriz_pass, f)

    with open(os.path.join(carpeta_datos, "respuestas_numero.json"), "w") as f:
        json.dump(respuestas_numero, f)

    with open(os.path.join(carpeta_datos, "respuestas_hogar.json"), "w") as f:
        json.dump(respuestas_hogar, f)

################################################################## cargar_datos_desde_json ####################################################################################################
def cargar_datos_desde_json():
    global matriz_user_in_code, matriz_pass_in_code, respuestas_numero_in_code, respuestas_hogar_in_code
    try:
        with open(os.path.join(carpeta_datos, "matriz_user.json"), "r") as f:
            matriz_user_in_code = json.load(f)
    except FileNotFoundError:
        matriz_user_in_code = [[" "] * 10 for _ in range(10)]

    try:
        with open(os.path.join(carpeta_datos, "matriz_pass.json"), "r") as f:
            matriz_pass_in_code = json.load(f)
    except FileNotFoundError:
        matriz_pass_in_code = [[" "] * 8 for _ in range(10)]

    try:
        with open(os.path.join(carpeta_datos, "respuestas_numero.json"), "r") as f:
            respuestas_numero_in_code = json.load(f)
    except FileNotFoundError:
        respuestas_numero_in_code = [[] for _ in range(10)]

    try:
        with open(os.path.join(carpeta_datos, "respuestas_hogar.json"), "r") as f:
            respuestas_hogar_in_code = json.load(f)
    except FileNotFoundError:
        respuestas_hogar_in_code = [[] for _ in range(10)]

    # Luego, actualiza la ventana de datos para reflejar los nuevos datos
    ventana_datos()

def fondo():
    try:
        image = Image.open("CRUD GE0SH.png")
        photo = ImageTk.PhotoImage(image)

        # Establecer la imagen de fondo en una etiqueta
        background_label = tk.Label(ventana, image=photo)
        background_label.place(relwidth=1, relheight=1)

        # Asegúrate de mantener una referencia global a la imagen para evitar que sea eliminada por el recolector de basura
        background_label.image = photo
    except FileNotFoundError:
        # Si el archivo de imagen no se encuentra, usa un color de fondo
        ventana.configure(bg="#FFFFF3")

def registrar():
    global ultimo_indice
    usuario = username_entry.get()  # Obtener el texto del campo de usuario
    contraseña = password_entry.get()  # Obtener el texto del campo de contraseña
    respuesta_numero = numero_entry.get()  # Obtener el texto del campo de número
    respuesta_hogar = hogar_entry.get()  # Obtener el texto del campo de hogar

    if ultimo_indice == 9:
        messagebox.showerror("Límite de Usuarios", "La matriz está llena. No se pueden registrar más usuarios.")
        return
    
    if not usuario or not contraseña or not respuesta_numero or not respuesta_hogar:
        messagebox.showerror("Campos Vacíos", "Ingrese datos en todos los campos.")
        return

    if usuario in ["".join(matriz_user_in_code[i]).strip() for i in range(ultimo_indice + 1)]:
        messagebox.showerror("Usuario Existente", "El usuario ya existe. Intente con un nombre de usuario diferente.")
        return

    if len(usuario) > 10:
        messagebox.showerror("Usuario Demasiado Largo", "El usuario no debe exceder los 10 caracteres.")
        return

    if len(contraseña) != 8 or not any(c.isupper() for c in contraseña) or not any(c in "!@#$%^&*()-_+=[]{}|;:'<>,.?/" for c in contraseña) or not any(c.isdigit() for c in contraseña):
        messagebox.showerror("Contraseña Incorrecta", "La contraseña debe tener 8 caracteres exactos, incluyendo al menos 1 mayúscula, 1 símbolo y 1 número")
        return

    ultimo_indice += 1

    for j, caracter in enumerate(usuario):
        matriz_user_in_code[ultimo_indice][j] = caracter
        matriz_user [ultimo_indice][j] = caracter

    for j, caracter in enumerate(contraseña):
        matriz_pass_in_code[ultimo_indice][j] = caracter
        matriz_pass[ultimo_indice][j] = caracter

    if not respuesta_numero.isdigit():
        messagebox.showerror("Respuesta Incorrecta", "La respuesta debe ser un número")
        ultimo_indice -= 1
        return
    if not respuesta_hogar.isalpha():
        messagebox.showerror("Respuesta Incorrecta", "La respuesta debe ser una palabra")
        ultimo_indice -= 1
        return

    respuestas_hogar_in_code[ultimo_indice].append(respuesta_hogar)
    respuestas_numero_in_code[ultimo_indice].append(respuesta_numero)
    respuestas_numero[ultimo_indice].append(respuesta_numero)
    respuestas_hogar[ultimo_indice].append(respuesta_hogar)
    guardar_datos()

    messagebox.showinfo("Registro Exitoso", "Usuario registrado exitosamente")
    menu_principal()

# Función para iniciar sesión
def login():
    global username_entry, password_entry
    usuario = username_entry.get()
    contraseña = password_entry.get()

    for i in range(ultimo_indice + 1):
        usuario_actual = "".join(matriz_user[i]).strip()
        contraseña_actual = "".join(matriz_pass[i]).strip()

        if usuario_actual == usuario and contraseña_actual == contraseña:
            messagebox.showinfo(":)","Inicio de sesión exitoso")
            ventana_submenu()
            return

    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def eliminar_usuario():
    global username_entry, numero_entry, hogar_entry
    global matriz_user, matriz_pass, respuestas_numero, respuestas_hogar, ultimo_indice
    global matriz_user_in_code, matriz_pass_in_code, respuestas_numero_in_code, respuestas_hogar_in_code

    usuario = username_entry.get()
    numero = numero_entry.get()
    hogar = hogar_entry.get()

    usuario_encontrado = False
    for i in range(ultimo_indice + 1):
        if "".join(matriz_user[i]).strip() == usuario:
            usuario_encontrado = True
            if numero in respuestas_numero[i] and hogar in respuestas_hogar[i]:
                matriz_user[i] = [" "] * 10
                matriz_pass[i] = [" "] * 8
                respuestas_numero[i] = []
                respuestas_hogar[i] = []

                matriz_user_in_code[i] = [" "] * 10
                matriz_pass_in_code[i] = [" "] * 8
                respuestas_numero_in_code[i] = []
                respuestas_hogar_in_code[i] = []

                i = 0
                while i < ultimo_indice:
                    if "".join(matriz_user[i]).strip() == "":
                        for j in range(i, ultimo_indice):
                            matriz_user[j] = matriz_user[j + 1]
                            matriz_pass[j] = matriz_pass[j + 1]
                            respuestas_numero[j] = respuestas_numero[j + 1]
                            respuestas_hogar[j] = respuestas_hogar[j + 1]

                            matriz_user_in_code[j] = matriz_user_in_code[j + 1]
                            matriz_pass_in_code[j] = matriz_pass_in_code[j + 1]
                            respuestas_numero_in_code[j] = respuestas_numero_in_code[j + 1]
                            respuestas_hogar_in_code[j] = respuestas_hogar_in_code[j + 1]

                        matriz_user[ultimo_indice] = [" "] * 10
                        matriz_pass[ultimo_indice] = [" "] * 8
                        respuestas_numero[ultimo_indice] = []
                        respuestas_hogar[ultimo_indice] = []

                        matriz_user_in_code[ultimo_indice] = [" "] * 10
                        matriz_pass_in_code[ultimo_indice] = [" "] * 8
                        respuestas_numero_in_code[ultimo_indice] = []
                        respuestas_hogar_in_code[ultimo_indice] = []

                        ultimo_indice -= 1

                    i += 1

                guardar_datos()  # Actualiza los archivos JSON después de la compactación
                ventana_datos()  # Actualiza la interfaz gráfica
                messagebox.showinfo("Usuario Eliminado", "Contenido del usuario eliminado exitosamente")
            else:
                messagebox.showerror("Error", "Respuestas incorrectas")
            break

    if not usuario_encontrado:
        messagebox.showerror("Error", "Usuario no encontrado.")


def actualizar_usuario():
    global username_entry, update_password_entry, update_numero_entry, update_hogar_entry
    usuario = username_entry.get()
    nueva_contraseña = update_password_entry.get()
    nuevo_numero = update_numero_entry.get()
    nuevo_hogar = update_hogar_entry.get()

    if not usuario or (not nueva_contraseña and not nuevo_numero and not nuevo_hogar):
        messagebox.showerror("Campos Vacíos", "Por favor, complete al menos un campo para actualizar.")
        return
    usuario_encontrado = False
# Buscar el usuario en la matriz de usuarios
    for i in range(ultimo_indice + 1):
        if "".join(matriz_user[i]).strip() == usuario:
            usuario_encontrado = True

            if nueva_contraseña:
                # Verificar la nueva contraseña
                if len(nueva_contraseña) != 8 or not any(c.isupper() for c in nueva_contraseña) or not any(
                        c in "!@#$%^&*()-_+=[]{}|;:'<>,.?/" for c in nueva_contraseña) or not any(c.isdigit() for c in nueva_contraseña):
                    messagebox.showerror("Contraseña Incorrecta", "La contraseña debe tener 8 caracteres exactos, incluyendo al menos 1 mayúscula, 1 símbolo y 1 número")
                    return
                matriz_pass[i] = list(nueva_contraseña)
                matriz_pass_in_code[i] = list(nueva_contraseña)

            if nuevo_numero:
                if not nuevo_numero.isdigit():
                    messagebox.showerror("Número Incorrecto", "El número debe ser un número válido.")
                    return
                respuestas_numero[i] = [nuevo_numero]
                respuestas_numero_in_code[i] = [nuevo_numero]

            if nuevo_hogar:
                if not nuevo_hogar.isalpha():
                    messagebox.showerror("Lugar de Nacimiento Incorrecto", "El lugar de nacimiento debe contener solo letras.")
                    return
                respuestas_hogar[i] = [nuevo_hogar]
                respuestas_hogar_in_code[i] = [nuevo_hogar]

            guardar_datos()
            ventana_datos()
            messagebox.showinfo("Actualización Exitosa", "La información del usuario ha sido actualizada exitosamente.")
            return

    if not usuario_encontrado:
        messagebox.showerror("Error", "Usuario no encontrado.")



def ventana_submenu():
    for widget in ventana.winfo_children():
        widget.destroy()
    fondo()

    ventana.geometry("400x400")
    ventana.resizable(False, False)


    # Botones "Ver datos" y "Ordenamientos" centrados y más grandes
    verdatos_button = tk.Button(ventana, text="Datos", height=3, width=15,command=ventana_datos)
    verdatos_button.pack(pady=20)
    verdatos_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")

    ordenamientos_button = tk.Button(ventana, text="Ordenamientos", height=3, width=15,command=ventana_ordenamientos)
    ordenamientos_button.pack(pady=20)
    ordenamientos_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")
    
    arboles_button = tk.Button(ventana, text="Árboles", height=3, width=15,command=ventana_arboles)
    arboles_button.pack(pady=20)
    arboles_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")

    # Botón "Volver al Menú Principal" en la parte inferior
    volver_button = tk.Button(ventana, text="Volver",height=3,width=15,command=menu_principal)
    volver_button.pack(side="bottom",pady=10)
    volver_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")


def ventana_datos():
    global matriz_user, matriz_pass, respuestas_numero, respuestas_hogar, frame_info
    for widget in ventana.winfo_children():
        widget.destroy()

    ventana.geometry("685x500")

    # Crear un Frame principal que llenará toda la ventana
    frame_principal = tk.Frame(ventana)
    frame_principal.config(bg="#FFFFF3")
    frame_principal.pack(expand=True, fill='both')

    # Separar la ventana en dos partes: parte superior y parte inferior
    frame_superior = tk.Frame(frame_principal)
    frame_superior.pack(side="top", expand=True, fill='both')
    frame_superior.config(bg="#FFFFF3")

    frame_botones = tk.Frame(frame_superior)
    frame_botones.pack(side="left", fill="x", expand=True)
    frame_botones.config(bg="#FFFFF3")

    global frame_info  # Usar la variable global frame_info
    frame_info = tk.Frame(frame_principal)
    frame_info.pack(side="bottom", expand=True, fill='both', pady=10)
    frame_info.config(bg="#FFFFF3")

    # Mostrar la matriz de usuario
    for i in range(ultimo_indice + 1):
        for j in range(10):
            cuadro_texto = tk.Text(frame_info, height=1, width=2)
            cuadro_texto.grid(row=i, column=j)
            cuadro_texto.insert(tk.END, matriz_user_in_code[i][j])
            cuadro_texto.config(state=tk.DISABLED)

    # Mostrar la matriz de contraseña
    for i in range(ultimo_indice + 1):
        for j in range(8):
            cuadro_texto = tk.Text(frame_info, height=1, width=2)
            cuadro_texto.grid(row=i, column=j + 11)  # Separar las matrices
            cuadro_texto.insert(tk.END, matriz_pass_in_code[i][j])
            cuadro_texto.config(state=tk.DISABLED)

    # Mostrar la información de las respuestas
    for i in range(ultimo_indice + 1):
        if i < len(respuestas_numero):
            cuadro_texto = tk.Text(frame_info, height=1, width=20)
            cuadro_texto.grid(row=i, column=21)  # Separar las matrices
            cuadro_texto.insert(tk.END, ", ".join(respuestas_numero_in_code[i]))
            cuadro_texto.config(state=tk.DISABLED)

        if i < len(respuestas_hogar):
            cuadro_texto = tk.Text(frame_info, height=1, width=20)
            cuadro_texto.grid(row=i, column=22)  # Separar las matrices
            cuadro_texto.insert(tk.END, ", ".join(respuestas_hogar_in_code[i]))
            cuadro_texto.config(state=tk.DISABLED)

    # Botones
    botton_eliminar_usuario = tk.Button(frame_botones, text="Eliminar Usuario", height=1, width=15)
    botton_eliminar_usuario.pack(side="left", pady=10, padx=10)
    botton_eliminar_usuario.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white", command=ventana_eliminar)

    botton_actualizar_usuario = tk.Button(frame_botones, text="Actualizar Usuario", height=1, width=15,command=ventana_actualizar)
    botton_actualizar_usuario.pack(side="left", pady=10, padx=10)
    botton_actualizar_usuario.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    botton_cargar_datos = tk.Button(frame_botones, text="Cargar Datos", height=1, width=15,command=cargar_datos_desde_json)
    botton_cargar_datos.pack(side="left", pady=10, padx=10)
    botton_cargar_datos.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    botton_volver = tk.Button(frame_botones, text="Volver", height=1, width=15)
    botton_volver.pack(side="left", pady=10, padx=10)
    botton_volver.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white", command=ventana_submenu)

def ventana_eliminar():
    global username_entry, numero_entry, hogar_entry
    ventana = tk.Toplevel()
    ventana.title("Eliminar Usuario")
    ventana.geometry("400x400")
    ventana.resizable(False, False)
    ventana.config(bg="#FFFFF3")

    username_label = tk.Label(ventana, text="Usuario: ")
    username_label.pack(pady=5)
    username_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white",anchor="center", justify="center")

    username_entry = tk.Entry(ventana)
    username_entry.pack(pady=5)
    username_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    numero_label = tk.Label(ventana, text="Número favorito: ")
    numero_label.pack(pady=5)
    numero_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")

    numero_entry = tk.Entry(ventana)
    numero_entry.pack(pady=5)
    numero_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    hogar_label = tk.Label(ventana, text="Lugar de nacimiento: ")
    hogar_label.pack(pady=5)
    hogar_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")

    hogar_entry = tk.Entry(ventana)
    hogar_entry.pack(pady=5)
    hogar_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    bottom_eliminar = tk.Button(ventana, text="Eliminar", height=1, width=15,command=eliminar_usuario)
    bottom_eliminar.pack(pady=5)
    bottom_eliminar.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")


def ventana_actualizar():
    global username_entry, password_entry, numero_entry, hogar_entry, update_password_entry, update_numero_entry, update_hogar_entry
    ventana = tk.Toplevel()
    ventana.title("Actualizar Usuario")
    ventana.geometry("400x400")
    ventana.resizable(False, False)
    ventana.config(bg="#FFFFF3")

    username_label = tk.Label(ventana, text="Usuario: ")
    username_label.pack(pady=5)
    username_label.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white", anchor="center", justify="center")

    username_entry = tk.Entry(ventana)
    username_entry.pack(pady=5)
    username_entry.config(font=("Arial", 12), borderwidth=2, relief="ridge")

    password_label = tk.Label(ventana, text="Nueva Contraseña: ")
    password_label.pack(pady=5)
    password_label.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    update_password_entry = tk.Entry(ventana, show="*")
    update_password_entry.pack(pady=5)
    update_password_entry.config(font=("Arial", 12), borderwidth=2, relief="ridge")

    numero_label = tk.Label(ventana, text="Nuevo Número favorito: ")
    numero_label.pack(pady=5)
    numero_label.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    update_numero_entry = tk.Entry(ventana)
    update_numero_entry.pack(pady=5)
    update_numero_entry.config(font=("Arial", 12), borderwidth=2, relief="ridge")

    hogar_label = tk.Label(ventana, text="Nuevo Lugar de nacimiento: ")
    hogar_label.pack(pady=5)
    hogar_label.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    update_hogar_entry = tk.Entry(ventana)
    update_hogar_entry.pack(pady=5)
    update_hogar_entry.config(font=("Arial", 12), borderwidth=2, relief="ridge")

    bottom_actualizar = tk.Button(ventana, text="Actualizar", height=1, width=15, command=actualizar_usuario)
    bottom_actualizar.pack(pady=5)
    bottom_actualizar.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

################################################################## ORDENAMIENTOS ####################################################################################################

def ventana_ordenamientos():
    for widget in ventana.winfo_children():
        widget.destroy()

    ventana.geometry("800x500")

    panel = ttk.Notebook(ventana)
    panel.pack(expand=True, fill='both')

################################################################## BURBUJA ####################################################################################################
    tab_burbuja = ttk.Frame(panel)
    panel.add(tab_burbuja, text="Burbuja")

    etiqueta_burbuja = tk.Label(tab_burbuja, text="Ingresa los números a ordenar separados por comas", font=("Arial", 16, "bold"))
    etiqueta_burbuja.pack(pady=10)

    entrada_burbuja = tk.Entry(tab_burbuja)
    entrada_burbuja.pack(pady=20)
    entrada_burbuja.config(font=("Arial", 12), borderwidth=2, relief="ridge", width=50, justify="center")

    resultado_label = ttk.Label(tab_burbuja, text="", font=("Arial", 12))
    resultado_label.pack(pady=10)

    lista_ordenada = ttk.Label(tab_burbuja, text="", font=("Arial", 12))
    lista_ordenada.pack(pady=10)

    lista_original = ttk.Label(tab_burbuja, text="", font=("Arial", 12))
    lista_original.pack(pady=10)

    info_burbuja = ttk.Label(tab_burbuja, text="", font=("Arial", 12))
    info_burbuja.pack(pady=10)

    def ordenar_burbuja():
        # Obtener la entrada del usuario
        entrada = entrada_burbuja.get().strip()
        resultado_label.config(text="")
        
        if not entrada:
            resultado_label.config(text="Por favor, ingresa números separados por comas.")
            return

        try:
            # Dividir la entrada en una lista de números
            numeros = [int(x) for x in entrada.split(',')]
        except ValueError:
            resultado_label.config(text="Error: Ingresa números válidos separados por comas.")
            return
        
        # Verificar si la entrada contiene más de 10 números
        if len(numeros) > 10:
            resultado_label.config(text="Error: No se permiten más de 10 números.")
            return
        
        # Verificar si la entrada contiene menos de 5 números
        if len(numeros) < 5:
            resultado_label.config(text="Error: Se requieren al menos 5 números.")
            return
        
        def burbuja():
            movimientos = 0
            consultas = 0
            for i in range(len(numeros)):
                for j in range(len(numeros) - 1):
                    consultas += 1
                    if numeros[j] > numeros[j + 1]:
                        numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
                        movimientos += 1
            return movimientos, consultas
        
        movimientos, consultas = burbuja()

        # Actualizar las etiquetas existentes
        lista_ordenada.config(text=f"Lista Ordenada: {numeros}")
        lista_original.config(text=f"Lista Original: {entrada}")
        info_burbuja.config(text=f"Iteraciones: {len(numeros)}, Movimientos: {movimientos}, Consultas: {consultas}")

    boton_ordenar = tk.Button(tab_burbuja, text="Ordenar", command=ordenar_burbuja)
    boton_ordenar.pack(pady=10)
    boton_ordenar.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    botton_volver = tk.Button(tab_burbuja, text="Volver", height=1, width=15)
    botton_volver.pack(side="bottom", pady=10)
    botton_volver.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white", command=ventana_submenu)

################################################################## BURBUJA MEJORADA ####################################################################################################
    tab_burbuja_mejorada = ttk.Frame(panel)
    panel.add(tab_burbuja_mejorada, text="Burbuja Mejorada")

    etiqueta_burbuja_mejorada = tk.Label(tab_burbuja_mejorada, text="Ingresa los números a ordenar separados por comas", font=("Arial", 16, "bold"))
    etiqueta_burbuja_mejorada.pack(pady=10)

    entrada_burbuja_mejorada = tk.Entry(tab_burbuja_mejorada)
    entrada_burbuja_mejorada.pack(pady=20)
    entrada_burbuja_mejorada.config(font=("Arial", 12), borderwidth=2, relief="ridge", width=50, justify="center")

    resultado_label_mejorada = ttk.Label(tab_burbuja_mejorada, text="", font=("Arial", 12))
    resultado_label_mejorada.pack(pady=10)

    lista_ordenada_mejorada = ttk.Label(tab_burbuja_mejorada, text="", font=("Arial", 12))
    lista_ordenada_mejorada.pack(pady=10)

    lista_original_mejorada = ttk.Label(tab_burbuja_mejorada, text="", font=("Arial", 12))
    lista_original_mejorada.pack(pady=10)

    info_burbuja_mejorada = ttk.Label(tab_burbuja_mejorada, text="", font=("Arial", 12))
    info_burbuja_mejorada.pack(pady=10)

    def ordenar_burbuja_mejorada():
        entrada = entrada_burbuja_mejorada.get().strip()
        resultado_label_mejorada.config(text="")
        
        if not entrada:
            resultado_label_mejorada.config(text="Por favor, ingresa números separados por comas.")
            return

        try:
            # Dividir la entrada en una lista de números
            numeros = [int(x) for x in entrada.split(',')]
        except ValueError:
            resultado_label_mejorada.config(text="Error: Ingresa números válidos separados por comas.")
            return
        
        # Verificar si la entrada contiene más de 10 números
        if len(numeros) > 10:
            resultado_label_mejorada.config(text="Error: No se permiten más de 10 números.")
            return
        
        # Verificar si la entrada contiene menos de 5 números
        if len(numeros) < 5:
            resultado_label_mejorada.config(text="Error: Se requieren al menos 5 números.")
            return
        
        def burbuja_mejorada(arr):
            n = len(arr)
            iteraciones = 0
            movimientos = 0
            consultas = 0
            for i in range(len(numeros)):
                swapped = False
                for j in range(0, n - i - 1):
                    consultas += 1
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        movimientos += 1
                        swapped = True
                iteraciones += 1
                if swapped == False:
                    break
            return iteraciones, movimientos, consultas
        
        iteraciones, movimientos, consultas = burbuja_mejorada(numeros)



        lista_ordenada_mejorada.config(text=f"Lista Ordenada: {numeros}")
        lista_original_mejorada.config(text=f"Lista Original: {entrada}")
        info_burbuja_mejorada.config(text=f"Iteraciones: {iteraciones}, Movimientos: {movimientos}, Consultas: {consultas}")
    
    boton_ordenar_mejorada = tk.Button(tab_burbuja_mejorada, text="Ordenar", command=ordenar_burbuja_mejorada)
    boton_ordenar_mejorada.pack(pady=10)
    boton_ordenar_mejorada.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    botton_volver_mejorada = tk.Button(tab_burbuja_mejorada, text="Volver", height=1, width=15)
    botton_volver_mejorada.pack(side="bottom", pady=10)
    botton_volver_mejorada.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white", command=ventana_submenu)

################################################################## INSERCIÓN ####################################################################################################

    tab_insercion = ttk.Frame(panel)
    panel.add(tab_insercion, text="Insertion Sort")

    etiqueta_insercion = tk.Label(tab_insercion, text="Ingresa los números a ordenar separados por comas", font=("Arial", 16, "bold"))
    etiqueta_insercion.pack(pady=10)

    entrada_insercion = tk.Entry(tab_insercion)
    entrada_insercion.pack(pady=20)
    entrada_insercion.config(font=("Arial", 12), borderwidth=2, relief="ridge", width=50, justify="center")

    resultado_label_insercion = ttk.Label(tab_insercion, text="", font=("Arial", 12))
    resultado_label_insercion.pack(pady=10)

    lista_ordenada_insercion = ttk.Label(tab_insercion, text="", font=("Arial", 12))
    lista_ordenada_insercion.pack(pady=10)

    lista_original_insercion = ttk.Label(tab_insercion, text="", font=("Arial", 12))
    lista_original_insercion.pack(pady=10)

    info_insercion = ttk.Label(tab_insercion, text="", font=("Arial", 12))
    info_insercion.pack(pady=10)

    def ordenar_insercion():
        entrada = entrada_insercion.get().strip()
        resultado_label_insercion.config(text="")
        
        if not entrada:
            resultado_label_insercion.config(text="Por favor, ingresa números separados por comas.")
            return

        try:
            # Dividir la entrada en una lista de números
            numeros = [int(x) for x in entrada.split(',')]
        except ValueError:
            resultado_label_insercion.config(text="Error: Ingresa números válidos separados por comas.")
            return
        
        # Verificar si la entrada contiene más de 10 números
        if len(numeros) > 10:
            resultado_label_insercion.config(text="Error: No se permiten más de 10 números.")
            return
        
        # Verificar si la entrada contiene menos de 5 números
        if len(numeros) < 5:
            resultado_label_insercion.config(text="Error: Se requieren al menos 5 números.")
            return
        
        def insercion(numbers):
            iterations = 0
            movements = 0
            queries = 0

            for i in range(1, len(numbers)):
                key = numbers[i]
                j = i - 1
                queries += 1
                while j >= 0 and key < numbers[j]:
                    numbers[j + 1] = numbers[j]
                    movements += 1
                    j -= 1
                numbers[j + 1] = key
                iterations += 1

            return iterations, movements, queries
        
        iteraciones, movimientos, consultas = insercion(numeros)




        lista_ordenada_insercion.config(text=f"Lista Ordenada: {numeros}")
        lista_original_insercion.config(text=f"Lista Original: {entrada}")
        info_insercion.config(text=f"Iteraciones: {iteraciones}, Movimientos: {movimientos}, Consultas: {consultas}")

    boton_ordenar_insercion = tk.Button(tab_insercion, text="Ordenar", command=ordenar_insercion)
    boton_ordenar_insercion.pack(pady=10)
    boton_ordenar_insercion.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    botton_volver_insercion = tk.Button(tab_insercion, text="Volver", height=1, width=15)
    botton_volver_insercion.pack(side="bottom", pady=10)
    botton_volver_insercion.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white", command=ventana_submenu)

    ################################################################## QUICKSORT ####################################################################################################

    tab_quicksort = ttk.Frame(panel)
    panel.add(tab_quicksort, text="Quick Sort")

    etiqueta_quicksort = tk.Label(tab_quicksort, text="Ingresa los números a ordenar separados por comas", font=("Arial", 16, "bold"))
    etiqueta_quicksort.pack(pady=10)

    entrada_quicksort = tk.Entry(tab_quicksort)
    entrada_quicksort.pack(pady=20)
    entrada_quicksort.config(font=("Arial", 12), borderwidth=2, relief="ridge", width=50, justify="center")

    resultado_label_quicksort = ttk.Label(tab_quicksort, text="", font=("Arial", 12))
    resultado_label_quicksort.pack(pady=10)

    lista_ordenada_quicksort = ttk.Label(tab_quicksort, text="", font=("Arial", 12))
    lista_ordenada_quicksort.pack(pady=10)

    lista_original_quicksort = ttk.Label(tab_quicksort, text="", font=("Arial", 12))
    lista_original_quicksort.pack(pady=10)

    info_quicksort = ttk.Label(tab_quicksort, text="", font=("Arial", 12))
    info_quicksort.pack(pady=10)




    def ordenar_quicksort():
        entrada = entrada_quicksort.get().strip()
        resultado_label_quicksort.config(text="")

        if not entrada:
            resultado_label_quicksort.config(text="Por favor, ingresa números separados por comas.")
            return

        try:
            # Dividir la entrada en una lista de números
            numeros = [int(x) for x in entrada.split(',')]
        except ValueError:
            resultado_label_quicksort.config(text="Error: Ingresa números válidos separados por comas.")
            return
 
        # Verificar si la entrada contiene más de 10 números
        if len(numeros) > 10:
            resultado_label_quicksort.config(text="Error: No se permiten más de 10 números.")
            return
        
        # Verificar si la entrada contiene menos de 5 números
        if len(numeros) < 5:
            resultado_label_quicksort.config(text="Error: Se requieren al menos 5 números.")
            return

        iterations = 0
        movements = 0
        queries = 0

        def partition(arr, low, high, movements, queries):
            i = (low-1)  # index of smaller element
            pivot = arr[high]  # pivot

            for j in range(low, high):
                queries += 1
        # If current element is smaller than or equal to pivot
                if arr[j] <= pivot:
            # increment index of smaller element
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
                    movements += 1

            arr[i+1], arr[high] = arr[high], arr[i+1]
            movements += 1
            return (i+1, movements, queries)
        
        def quicksort(arr, low, high, iterations, movements, queries):
            if len(arr) == 1:
                return arr
            if low < high:
        # pi is partitioning index, arr[p] is now at right place
                pi, movements, queries = partition(arr, low, high, movements, queries)

        # Separately sort elements before partition and after partition
                iterations += 1
                quicksort(arr, low, pi-1, iterations, movements, queries)
                quicksort(arr, pi+1, high, iterations, movements, queries)
            return (arr, iterations, movements, queries)
        


        numeros, iterations, movements, queries = quicksort(numeros, 0, len(numeros)-1, iterations, movements, queries)
    
        lista_ordenada_quicksort.config(text=f"Lista Ordenada: {numeros}")
        lista_original_quicksort.config(text=f"Lista Original: {entrada}")
        info_quicksort.config(text=f"Iteraciones: {iterations}, Movimientos: {movements}, Consultas: {queries}")


    boton_ordenar_quicksort = tk.Button(tab_quicksort, text="Ordenar", command=ordenar_quicksort)
    boton_ordenar_quicksort.pack(pady=10)
    boton_ordenar_quicksort.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    botton_volver_quicksort = tk.Button(tab_quicksort, text="Volver", height=1, width=15)
    botton_volver_quicksort.pack(side="bottom", pady=10)
    botton_volver_quicksort.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white", command=ventana_submenu)

    ################################################################## MERGESORT ####################################################################################################
    tab_mergesort = ttk.Frame(panel)
    panel.add(tab_mergesort, text="Merge Sort")

    etiqueta_mergesort = tk.Label(tab_mergesort, text="Ingresa los números a ordenar separados por comas", font=("Arial", 16, "bold"))
    etiqueta_mergesort.pack(pady=10)

    entrada_mergesort = tk.Entry(tab_mergesort)
    entrada_mergesort.pack(pady=20)
    entrada_mergesort.config(font=("Arial", 12), borderwidth=2, relief="ridge", width=50, justify="center")

    resultado_label_mergesort = ttk.Label(tab_mergesort, text="", font=("Arial", 12))
    resultado_label_mergesort.pack(pady=10)

    lista_ordenada_mergesort = ttk.Label(tab_mergesort, text="", font=("Arial", 12))
    lista_ordenada_mergesort.pack(pady=10)

    lista_original_mergesort = ttk.Label(tab_mergesort, text="", font=("Arial", 12))
    lista_original_mergesort.pack(pady=10)

    info_mergesort = ttk.Label(tab_mergesort, text="", font=("Arial", 12))
    info_mergesort.pack(pady=10)

    def ordenar_mergesort():
        entrada = entrada_mergesort.get().strip()
        resultado_label_mergesort.config(text="")

        if not entrada:
            resultado_label_mergesort.config(text="Por favor, ingresa números separados por comas.")
            return

        try:
            # Dividir la entrada en una lista de números
            numeros = [int(x) for x in entrada.split(',')]
        except ValueError:
            resultado_label_mergesort.config(text="Error: Ingresa números válidos separados por comas.")
            return
        
        # Verificar si la entrada contiene números repetidos
        if len(numeros) != len(set(numeros)):
            resultado_label_mergesort.config(text="Error: No se permiten números repetidos.")
            return

        # Verificar si la entrada contiene más de 10 números
        if len(numeros) > 10:
            resultado_label_mergesort.config(text="Error: No se permiten más de 10 números.")
            return
        
        # Verificar si la entrada contiene menos de 5 números
        if len(numeros) < 5:
            resultado_label_mergesort.config(text="Error: Se requieren al menos 5 números.")
            return
        
        def mergesort(arr):
            movimientos = 0
            consultas = 0
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]
                movimientos_izquierda, consultas_izquierda = mergesort(L)
                movimientos_derecha, consultas_derecha = mergesort(R)
                movimientos += movimientos_izquierda + movimientos_derecha
                consultas += consultas_izquierda + consultas_derecha
                i = j = k = 0
                while i < len(L) and j < len(R):
                    consultas += 1
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                    movimientos += 1
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                    movimientos += 1
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
                    movimientos += 1
            return movimientos, consultas
        
        movimientos, consultas = mergesort(numeros)

        lista_ordenada_mergesort.config(text=f"Lista Ordenada: {numeros}")
        lista_original_mergesort.config(text=f"Lista Original: {entrada}")
        info_mergesort.config(text=f"Iteraciones: {len(numeros) - 1}, Movimientos: {movimientos}, Consultas: {consultas}")

    boton_ordenar_mergesort = tk.Button(tab_mergesort, text="Ordenar", command=ordenar_mergesort)
    boton_ordenar_mergesort.pack(pady=10)
    boton_ordenar_mergesort.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white")

    botton_volver_mergesort = tk.Button(tab_mergesort, text="Volver", height=1, width=15)
    botton_volver_mergesort.pack(side="bottom", pady=10)
    botton_volver_mergesort.config(font=("Arial", 12, "bold"), borderwidth=2, relief="ridge", bg="#151918", fg="white", command=ventana_submenu)



################################################################# VENTANA ARBOLES ##########################################################

def ventana_arboles():
    for widget in ventana.winfo_children():
        widget.destroy()
    fondo()

    ventana.geometry("400x400")
    ventana.resizable(False, False)
    ventana.config(bg="#FFFFF3")

    # Botones "Ver datos" y "Ordenamientos" centrados y más grandes
    arbol_binario_button = tk.Button(ventana, text="Arbol Binario", height=3, width=15,command=ventana_arbol_binario)
    arbol_binario_button.pack(pady=20)
    arbol_binario_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")

    arbol_avl_button = tk.Button(ventana, text="Arbol AVL", height=3, width=15,command=ventana_arbol_avl)
    arbol_avl_button.pack(pady=20)
    arbol_avl_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")
    
    # Botón "Volver al Menú Principal" en la parte inferior
    volver_button = tk.Button(ventana, text="Volver",height=3,width=15,command=ventana_submenu)
    volver_button.pack(side="bottom",pady=10)
    volver_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")


##################################################### ARBOL BINARIO ##########################################################
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
def create_binary_tree():
    global entrada_arbol_binario
    # Limpia el lienzo antes de dibujar el árbol
    canvas.delete("all")
    # Obtiene la entrada del usuario y crea el árbol binario
    input_str = entrada_arbol_binario.get().strip()
    try:
        # Convertir la entrada del usuario en una lista de números
        numbers = [float(num_str) for num_str in input_str.split(",")]
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números separados por comas.")
        return

    # Crea un nodo raíz
    root = Node(numbers[0])

    # Inserta el resto de los números en el árbol
    for num in numbers[1:]:
        root.insert(num)

    # Limpia el lienzo antes de dibujar el árbol
    canvas.delete("all")

    # Función para dibujar el árbol en el lienzo
    def draw_tree(node, x, y, dx, level=1):
        if node:
            canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white")
            canvas.create_text(x, y, text=str(node.data))

            y_spacing = 100  # Espaciado vertical
            if node.left:
                canvas.create_line(x, y + 15, x - dx, y + y_spacing)
                draw_tree(node.left, x - dx, y + y_spacing, dx / 2, level + 1)
            if node.right:
                canvas.create_line(x, y + 15, x + dx, y + y_spacing)
                draw_tree(node.right, x + dx, y + y_spacing, dx / 2, level + 1)

    dx = 250  # Espaciado horizontal
    dy = 200  # Espaciado vertical

    draw_tree(root, canvas.winfo_width() // 2, 50, dx)

    # Actualiza el área de desplazamiento del lienzo, permitiendo el desplazamiento horizontal
    canvas.config(scrollregion=canvas.bbox("all"), xscrollcommand=horizontal_scrollbar.set)

    
        

################################################################# VENTANA ARBOL BINARIO ##########################################################
def ventana_arbol_binario():
    global canvas, entrada_arbol_binario, horizontal_scrollbar, vertical_scrollbar
    for widget in ventana.winfo_children():
        widget.destroy()
    ventana.title("Árbol Binario")
    ventana.geometry("500x500")
    ventana.resizable(False, False)
    ventana.config(bg="#FFFFF3")

# Agrega una etiqueta y una entrada de texto
    label = tk.Label(ventana, text="Ingrese una lista de números separados por comas:")
    result_label = tk.Label(ventana, text="")
    result_label.pack()
    label.pack(pady=10)
    label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")


    entrada_arbol_binario = tk.Entry(ventana)
    entrada_arbol_binario.pack(pady=10)
    entrada_arbol_binario.config(font=("Arial", 12),borderwidth=2, relief="ridge")

# Agrega un botón para crear el árbol
    crear_arbol_binario_botton = tk.Button(ventana, text="Crear Árbol Binario",height=2,width=15,command=create_binary_tree)
    crear_arbol_binario_botton.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")
    crear_arbol_binario_botton.pack(side="top",pady=10)

    volver_button = tk.Button(ventana, text="Volver",height=2,width=15,command=ventana_arboles)
    volver_button.pack(side="bottom",pady=10)
    volver_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")
    

# Agrega un lienzo (canvas) con barras de desplazamiento vertical y horizontal
    canvas = tk.Canvas(ventana, width=100, height=100)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Agrega una barra de desplazamiento vertical
    vertical_scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    vertical_scrollbar.pack(side="right", fill="y")

# Agrega una barra de desplazamiento horizontal
    horizontal_scrollbar = tk.Scrollbar(ventana, orient="horizontal", command=canvas.xview)
    horizontal_scrollbar.pack(side="bottom", fill="x")

# Crea un marco para contener el contenido del lienzo
    frame = tk.Frame(canvas)
    canvas.create_window((4, 4), window=frame, anchor="nw")
################################################################" ARBOL AVL ##########################################################
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def insert(self, node, data):
        if not node:
            return AVLNode(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        self._update_height(node)

        balance = self._balance_factor(node)

        if balance > 1:
            if data < node.left.data:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if data > node.right.data:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

class TreeVisualization:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        self.draw_tree(self.root, 300, 50, 200)

    def draw_tree(self, node, x, y, dx):
        if node:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white")
            self.canvas.create_text(x, y, text=str(node.data))

            y_spacing = 100  # Espaciado vertical
            if node.left:
                self.canvas.create_line(x, y + 15, x - dx, y + y_spacing)
                self.draw_tree(node.left, x - dx, y + y_spacing, dx / 2)
            if node.right:
                self.canvas.create_line(x, y + 15, x + dx, y + y_spacing)
                self.draw_tree(node.right, x + dx, y + y_spacing, dx / 2)

def create_avl_tree():
    global entrada_arbol_avl, canvas, horizontal_scrollbar
    # Limpia el lienzo antes de dibujar el árbol AVL
    canvas.delete("all")
    
    input_str = entrada_arbol_avl.get().strip()
    try:
        numbers = [float(num_str) for num_str in input_str.split(",")]
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números separados por comas.")
        return

    avl_tree = AVLTree()
    
    for num in numbers:
        avl_tree.root = avl_tree.insert(avl_tree.root, num)

    # Limpia el lienzo antes de dibujar el árbol AVL
    canvas.delete("all")

    def draw_avl_tree(node, x, y, dx):
        if node:
            canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white")
            canvas.create_text(x, y, text=str(node.data))

            y_spacing = 100  # Espaciado vertical
            if node.left:
                canvas.create_line(x, y + 15, x - dx, y + y_spacing)
                draw_avl_tree(node.left, x - dx, y + y_spacing, dx / 2)
            if node.right:
                canvas.create_line(x, y + 15, x + dx, y + y_spacing)
                draw_avl_tree(node.right, x + dx, y + y_spacing, dx / 2)

    dx = 250  # Espaciado horizontal
    dy = 200  # Espaciado vertical

    draw_avl_tree(avl_tree.root, canvas.winfo_width() // 2, 50, dx)

    # Actualiza el área de desplazamiento del lienzo, permitiendo el desplazamiento horizontal
    canvas.config(scrollregion=canvas.bbox("all"), xscrollcommand=horizontal_scrollbar.set)







################################################################# VENTANA ARBOL AVL ##########################################################
def ventana_arbol_avl():
    global canvas, entrada_arbol_avl, horizontal_scrollbar, vertical_scrollbar
    for widget in ventana.winfo_children():
        widget.destroy()
    ventana.title("Árbol AVL")
    ventana.geometry("500x500")
    ventana.resizable(False, False)
    ventana.config(bg="#FFFFF3")

# Agrega una etiqueta y una entrada de texto
    label = tk.Label(ventana, text="Ingrese una lista de números separados por comas:")
    label.pack(pady=10)
    label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")


    entrada_arbol_avl = tk.Entry(ventana)
    entrada_arbol_avl.pack(pady=10)
    entrada_arbol_avl.config(font=("Arial", 12),borderwidth=2, relief="ridge")

# Agrega un botón para crear el árbol
    crear_arbol_avl_botton = tk.Button(ventana, text="Crear Árbol AVL",height=2,width=15,command=create_avl_tree)
    crear_arbol_avl_botton.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")
    crear_arbol_avl_botton.pack(side="top",pady=10)

    volver_button = tk.Button(ventana, text="Volver",height=2,width=15,command=ventana_arboles)
    volver_button.pack(side="bottom",pady=10)
    volver_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")
    

# Agrega un lienzo (canvas) con barras de desplazamiento vertical y horizontal
    canvas = tk.Canvas(ventana, width=100, height=100)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Agrega una barra de desplazamiento vertical
    vertical_scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
    vertical_scrollbar.pack(side="right", fill="y")

# Agrega una barra de desplazamiento horizontal
    horizontal_scrollbar = tk.Scrollbar(ventana, orient="horizontal", command=canvas.xview)
    horizontal_scrollbar.pack(side="bottom", fill="x")

# Crea un marco para contener el contenido del lienzo
    frame = tk.Frame(canvas)
    canvas.create_window((4, 4), window=frame, anchor="nw")

# Agrega una etiqueta para mostrar errores
    result_label = tk.Label(ventana, text="")
    result_label.pack()
################################################################## VENTANA REGISTRO  ####################################################################################################
# Función para cambiar la ventana a la ventana de registro
def ventana_registro():
    global username_entry, password_entry, numero_entry, hogar_entry
    # Borrar elementos de la ventana principal
    for widget in ventana.winfo_children():
        widget.destroy()
    
    #fondo
    fondo()


    # Etiquetas y campos de entrada en la ventana de registro
    username_label = tk.Label(ventana, text="Usuario: ")
    username_label.pack(pady=5)
    username_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="#F4A50E",anchor="center", justify="center")

    username_entry = tk.Entry(ventana)
    username_entry.pack(pady=5)
    username_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    password_label = tk.Label(ventana, text="Contraseña: ")
    password_label.pack(pady=5)
    password_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="#F4A50E")

    password_entry = tk.Entry(ventana, show="*")
    password_entry.pack(pady=5)
    password_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    numero_label = tk.Label(ventana, text="Número favorito: ")
    numero_label.pack(pady=5)
    numero_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="#F4A50E")

    numero_entry = tk.Entry(ventana)
    numero_entry.pack(pady=5)
    numero_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    hogar_label = tk.Label(ventana, text="Lugar de nacimiento: ")
    hogar_label.pack(pady=5)
    hogar_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="#F4A50E")

    hogar_entry = tk.Entry(ventana)
    hogar_entry.pack(pady=5)
    hogar_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    # Botones para registrar y volver al menú principal
    registrar_button = tk.Button(ventana, text="Registrar", command=registrar)
    registrar_button.pack(pady=10)
    registrar_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")

    volver_button = tk.Button(ventana, text="Volver al Menú Principal", command=menu_principal)
    volver_button.pack(pady=10)
    volver_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="ridge",bg="#151918",fg="white")

    

# Función para cambiar la ventana de nuevo al menú principal
def menu_principal():
    global username_entry, password_entry
    # Borrar elementos de la ventana de registro
    for widget in ventana.winfo_children():
        widget.destroy()

    titulo = tk.Label(ventana, text="\nINICIAR SESIÓN", font=("Arial", 16, "bold"))
    titulo.pack()
    titulo.config(bg="#fffff5",fg="#F4A50E")

    
    #fondo
    fondo()
    
    
    # Etiquetas y campos de entrada en la ventana de inicio de sesión
    username_label = tk.Label(ventana, text="Usuario:")
    username_label.pack(pady=5)
    username_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="raised",bg="#151918",fg="#F4A50E")

    username_entry = tk.Entry(ventana)
    username_entry.pack(pady=5)
    username_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    password_label = tk.Label(ventana, text="Contraseña:")
    password_label.pack(pady=5)
    password_label.config(font=("Arial", 12,"bold"),borderwidth=2, relief="raised",bg="#151918",fg="#F4A50E")

    password_entry = tk.Entry(ventana, show="*")
    password_entry.pack(pady=5)
    password_entry.config(font=("Arial", 12),borderwidth=2, relief="ridge")

    # Botones para iniciar sesión y registrar
    login_button = tk.Button(ventana, text="Iniciar Sesión", command=login)
    login_button.pack(pady=10)
    login_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="groove",bg="#151918",fg="white")

    registro_button = tk.Button(ventana, text="Registrar", command=ventana_registro)
    registro_button.pack(pady=10)
    registro_button.config(font=("Arial", 12,"bold"),borderwidth=2, relief="groove",bg="#151918",fg="white")

ventana = tk.Tk()
ventana.title("CRUD SYSTEM BY GE0SH")
#ventana.resizable(False, False)
ventana.geometry("400x400")
ventana.resizable(False, False)

cargar_datos()

menu_principal()
ventana.mainloop()
