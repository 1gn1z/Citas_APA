import dns.resolver

def main():
	try:
		# El query toma 2 parametros, la página y el código de dns
		target1 = input('Ingresa la página >>> ')
		target = dns.resolver.query(target1, "A")
		for i in target:
			print(i)
	except:
		print('Información no disponible')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()