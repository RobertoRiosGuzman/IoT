from flask import Flask
from flask_ask import Ask, statement
import RPi.GPIO as GPIO
import threading
import time
 
app = Flask(__name__)
ask = Ask(app, '/')

posicion1r = False
posicion2r = False
posicion3r = False
posicion4r = False
posicion5r = False
posicion6r = False
posicion7r = False
posicion8r = False
posicion9r = False

posicion1v = False
posicion2v = False
posicion3v = False
posicion4v = False
posicion5v = False
posicion6v = False
posicion7v = False
posicion8v = False
posicion9v = False
 
@ask.intent('LedIntent')
def led(color, posicion):
	
	global posicion1r
	global posicion2r
	global posicion3r
	global posicion4r
	global posicion5r
	global posicion6r
	global posicion7r
	global posicion8r
	global posicion9r
	
	global posicion1v
	global posicion2v
	global posicion3v
	global posicion4v
	global posicion5v
	global posicion6v
	global posicion7v
	global posicion8v
	global posicion9v
	
	if color not in pins.values():
		return statement("No tengo el led de color {}".format(color))
	else:
		if color == 'rojo':
			
			if posicion == '1':
				if not posicion1r and not posicion1v:
					GPIO.output(17, GPIO.LOW)
					posicion1r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '2':
				if not posicion2r and not posicion2v:
					GPIO.output(27, GPIO.LOW)
					posicion2r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '3':
				if not posicion3r and not posicion3v:
					GPIO.output(22, GPIO.LOW)
					posicion3r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '4':
				if not posicion4r and not posicion4v:
					GPIO.output(10, GPIO.LOW)
					posicion4r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '5':
				if not posicion5r and not posicion5v:
					GPIO.output(9, GPIO.LOW)
					posicion5r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '6':
				if not posicion6r and not posicion6v:
					GPIO.output(5, GPIO.LOW)
					posicion6r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '7':
				if not posicion7r and not posicion7v:
					GPIO.output(6, GPIO.LOW)
					posicion7r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '8':
				if not posicion8r and not posicion8v:
					GPIO.output(13, GPIO.LOW)
					posicion8r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '9':
				if not posicion9r and not posicion9v:
					GPIO.output(19, GPIO.LOW)
					posicion9r = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			else:
				return statement('La posicion {} no existe. Elija una entre uno y nueve'.format(posicion))

		if color == 'verde':
			if posicion == '1':
				if not posicion1v and not posicion1r:
					GPIO.output(26, GPIO.LOW)
					posicion1v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '2':
				if not posicion2v and not posicion2r:
					GPIO.output(18, GPIO.LOW)
					posicion2v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '3':
				if not posicion3v and not posicion3r:
					GPIO.output(23, GPIO.LOW)
					posicion3v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '4':
				if not posicion4v and not posicion4r:
					GPIO.output(24, GPIO.LOW)
					posicion4v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '5':
				if not posicion5v and not posicion5r:
					GPIO.output(25, GPIO.LOW)
					posicion5v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '6':
				if not posicion6v and not posicion6r:
					GPIO.output(12, GPIO.LOW)
					posicion6v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '7':
				if not posicion7v and not posicion7r:
					GPIO.output(16, GPIO.LOW)
					posicion7v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '8':
				if not posicion8v and not posicion8r:
					GPIO.output(20, GPIO.LOW)
					posicion8v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			elif posicion == '9':
				if not posicion9v and not posicion9r:
					GPIO.output(21, GPIO.LOW)
					posicion9v = True
					return statement('Encendiendo el led {}'.format(posicion))
				else:
					return statement('El led de la posicion {} está encendido, elija otra'.format(posicion))
			else:
				return statement('La posicion {} no existe. Elija otra entre uno y nueve'.format(posicion))
			
	
def ganLinea1():
	global posicion1r
	global posicion2r
	global posicion3r
	
	global posicion1v
	global posicion2v
	global posicion3v
	
	while True:
		time.sleep(8)
		if posicion1r and posicion2r and posicion3r:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(17, GPIO.HIGH)
				GPIO.output(27, GPIO.HIGH)
				GPIO.output(22, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(17, GPIO.LOW)
				GPIO.output(27, GPIO.LOW)
				GPIO.output(22, GPIO.LOW)
				i = i + 1
			finJuego()
			break
		if posicion1v and posicion2v and posicion3v:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(26, GPIO.HIGH)
				GPIO.output(18, GPIO.HIGH)
				GPIO.output(23, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(26, GPIO.LOW)
				GPIO.output(18, GPIO.LOW)
				GPIO.output(23, GPIO.LOW)
				i = i + 1
			finJuego()
			break

def ganLinea2():
	global posicion4r
	global posicion5r
	global posicion6r
	
	global posicion4v
	global posicion5v
	global posicion6v
	
	while True:
		time.sleep(8)
		if posicion4r and posicion5r and posicion6r:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(10, GPIO.HIGH)
				GPIO.output(9, GPIO.HIGH)
				GPIO.output(5, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(10, GPIO.LOW)
				GPIO.output(9, GPIO.LOW)
				GPIO.output(5, GPIO.LOW)
				i = i + 1
			finJuego()
			break
		if posicion4v and posicion5v and posicion6v:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(24, GPIO.HIGH)
				GPIO.output(25, GPIO.HIGH)
				GPIO.output(12, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(24, GPIO.LOW)
				GPIO.output(25, GPIO.LOW)
				GPIO.output(12, GPIO.LOW)
				i = i + 1
			finJuego()
			break
			
def ganLinea3():
	global posicion7r
	global posicion8r
	global posicion9r
	
	global posicion7v
	global posicion8v
	global posicion9v
	
	while True:	
		time.sleep(8)
		if posicion7r and posicion8r and posicion9r:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(6, GPIO.HIGH)
				GPIO.output(13, GPIO.HIGH)
				GPIO.output(19, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(6, GPIO.LOW)
				GPIO.output(13, GPIO.LOW)
				GPIO.output(19, GPIO.LOW)
				i = i + 1
			finJuego()
			break
		if posicion7v and posicion8v and posicion9v:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(16, GPIO.HIGH)
				GPIO.output(20, GPIO.HIGH)
				GPIO.output(21, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(16, GPIO.LOW)
				GPIO.output(20, GPIO.LOW)
				GPIO.output(21, GPIO.LOW)
				i = i + 1
			finJuego()
			break

def ganLinea4():
	global posicion1r
	global posicion4r
	global posicion7r
	
	global posicion1v
	global posicion4v
	global posicion7v
	
	while True:
		time.sleep(8)
		if posicion1r and posicion4r and posicion7r:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(17, GPIO.HIGH)
				GPIO.output(10, GPIO.HIGH)
				GPIO.output(6, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(17, GPIO.LOW)
				GPIO.output(10, GPIO.LOW)
				GPIO.output(6, GPIO.LOW)
				i = i + 1
			finJuego()
			break
		if posicion1v and posicion4v and posicion7v:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(26, GPIO.HIGH)
				GPIO.output(24, GPIO.HIGH)
				GPIO.output(16, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(26, GPIO.LOW)
				GPIO.output(24, GPIO.LOW)
				GPIO.output(16, GPIO.LOW)
				i = i + 1
			finJuego()
			break

def ganLinea5():
	global posicion2r
	global posicion5r
	global posicion8r
	
	global posicion2v
	global posicion5v
	global posicion8v
	
	while True:
		time.sleep(8)
		if posicion2r and posicion5r and posicion8r:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(27, GPIO.HIGH)
				GPIO.output(9, GPIO.HIGH)
				GPIO.output(13, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(27, GPIO.LOW)
				GPIO.output(9, GPIO.LOW)
				GPIO.output(13, GPIO.LOW)
				i = i + 1
			finJuego()
			break
		if posicion2v and posicion5v and posicion8v:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(18, GPIO.HIGH)
				GPIO.output(25, GPIO.HIGH)
				GPIO.output(20, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(18, GPIO.LOW)
				GPIO.output(25, GPIO.LOW)
				GPIO.output(20, GPIO.LOW)
				i = i + 1
			finJuego()
			break

def ganLinea6():
	global posicion3r
	global posicion6r
	global posicion9r
	
	global posicion3v
	global posicion6v
	global posicion9v
	
	while True:
		time.sleep(8)
		if posicion3r and posicion6r and posicion9r:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(22, GPIO.HIGH)
				GPIO.output(5, GPIO.HIGH)
				GPIO.output(19, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(22, GPIO.LOW)
				GPIO.output(5, GPIO.LOW)
				GPIO.output(19, GPIO.LOW)
				i = i + 1
			finJuego()
			break
		if posicion3v and posicion6v and posicion9v:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(23, GPIO.HIGH)
				GPIO.output(12, GPIO.HIGH)
				GPIO.output(21, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(23, GPIO.LOW)
				GPIO.output(12, GPIO.LOW)
				GPIO.output(21, GPIO.LOW)
				i = i + 1
			finJuego()
			break

def ganLinea7():
	global posicion1r
	global posicion5r
	global posicion9r
	
	global posicion1v
	global posicion5v
	global posicion9v
	
	while True:
		time.sleep(8)
		if posicion1r and posicion5r and posicion9r:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(17, GPIO.HIGH)
				GPIO.output(9, GPIO.HIGH)
				GPIO.output(19, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(17, GPIO.LOW)
				GPIO.output(9, GPIO.LOW)
				GPIO.output(19, GPIO.LOW)
				i = i + 1
			finJuego()
			break
		if posicion1v and posicion5v and posicion9v:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(26, GPIO.HIGH)
				GPIO.output(25, GPIO.HIGH)
				GPIO.output(21, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(26, GPIO.LOW)
				GPIO.output(25, GPIO.LOW)
				GPIO.output(21, GPIO.LOW)
				i = i + 1
			finJuego()
			break
			
def ganLinea8():
	global posicion7r
	global posicion5r
	global posicion3r
	
	global posicion7v
	global posicion5v
	global posicion3v
	
	while True:
		time.sleep(8)
		if posicion7r and posicion5r and posicion3r:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(6, GPIO.HIGH)
				GPIO.output(9, GPIO.HIGH)
				GPIO.output(22, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(6, GPIO.LOW)
				GPIO.output(9, GPIO.LOW)
				GPIO.output(22, GPIO.LOW)
				i = i + 1
			finJuego()
			break
		if posicion7v and posicion5v and posicion3v:
			i = 0
			while i<5:
				time.sleep(1)
				GPIO.output(16, GPIO.HIGH)
				GPIO.output(25, GPIO.HIGH)
				GPIO.output(23, GPIO.HIGH)
				time.sleep(1)
				GPIO.output(16, GPIO.LOW)
				GPIO.output(25, GPIO.LOW)
				GPIO.output(23, GPIO.LOW)
				i = i + 1
			finJuego()
			break

def finJuego():
	GPIO.output(17, GPIO.HIGH)
	GPIO.output(27, GPIO.HIGH)
	GPIO.output(22, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH) 
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(13, GPIO.HIGH)
	GPIO.output(19, GPIO.HIGH)
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(25, GPIO.HIGH)
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(20, GPIO.HIGH)
	GPIO.output(21, GPIO.HIGH)
	
	global posicion1r
	global posicion2r
	global posicion3r
	global posicion4r
	global posicion5r
	global posicion6r
	global posicion7r
	global posicion8r
	global posicion9r
	
	global posicion1v
	global posicion2v
	global posicion3v
	global posicion4v
	global posicion5v
	global posicion6v
	global posicion7v
	global posicion8v
	global posicion9v
	
	posicion1r = False
	posicion2r = False
	posicion3r = False
	posicion4r = False
	posicion5r = False
	posicion6r = False
	posicion7r = False
	posicion8r = False
	posicion9r = False

	posicion1v = False
	posicion2v = False
	posicion3v = False
	posicion4v = False
	posicion5v = False
	posicion6v = False
	posicion7v = False
	posicion8v = False
	posicion9v = False
	
	
 
if __name__ == '__main__':
	try:
		GPIO.setmode(GPIO.BCM)
		pins = {
				17:'rojo',
				27:'rojo',
				22:'rojo',
				10:'rojo',
				9:'rojo',
				5:'rojo',
				6:'rojo',
				13:'rojo',
				19:'rojo',
				26:'verde',
				18:'verde',
				23:'verde',
				24:'verde',
				25:'verde',
				12:'verde',
				16:'verde',
				20:'verde',
				21:'verde'
		}
		for pin in pins.keys(): 
			GPIO.setup(pin, GPIO.OUT)
		finJuego()
		t1=threading.Thread(target=ganLinea1)
		t1.start()
		t2=threading.Thread(target=ganLinea2)
		t2.start()
		t3=threading.Thread(target=ganLinea3)
		t3.start()
		t4=threading.Thread(target=ganLinea4)
		t4.start()
		t5=threading.Thread(target=ganLinea5)
		t5.start()
		t6=threading.Thread(target=ganLinea6)
		t6.start()
		t7=threading.Thread(target=ganLinea7)
		t7.start()
		t8=threading.Thread(target=ganLinea8)
		t8.start()
		app.run(debug=True)
	finally:
		GPIO.cleanup()
