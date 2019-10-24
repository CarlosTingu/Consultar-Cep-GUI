# coding: utf-8
import requests
import time
import json

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("consultar-cep.glade")
	
# Funções do programa

def consultarCep(widget):
	# Selecionando widgets
	inputCep = builder.get_object('inputCep')
	resulLogradouro = builder.get_object('resulLogradouro')
	resulComplemento = builder.get_object('resulComplemento')
	resulBairro = builder.get_object('resulBairro')
	resulLocalidade = builder.get_object('resulLocalidade')
	resulUf = builder.get_object('resulUf')
	resulIbge = builder.get_object('resulIbge')
	
	# Pegando valor do campo
	valueCep = inputCep.get_text()
	
	if valueCep.isnumeric() == False or len(valueCep) < 8:
		inputCep.set_text('Inválido')
		
		# Mostando resultado da pesquisa
		resulLogradouro.set_text('?')
		resulComplemento.set_text('?')
		resulBairro.set_text('?')
		resulLocalidade.set_text('?')
		resulUf.set_text('?')
		resulIbge.set_text('?')
	else:	
		# Fazendo requisição Api ViaCep
		try:
			req = requests.get('https://viacep.com.br/ws/{}/json'.format(valueCep))
			res = req.json()
			
			if 'erro' in res:
				inputCep.set_text('Inválido')

				# Mostando resultado da pesquisa
				resulLogradouro.set_text('?')
				resulComplemento.set_text('?')
				resulBairro.set_text('?')
				resulLocalidade.set_text('?')
				resulUf.set_text('?')
				resulIbge.set_text('?')
			else:
				# Mostando resultado da pesquisa
				resulLogradouro.set_text(res['logradouro'])
				resulComplemento.set_text(res['complemento'])
				resulBairro.set_text(res['bairro'])
				resulLocalidade.set_text(res['localidade'])
				resulUf.set_text(res['uf'])
				resulIbge.set_text(res['ibge'])
		except:
			print('Sem conexão com a internet !')
			exit()
		
def limparCampo(widget):
	# Selecionando campo
	inputCep = builder.get_object('inputCep')
	valueCep = inputCep.set_text('')
	
	# Selecionando widgets
	resulLogradouro = builder.get_object('resulLogradouro')
	resulComplemento = builder.get_object('resulComplemento')
	resulBairro = builder.get_object('resulBairro')
	resulLocalidade = builder.get_object('resulLocalidade')
	resulUf = builder.get_object('resulUf')
	resulIbge = builder.get_object('resulIbge')
	
	# Mostando resultado da pesquisa
	resulLogradouro.set_text('?')
	resulComplemento.set_text('?')
	resulBairro.set_text('?')
	resulLocalidade.set_text('?')
	resulUf.set_text('?')
	resulIbge.set_text('?')

# -------------------

# Eventos do programa

handlers = {
	'onDestroy': Gtk.main_quit,
	'btnLocalizarClicked': consultarCep,
	'btnLimparClicked': limparCampo
}

# -------------------
builder.connect_signals(handlers)
window = builder.get_object("window1")
window.show_all()
Gtk.main()
