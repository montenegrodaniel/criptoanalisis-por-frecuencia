#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def revisionprimos(primo):    ###funcion revisionprimos recibe un valor
  v_1=int(primo)##convierte la entrada en  un entero
  i=2 
  res=(i**(v_1-1)) %v_1 #aplica formula fermat
  print("\n\t2^(",v_1,"- 1)","Mod",v_1," = ",res)
  #print ("\n\tResultado Aplicando Fermat = ",res)###imprime el resultado
  if (res == 1):    #si el resultado es igual a 1 el numero es primo 
      print("\t\t -aplicando la formula de fermat tenemos que el numero ingresado\n\t\t  cumple la equivalencia a 1 Mod",v_1)
  else:    
      print("\t\t -el numero ingresado no es primo, y no se encuentra equivalencia\n\t\t  aplicando la formula de fermat")    

