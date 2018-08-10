try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import threading

color=(0,0,0)

class Cores:

	def change2preto(self, event):
		global color
		color = (0,0,0)

	def change2branco(self, event):
		global color
		color = (255,255,255)

	def change2cinza1(self, event):
		global color
		color = (70,70,70)

	def change2cinza2(self, event):
		global color
		color = (220,220,220)

	def change2vermelho1(self, event):
		global color
		color = (153,0,48)

	def change2marrom1(self, event):
		global color
		color = (156,90,60)

	def change2vermelho2(self, event):
		global color
		color = (237,28,36)

	def change2rosa(self, event):
		global color
		color = (255,163,177)

	def change2laranja1(self, event):
		global color
		color = (155,126,0)

	def change2marrom2(self, event):
		global color
		color = (229,170,122)

	def change2amarelo(self, event):
		global color
		color = (255,194,14)

	def change2amarelo2(self, event):
		global color
		color = (245,228,156)


	def __init__(self, master=None):
		
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

		self.msg = Label(self.widget1, text="cores")
		self.msg.pack()
		
		self.preto = Button(self.widget1)
		self.preto["width"]= 1
		self.preto["bg"]='black'
		self.preto.bind("<Button-1>", self.change2preto)
		self.preto.pack(side=LEFT)

		self.branco = Button(self.widget1)
		self.branco["width"]= 1
		self.branco["bg"]='white'
		self.branco.bind("<Button-1>", self.change2branco)
		self.branco.pack(side=RIGHT)
		
		self.cinza1 = Button(self.widget2)
		self.cinza1["width"]= 1
		self.cinza1["bg"]='#464646'
		self.cinza1.bind("<Button-1>", self.change2cinza1)
		self.cinza1.pack(side=LEFT)

		self.cinza2 = Button(self.widget2)
		self.cinza2["width"]= 1
		self.cinza2["bg"]='#DCDCDC'
		self.cinza2.bind("<Button-1>", self.change2cinza2)
		self.cinza2.pack(side=RIGHT)

		self.vermelho1 = Button(self.widget3)
		self.vermelho1["width"]= 1
		self.vermelho1["bg"]='#990030'
		self.vermelho1.bind("<Button-1>", self.change2vermelho1)
		self.vermelho1.pack(side=LEFT)

		self.marrom1 = Button(self.widget3)
		self.marrom1["width"]= 1
		self.marrom1["bg"]='#9C5A3C'
		self.marrom1.bind("<Button-1>", self.change2marrom1)
		self.marrom1.pack(side=RIGHT)

		self.vermelho2 = Button(self.widget4)
		self.vermelho2["width"]= 1
		self.vermelho2["bg"]='#ED1C24'
		self.vermelho2.bind("<Button-1>", self.change2vermelho2)
		self.vermelho2.pack(side=LEFT)

		self.rosa = Button(self.widget4)
		self.rosa["width"]= 1
		self.rosa["bg"]='#FFA3B1'
		self.rosa.bind("<Button-1>", self.change2rosa)
		self.rosa.pack(side=RIGHT)
		
		self.laranja1 = Button(self.widget5)
		self.laranja1["width"]= 1
		self.laranja1["bg"]='#9B7E00'
		self.laranja1.bind("<Button-1>", self.change2laranja1)
		self.laranja1.pack(side=RIGHT)

		self.marrom2 = Button(self.widget5)
		self.marrom2["width"]= 1
		self.marrom2["bg"]='#E5AA7A'
		self.marrom2.bind("<Button-1>", self.change2marrom2)
		self.marrom2.pack(side=RIGHT)

		self.amarelo = Button(self.widget6)
		self.amarelo["width"]= 1
		self.amarelo["bg"]='#FFC20E'
		self.amarelo.bind("<Button-1>", self.change2amarelo)
		self.amarelo.pack(side=RIGHT)

		self.amarelo2 = Button(self.widget6)
		self.amarelo2["width"]= 1
		self.amarelo2["bg"]='#F5E49C'
		self.amarelo2.bind("<Button-1>", self.change2amarelo2)
		self.amarelo2.pack(side=RIGHT)


	def startCores():
		root = Tk()
		Cores(root)
		root.mainloop()

