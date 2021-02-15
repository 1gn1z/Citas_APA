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
print('\n8.- Para SALIR')
print()
print()

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
        print('opcion 6')
    elif opcion == '7':
        print('opcion 7')  
    elif opcion == '8':
        print('Salir')      
    else:
        print('opcion invalida, favor de verificar')

    opcion = input('Elige una opcion: ')