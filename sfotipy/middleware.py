from random import choice
from django.shortcuts import redirect

paises = ['Peru', 'Mexico', 'Colombia']

def de_donde_vengo(req):
	return choice(paises)

class PaisMiddleware():
	def process_request(self, req):
		pais = de_donde_vengo(req)

		if pais == 'Mexico':
			return redirect('http://mejorando.la/')
		
