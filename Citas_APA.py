# Importacion de Pyfiglet para el banner (Inicial de Figlet con mayusculas!)

from pyfiglet import Figlet

# Indicamos la fuente para el banner, guardada en una variable

banner = Figlet(font="standard")

# Imprimimos el texto que queramos como banner
print(banner.renderText('Citas  APA'))

print('\nMuy bienvenidos a mi programa para citar en formato APA\n')
# Menú

print('1.- Si tu fuente es un LIBRO')
print('2.- Si tu fuente es un REVISTA')
print('3.- Si tu fuente es un PERIÓDICO')
print('4.- Si tu fuente es un artículo de ENCICLOPEDIA')
print('5.- Si tu fuente es un artículo o capítulo de un LIBRO')
print('6.- Si tu fuente es un artículo de PÁGINA WEB')
print('7.- Si tu fuente es el artículo de un PERIÓDICO, un JOURNAL (Publicación académica especializada.) o REVISTA en una BASE DE DATOS ')
print('\n8.- MENU')
print('\n9.- Para SALIR')
print()
print()


def menu():
    opcion = None
    while opcion != '8':
        if opcion == '1':
            print('opcion 1 elegida')
        elif opcion == '2':
            print('opcion 2')
        elif opcion == '3':
            print('opcion 3')    
        elif opcion == '4':
            print('opcion 4')   
        elif opcion == '5':
            print('opcion 5')
        elif opcion == '6':
            articulo_web()
        elif opcion == '7':
            print('opcion 7')
        elif opcion == '8':
            opciones()
        elif opcion == '9':
            print('Salir')      
        else:
            print('opcion invalida, favor de verificar')

        opcion = input('Elige una opcion: ')


def articulo_web():
    print()
    autor = input('\nAutor(es). En el campo "Autor" sólo se escribe el apellido paterno y de los nombres, \n'
    'únicamente se escribe la letra inicial abreviada con punto. (Ejemplo: Okuda, M.).\n')
    anio = input('\nAño de publicación:\n')
    titulo = input('\nTítulo del artículo:\n')
    fecha = input('\nFecha de recuperación del documento: \n'
    'La fecha va en el formato: Mes, día, año(Ejemplo: diciembre 20, 2007)\n')
    asociacion = input('\nAsociación que publica el artículo: \n')
    url = input('\nURL: \n')
    print('\n\nTu ficha es:\n')
#            print(autor + titulo + fecha + asociacion + url)
    print(f'{autor}. ({anio}). {titulo}. {fecha}, de {asociacion} Sitio web: {url}')
    print('\n')


if __name__ == "__main__":
    menu()