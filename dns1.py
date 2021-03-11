import dns.resolver

def main():
	try:
		# El query toma 2 parametros, la página y el código de dns
		target = dns.resolver.query("www.cicap.edu.mx", "MD")
		for i in target:
			print(i)
	except:
		print('Información no disponible')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()