# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 01:04:31 2021

@author: fantasma
"""
###vision artificial en deteccion de rostro 
from matplotlib import pyplot
from matplotlib.patches import Rectangle #para dibujar el mapeo en rectangulos 
from matplotlib.patches import Circle # para dibujar circulos
from mtcnn.mtcnn import MTCNN #importa librerias
import cv2

#inicio de rostri¿o

cap = cv2.VideoCapture (0)
while (True):
    ret,frame = cap.read()#lee el video
    cv2.imshow('Rostro', frame) #muestra el video en pantalla
    if cv2.waitKey(1) == 27: #escape para salir 
        break
    cv2.imwrite('rostro.jpg',frame) #guardamnos la captura del video como imagen
    cap.release() #cierra
    cv2.destroyAllWindows()
    
    ##CREAREMOS UNA FUNCION QUE NOS PERMITE DIBUJAR LOS RECTANGULOS Y CIRCULOS DE NUESTRA CARA
    #
    
    def dib(img, lista_resultados):
        print(caras)
        #lee la imagen de matplo
        imagen = pyplot.imread(img)
        #ploteamos las imagenes
        pyplot.imshow(imagen)
        ##ejes polares para calcar
        ax = pyplot.gca()
        #
        for result in lista_resultados:
            x, y, ancho, alto = result['box']
            #creamos el rec
            rect = Rectangle ((x,y), ancho, alto, fill = False, color = 'green')
            #dibuja la caja
            ax.add_patch(rect)
            #ahora rectangulos y nariz
            for puntos, value in result['keypoints'].items():
                #cramos circulos
                dot = Circle(value, radius=4, color = 'green')
                ax.add_patch(dot)
        # #a exportar los pixeles que perteneces a los rostros con el fin de usarlos en otro sistema
        # for i in range(len(lista_resultados)):
        #     #obtenemos resultados
        #     x1, y1, ancho1, alto1 = lista_resultados[i]['box']
        #     x2, y2 =  x1 + ancho1, y1 + alto1
        #     #definimos subplot
        #     pyplot.subplot(l, len(lista_resultados), i+1)
        #     pyplot.axis('off')
        #     #ploteamos las caras
        #     pyplot.imshow(imagen[y1:y2, x1:x2])
        #ploteamnos la imagen con el dibnujo
        
        pyplot.show()
        
        ##leemos la imagen 
        
    img = 'rostro.jpg'
    pixeles = pyplot.imread(img)
    
    #creanis ek dectir
    
detector =  MTCNN ()

caras = detector.detect_faces(pixeles)
dib(img, caras)
