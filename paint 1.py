from tkinter import *
from tkinter import filedialog, colorchooser
from tkinter import messagebox

# Función para abrir un archivo
def abrirArchivo():
    archivo = filedialog.askopenfilename(title='Abrir', filetypes=[('Archivos de imagen', '*.jpg *.png *.bmp')])
    if archivo:
        print(f'Archivo abierto: {archivo}')  # Aquí puedes añadir funcionalidad para cargar la imagen

# Función para guardar el dibujo
def guardarArchivo():
    archivo = filedialog.asksaveasfilename(title='Guardar', defaultextension='.png', filetypes=[('PNG', '*.png'), ('JPG', '*.jpg')])
    if archivo:
        print(f'Archivo guardado: {archivo}')  # Aquí puedes añadir funcionalidad para guardar la imagen

# Función para salir de la aplicación
def salirAplicacion():
    respuesta = messagebox.askokcancel('Salir', '¿Seguro que quieres salir?')
    if respuesta:
        raiz.quit()

# Función para escoger el color del pincel
def escogerColor():
    color = colorchooser.askcolor(title='Escoger color')
    if color[1]:
        lienzo.config(fg=color[1])

# Inicialización de la ventana principal
raiz = Tk()
raiz.title('Mini Paint')
raiz.geometry('600x400')

# Menú
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
archivoMenu.add_command(label='Abrir', command=abrirArchivo)
archivoMenu.add_command(label='Nuevo', command=lambda: lienzo.delete('all'))  # Borra el lienzo
archivoMenu.add_separator()
archivoMenu.add_command(label='Guardar', command=guardarArchivo)
archivoMenu.add_command(label='Salir', command=salirAplicacion)

# Lienzo para dibujar
lienzo = Canvas(raiz, bg='white', width=500, height=300)
lienzo.pack(expand=True, fill='both')

# Variables para el dibujo
color = 'black'
grosor = 2

# Función para dibujar con el mouse
def pintar(event):
    x1, y1 = (event.x - grosor), (event.y - grosor)
    x2, y2 = (event.x + grosor), (event.y + grosor)
    lienzo.create_oval(x1, y1, x2, y2, fill=color, outline=color)

# Asociar el evento de dibujo
lienzo.bind('<B1-Motion>', pintar)

# Botón para escoger color
botonColor = Button(raiz, text='Escoger Color', command=escogerColor)
botonColor.pack(side='left')

# Botón para limpiar el lienzo
botonLimpiar = Button(raiz, text='Limpiar', command=lambda: lienzo.delete('all'))
botonLimpiar.pack(side='left')

raiz.mainloop()
