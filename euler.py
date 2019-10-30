#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def funceuler(primo):    ###funcion revisionprimos recibe un valor
  v_1=int(primo)##convierte la entrada en  un entero
  i=2 
  res=(i**(v_1-1)) %v_1 #aplica formula fermat
  print ("\n\tPhi = (",v_1,"- 1 )")
  print ("\tPhi = ",v_1-1)
  print("\n\tFormula Euler: 2^(Phi) Mod",v_1," = ",res)
  #print ("\n\tResultado Aplicando Fermat = ",res)###imprime el resultado
  if (res == 1):    #si el resultado es igual a 1 el numero es primo 
      print("\t\t -aplicando la formula de Euler tenemos que el numero \n\t\t  ingresado cumple la equivalencia a 1 Mod",v_1)
  else:    
      print("\t\t -no se encuentra equivalencia aplicando la formula de Euler")    

