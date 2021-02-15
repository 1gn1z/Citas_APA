# Importacion de Pyfiglet para el banner (Inicial de Figlet con mayusculas!)

from pyfiglet import Figlet

# Indicamos la fuente para el banner, guardada en una variable

banner = Figlet(font="standard")

# Imprimimos el texto que queramos como banner
print(banner.renderText('Citas  APA'))

