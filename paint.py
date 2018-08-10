import cv2
import numpy as np
import cores
import salvar
import ferramentas

drawing = False 	# true if mouse is pressed
ix,iy = -1,-1
color=(0,0,0)
colorTracker =(0,0,0)
tamanho_ponteiro=5

class Paint:
	"""docstring for Paint"""
	img=0
	

	def __init__(self):
		self.tamanho_ponteiro=2
		
	def nothing(x):
		pass

	def configColor():
		global ix,iy,drawing,mode, color, colorTracker, tamanho_ponteiro
		cv2.imshow('color',colorTracker)
		r = cv2.getTrackbarPos('R', 'color')
		g = cv2.getTrackbarPos('G', 'color')
		b = cv2.getTrackbarPos('B', 'color')
		tamanho_ponteiro= cv2.getTrackbarPos('tamanho do pincel\n', 'color')
		color=(b,g,r)
		colorTracker[:]=(b,g,r)

	def desenhar(self,x,y,tamanho_ponteiro):
		color=cores.color
		#tamanho_ponteiro=Ferramentas.tamanho_ponteiro
		cv2.circle(self.img,(x,y), tamanho_ponteiro, color,-1)
		return self.img


	def desenhar2(self,x,y, x2,y2,tamanho_ponteiro):
		color=cores.color
		#tamanho_ponteiro=Ferramentas.tamanho_ponteiro
		cv2.line(self.img,(x,y),(x2,y2), color ,tamanho_ponteiro)
		return self.img

	def apagar(x,y):
		global img
		cv2.circle(img,(x,y), tamanho_ponteiro, (255,255,255), -1)
		return img


	#inicializa um painel em branco
	def inicializacaoPainelDesenho(self):
		self.img =np.ones( (512,512,3), np.uint8 )*255
		

