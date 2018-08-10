import cv2
import numpy as np
import cores
from Tkinter import *
from PIL import Image
from PIL import ImageTk 
import tkFileDialog
import paint as paintarq
import ferramentas as ferramentasarq


primeiroClick=False

x=-10
y=-10
xpc=-10
ypc=-10
def chamarPainel(imagem):
	global painel
	#recebe a imagem em branco
	imagem=cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
	#converte a imagem para o formado PIL
	imagem=Image.fromarray(imagem)

	#converte para o Tk
	imagem2=ImageTk.PhotoImage(imagem)

	#image = Image.open("foto.jpeg")
	#photo = itk.PhotoImage(image)


	painel=Label(image=imagem2,cursor="cross")
	painel.imagem2 = imagem2
	painel.pack(side="right")

def motion(event):
	global x, y, xpc,ypc, primeiroClick
	if ferramentas.MODO==0:
		x, y = event.x, event.y
		#retorna a imagem apos o desenho
		i=paint.desenhar(x,y,ferramentas.tamanho_ponteiro)
	elif ferramentas.MODO==1:
		if primeiroClick==False:
			i=paint.desenhar(event.x,event.y,ferramentas.tamanho_ponteiro)
			primeiroClick=True
			xpc,ypc=event.x,event.y
		else:
			primeiroClick=False
			i=paint.desenhar2(xpc,ypc,event.x,event.y,ferramentas.tamanho_ponteiro)


	try:
		i=Image.fromarray(i)
		#recebe a imagem q pode ser colocada no TK
		i=ImageTk.PhotoImage(i)
		
		#substitui a imagem no tk
		painel.configure(image=i)
		painel.i=i
	except:
		pass



def motion2(event):
	if ferramentas.MODO==0:
		global x, y
		xa,ya=x,y
		x, y = event.x, event.y

		i=paint.desenhar2(xa,ya,x,y,ferramentas.tamanho_ponteiro)
		i=Image.fromarray(i)
		#recebe a imagem q pode ser colocada no TK
		i=ImageTk.PhotoImage(i)
		
		#substitui a imagem no tk
		painel.configure(image=i)
		painel.i=i
	else:
		pass
	
def borracha(event):
	global x, y
	x, y = event.x, event.y
	#retorna a imagem apos o desenho
	i=paint.apagar(x,y)
	i=Image.fromarray(i)
	#recebe a imagem q pode ser colocada no TK
	i=ImageTk.PhotoImage(i)
	
	#substitui a imagem no tk
	painel.configure(image=i)
	painel.i=i


def salvar(event):
	print("oi")
	if event.char== 's':
		tkFileDialog.askopenfilename()
		img=paint.img
		cv2.imwrite(path, img)

paint=paintarq.Paint()
#ferramentas = ferramentas.Ferramentas()

paint.inicializacaoPainelDesenho()
root = Tk()

chamarPainel(paint.img)
painel.bind('<Button-1>', motion)
painel.bind('<B1-Motion>', motion2)
painel.bind('<B3-Motion>', borracha)
root.bind('<Key>',salvar)


cores.Cores(root)
ferramentas=ferramentasarq.Ferramentas(root)

root.mainloop()

