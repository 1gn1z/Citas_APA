#!/usr/bin/python
import dns.resolver
from collections import OrderedDict
from pyfiglet import Figlet

banner = Figlet(font="standard")

# Imprimimos el texto que queramos como banner
print(banner.renderText('Dns-One'))
print(banner.renderText('by  1gn1z'))



def main():
	try:
		# El query toma 2 parametros, la página y el código de dns

		target_link = input('Ingresa la página ejemplo: pagina.com >>> ')
		target = dns.resolver.query(target_link, "A")
		for i in target:
			print(i)
	except:
		print('Información no disponible')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()



"""
A Host Address 
	


"""



