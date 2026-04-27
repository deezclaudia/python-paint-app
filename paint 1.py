from tkinter import *
from tkinter import filedialog, colorchooser
from tkinter import messagebox

def abrirArchivo():
    archivo = filedialog.askopenfilename(
        title='Abrir',
        filetypes=[('Archivos de imagen', '*.jpg *.png *.bmp')]
    )
    if archivo:
        print(f'Archivo abierto: {archivo}')

def guardarArchivo():
    archivo = filedialog.asksaveasfilename(
        title='Guardar',
        defaultextension='.png',
        filetypes=[('PNG', '*.png'), ('JPG', '*.jpg')]
    )
    if archivo:
        print(f'Archivo guardado: {archivo}')


def salirAplicacion():
    respuesta = messagebox.askokcancel('Salir', '¿Seguro que quieres salir?')
    if respuesta:
        raiz.quit()

def escogerColor():
    global color
    nuevo_color = colorchooser.askcolor(title='Escoger color')[1]
    if nuevo_color:
        color = nuevo_color

raiz = Tk()
raiz.title('Mini Paint')
raiz.geometry('600x400')

# Menú
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='Archivo', menu=archivoMenu)
archivoMenu.add_command(label='Abrir', command=abrirArchivo)
archivoMenu.add_command(label='Nuevo', command=lambda: lienzo.delete('all'))
archivoMenu.add_separator()
archivoMenu.add_command(label='Guardar', command=guardarArchivo)
archivoMenu.add_command(label='Salir', command=salirAplicacion)

lienzo = Canvas(raiz, bg='white', width=500, height=300)
lienzo.pack(expand=True, fill='both')

color = 'black'
grosor = 2


def pintar(event):
    x1, y1 = (event.x - grosor), (event.y - grosor)
    x2, y2 = (event.x + grosor), (event.y + grosor)
    lienzo.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    
lienzo.bind('<B1-Motion>', pintar)

botonColor = Button(raiz, text='Escoger Color', command=escogerColor)
botonColor.pack(side='left')

botonLimpiar = Button(raiz, text='Limpiar', command=lambda: lienzo.delete('all'))
botonLimpiar.pack(side='left')

raiz.mainloop()
