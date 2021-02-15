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
print()
print()
opcion = int(input('Elige una opcion: '))
