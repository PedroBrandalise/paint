#SALVAR	
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import threading
import paint


class Salvar:
	def __init__(self, master=None):
		self.widget1=Frame(master)
		self.widget1.pack()

		self.label=Label(self.widget1,text="Informe com qual nome o arquivo sera salvo")
		self.label.pack()

		self.nome = Entry(self.widget1)
		self.nome["width"] = 30
		self.nome.pack()

		self.salvar=Button(self.widget1)
		self.salvar["text"]="Salvar"
		self.salvar["command"]= self.salvarArquivo
		self.salvar.pack()

	def salvarArquivo(self):
		nomeArq=self.nome.get()
		paint.cv2.imwrite(nomeArq+'.png',img)

	def Salvar():
		root = Tk()
		Salvar(root)
		root.mainloop()