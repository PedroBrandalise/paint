try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *



class Ferramentas:
	"""docstring for Ferramentas"""
	
	tamanho_ponteiro=2
	########### DEFINICAO DE MODOS
	MODO = 0
	DESENHO_COMUM=0
	DESENHO_COM_LINHA=1
	###########

	def __init__(self, master=None):

		self.MODO=0

		self.tamanho_ponteiro=2

		self.widget1=Frame(master)
		self.widget1.pack()
		
		self.widget2=Frame(master)
		self.widget2.pack()
		
		self.widget3=Frame(master)
		self.widget3.pack()

		self.widget4=Frame(master)
		self.widget4.pack()

		self.widget6=Frame(master)
		self.widget6.pack()

		self.widget5=Frame(master)
		self.widget5.pack()
		
		self.msg = Label(self.widget1, text="Ferramentas")
		self.msg.pack()

		self.lapis = Button(self.widget1)
		self.lapis["width"]= 1
		self.lapis["text"]='lapis'
		self.lapis.bind("<Button-1>", self.selecionalapis)
		self.lapis.pack(side=RIGHT)

		self.pincel = Button(self.widget1)
		self.pincel["width"]= 1
		self.pincel["text"]='pincel'
		self.pincel.bind("<Button-1>", self.selecionapincel)
		self.pincel.pack(side=RIGHT)

		self.linha = Button(self.widget2)
		self.linha["width"]= 1
		self.linha["text"]='linha'
		self.linha.bind("<Button-1>", self.selecionalinha)
		self.linha.pack(side=RIGHT)


	def selecionalapis(self,event):
		self.MODO=0
		self.tamanho_ponteiro=2
		
	def selecionapincel(self,event):
		self.MODO=0
		self.tamanho_ponteiro = 5
		#print('entrou')

	def selecionalinha(self,event):
		self.MODO=1