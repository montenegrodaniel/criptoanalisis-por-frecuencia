#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

def ayudaPrincipal():
	print(format("",'-^87'))
	print ("|                                                                                     |")
	print ("|",format("ALGORITMOS CRIPTOGRAFICOS",'^83'),"|")
	print ("|										      |")
	print ("| sintaxis: python3 proyecto.py <algoritmo>					      |")
	print ("|										      |")
	print ("| <algoritmo>:									      |")
	print ("|\t-ces   Algoritmo de cifrado cesar                                             |")	
	print ("|\t-fre   Algoritmo de criptoanálisis por Frecuencia                             |")
	print ("|\t-tof   Pequeño teorema de fermat                                              |")
	print ("|\t-ale   Teorema de euler                                                       |")
	print ("|\t-cre   Criba de erathostenes                                                  |")
	print ("|\t-teu   Algoritmo extendido de euclides                                        |")
	print ("|										      |")
	print ("| consultar ayuda de un algoritmo en específico : 				      |")
	print ("|                                   sintaxis: python3 proyecto.py <algoritmo>	      |")
	print ("| 										      |")
	print ("| Ejemplo:									      |")
	print ("|		python3 proyecto.py -ces					      |")
	print ("|_____________________________________________________________________________________|")
	print ("| Actualización de version, sustituyendo algunos algoritmos criptograficos            |")
	print ("| Elaborado por: Daniel C. Montenegro (montenegrodaniel0@gmail.com)                   |")
	print ("| 		 Fabian D. Guzman     (fabianguzman0220@hotmail.com)                  |")
	print ("| Materia:	 Certificados y Firmas Digitales                              	      |")
	print ("| Docente:       Siler Amador Donado (samador@unicauca.edu.co)                        |")
	print ("|         									      |")
	print ("| Creditos y agradecimientos a los desarrolladores:                                   |")
	print ("| Tania Cañizares (ctania@unicauca.edu.co);Jonathan Ibarra (estivenp@unicauca.edu.co) |")
	print ("| *repositorio: https://github.com/TaniaCanizares/Criptografia			      |")
	print ("|      										      |")
	print ("|",format("UNIVERSIDAD AUTONOMA DE OCCIDENTE",'^83'),"|")
	print ("|",format("OCTUBRE 2019",'^83'),"|")
	print (" --------------------------------------------------------------------------------------")

def ayudaFrecuencia():
	print (" ------------------------------------------------------------------------------------------")
	print ("|                                                                                         |")
	print ("|",format("CRIPTOANÁLISIS POR FRECUENCIA",'^87'),"|")
	print ("|									                  |")
	print ("| sintaxis: python3 proyecto.py -fre <archivoCifrado>                                     |")
	print ("|			  				 		 	          |")
	print ("| <archivoCifrado>: Nombre del archivo de entrada que desea descifrar ej: quijote.cif     |")
	print ("|										          |")
	print ("| Ejemplo:    					 				          |")
	print ("|										          |")
	print ("| Los archivos de prueba los puedes encontrar en:            		                  |")
	print ("| http://seguridad.unicauca.edu.co/criptografia/MobyDick.txt           		          |")
	print ("| http://seguridad.unicauca.edu.co/criptografia/quijote.txt            	                  |")
	print ("|										          |")
	print ("| Ejemplo: decifrar archivo de  extenson .cif  					          |")
	print ("|								            	          |")
	print ("|          descifrar: python3 proyecto.py -fre quijote.cif                                |")
	print ("|         									          |")
	print ("|Ayuda con el alfabeto:                                                                   |")
	print ("|        									          |")
	print ("|\tPara agregar o borrar caracteres en el alfabeto digitar el comando:	          |")
	print ("|         									          |")
	print ("|\tnano <Nombre de archivo> y digitar el caracter en su posicion                     |")
	print ("|\tPara guardar los cambios presionar  teclas Ctrl + O y luego tecla ENTER           |")
	print ("|         									          |")
	print ("|_________________________________________________________________________________________|")
	print ("| Actualización de version, sustituyendo algunos algoritmos criptograficos                |")
	print ("| Elaborado por: Daniel C. Montenegro (montenegrodaniel0@gmail.com)                       |")
	print ("| 		 Fabian D. Guzman     (fabianguzman0220@hotmail.com)                      |")
	print ("| Materia:	 Certificados y Firmas Digitales                              	          |")
	print ("| Docente:       Siler Amador Donado (samador@unicauca.edu.co)                            |")
	print ("|         									          |")
	print ("| Creditos y agradecimientos a los desarrolladores:                                       |")
	print ("| Tania Cañizares (ctania@unicauca.edu.co);Jonathan Ibarra (estivenp@unicauca.edu.co)     |")
	print ("| *repositorio: https://github.com/TaniaCanizares/Criptografia			          |")
	print ("|      										          |")
	print ("|",format("UNIVERSIDAD AUTONOMA DE OCCIDENTE",'^87'),"|")
	print ("|",format("OCTUBRE 2019",'^87'),"|")
	print (" ------------------------------------------------------------------------------------------")

def ayudaeuclides():
	print ("-----------------------------------------------------------------------------------------------------")
	print ("|                                                                                                   |")
	print ("|",format("ALGORITMO EXTENDIDO DE EUCLIDES",'^97'),"|")
	print ("|                                                                                                   |")
	print ("| sintaxis: python3 proyecto.py -teu <Numero_1> <Numero_2>                                          |")
	print ("|                                                                                                   |")
	print ("| <modo>:   valor de numeros para calcular el M.C.D                                                 |")
        #print ("|                                                     |")
	print ("|\tNumero_1 :   valor numero 1                                                                 |")
	print ("|\tNumero_2 :   Valor numero 2    	  			         			    |")
	print ("|                                                     						    |")
	print ("| Ejemplo:									      		    |")
	print ("|		python3 proyecto.py -teu 4434 5675      			      		    |")
	print ("|___________________________________________________________________________________________________|")
	print ("| Actualización de version, sustituyendo algunos algoritmos criptograficos                          |")
	print ("| Elaborado por: Daniel C. Montenegro (montenegrodaniel0@gmail.com)                                 |")
	print ("| 		 Fabian D. Guzman     (fabianguzman0220@hotmail.com)                                |")
	print ("| Materia:	 Certificados y Firmas Digitales                              	                    |")
	print ("| Docente:       Siler Amador Donado (samador@unicauca.edu.co)                                      |")
	print ("|         									                    |")
	print ("| Creditos y agradecimientos a los desarrolladores:                                                 |")
	print ("| Tania Cañizares (ctania@unicauca.edu.co);Jonathan Ibarra (estivenp@unicauca.edu.co)               |")
	print ("| *repositorio: https://github.com/TaniaCanizares/Criptografia			                    |")
	print ("|      										                    |")
	print ("|",format("UNIVERSIDAD AUTONOMA DE OCCIDENTE",'^97'),"|")
	print ("|",format("OCTUBRE 2019",'^97'),"|")
	print (" ----------------------------------------------------------------------------------------------------")

	
def ayudacriba():
	print ("-----------------------------------------------------------------------------------------------------")
	print ("|                                                                                                   |")
	print ("|",format("ALGORITMO CRIBA DE ERATOSTHENES",'^97'),"|")
	print ("|	           								                    |")
	print ("| sintaxis: python3 proyecto.py -cre <Valor_num>                                                    |")
	print ("|								   		                    |")
	print ("| nota: el script  toma como numero inferior 2 para empezar a cribar  		                    |")
	print ("| <modo>:       ingresar numero de rango superior para cribar                                       |")
	print ("|\tValor_num :    valor final a cribar                                                         |")
	print ("| 										     		    |")
	print ("|                                                     						    |")
	print ("| Ejemplo:									      		    |")
	print ("|		python3 proyecto.py -cre 675  		      			      		    |")
	print ("|___________________________________________________________________________________________________|")
	print ("| Actualización de version, sustituyendo algunos algoritmos criptograficos                          |")
	print ("| Elaborado por: Daniel C. Montenegro (montenegrodaniel0@gmail.com)                                 |")
	print ("| 		 Fabian D. Guzman     (fabianguzman0220@hotmail.com)                                |")
	print ("| Materia:	 Certificados y Firmas Digitales                              	                    |")
	print ("| Docente:       Siler Amador Donado (samador@unicauca.edu.co)                                      |")
	print ("|         									                    |")
	print ("| Creditos y agradecimientos a los desarrolladores:                                                 |")
	print ("| Tania Cañizares (ctania@unicauca.edu.co);Jonathan Ibarra (estivenp@unicauca.edu.co)               |")
	print ("| *repositorio: https://github.com/TaniaCanizares/Criptografia			                    |")
	print ("|      										                    |")
	print ("|",format("UNIVERSIDAD AUTONOMA DE OCCIDENTE",'^97'),"|")
	print ("|",format("OCTUBRE 2019",'^97'),"|")
	print (" ----------------------------------------------------------------------------------------------------")
def ayudafermat():
	print ("-----------------------------------------------------------------------------------------------------")
	print ("|                                                                                                   |")
	print ("|",format("TEOREMA DE FERMAT",'^97'),"|")
	print ("|	           								                    |")
	print ("| Importante: antes de utilizar esta funcion tener claro la primalidad del numero a ingresar,	    |")
	print ("|	      si necesita ayuda, usar algoritmo criba de eratosthenes         			    |")
	print ("|	           								                    |")
	print ("|	           								                    |")
	print ("| sintaxis: python3 proyecto.py -tof <numero>                                                       |")
	print ("|								   		                    |")
	print ("|formula fermat: (a^(<numero> - 1)Mod<numero>) Equivalente 1 mod <numero>  || utilizando a = 2      |")
	print ("| <modo>:       ingresar numero primo 					                            |")
	print ("|\tnumero :     valor entero del numero                                                        |")
	#print ("|\tnum_superior :    numero superior                                                           |")
	print ("| 										     		    |")
	print ("|                                                     						    |")
	print ("| Ejemplo:									      		    |")
	print ("|		python3 proyecto.py -tof 52543      				      		    |")
	print ("|___________________________________________________________________________________________________|")
	print ("| Actualización de version, sustituyendo algunos algoritmos criptograficos                          |")
	print ("| Elaborado por: Daniel C. Montenegro (montenegrodaniel0@gmail.com)                                 |")
	print ("| 		 Fabian D. Guzman     (fabianguzman0220@hotmail.com)                                |")
	print ("| Materia:	 Certificados y Firmas Digitales                              	                    |")
	print ("| Docente:       Siler Amador Donado (samador@unicauca.edu.co)                                      |")
	print ("|         									                    |")
	print ("| Creditos y agradecimientos a los desarrolladores:                                                 |")
	print ("| Tania Cañizares (ctania@unicauca.edu.co);Jonathan Ibarra (estivenp@unicauca.edu.co)               |")
	print ("| *repositorio: https://github.com/TaniaCanizares/Criptografia			                    |")
	print ("|      										                    |")
	print ("|",format("UNIVERSIDAD AUTONOMA DE OCCIDENTE",'^97'),"|")
	print ("|",format("OCTUBRE 2019",'^97'),"|")
	print (" ----------------------------------------------------------------------------------------------------")

def ayudaeuler():
	print ("-----------------------------------------------------------------------------------------------------")
	print ("|                                                                                                   |")
	print ("|",format("ALGORITMO DE EULER",'^97'),"|")
	print ("|	           								                    |")
	print ("|	           								                    |")
	print ("| Importante: antes de utilizar esta funcion tener claro la primalidad del numero a ingresar,	    |")
	print ("|	      si necesita ayuda, usar algoritmo criba de eratosthenes         			    |")
	print ("|	           								                    |")
	print ("|	           								                    |")
	print ("| sintaxis: python3 proyecto.py -ale <numero>                                                       |")
	print ("|								   		                    |")
	print ("|               Phi= (<numero> - 1)				   		                    |")
	print ("|formula Euler: (a^(Phi)Mod<numero>) Equivalente 1 mod <numero>  || utilizando a = 2                |")
	print ("|								   		                    |")
	print ("| <modo>:       ingresar numero para comprobar test de equivalencia                                 |")
	print ("|\tnumero :    valor entero del numero                                                         |")
	#print ("|\tnum_superior :    numero superior                                                           |")
	print ("| 										     		    |")
	print ("|                                                     						    |")
	print ("| Ejemplo:									      		    |")
	print ("|		python3 proyecto.py -ale 4565      	 			      		    |")
	print ("|___________________________________________________________________________________________________|")
	print ("| Actualización de version, sustituyendo algunos algoritmos criptograficos                          |")
	print ("| Elaborado por: Daniel C. Montenegro (montenegrodaniel0@gmail.com)                                 |")
	print ("| 		 Fabian D. Guzman     (fabianguzman0220@hotmail.com)                                |")
	print ("| Materia:	 Certificados y Firmas Digitales                              	                    |")
	print ("| Docente:       Siler Amador Donado (samador@unicauca.edu.co)                                      |")
	print ("|         									                    |")
	print ("| Creditos y agradecimientos a los desarrolladores:                                                 |")
	print ("| Tania Cañizares (ctania@unicauca.edu.co);Jonathan Ibarra (estivenp@unicauca.edu.co)               |")
	print ("| *repositorio: https://github.com/TaniaCanizares/Criptografia			                    |")
	print ("|      										                    |")
	print ("|",format("UNIVERSIDAD AUTONOMA DE OCCIDENTE",'^97'),"|")
	print ("|",format("OCTUBRE 2019",'^97'),"|")
	print (" ----------------------------------------------------------------------------------------------------")
def ayudacesar():
	print (" -------------------------------------------------------------------------------------")
	print ("|                                                                                     |")
	print ("| ",format("ALGORITMO DE JULIO CESAR",'^97'),"|")
	print ("|										      |")
	print ("| sintaxis: python3 proyecto.py -ces <modo> <archivoEntrada> <clave>                  |")
	print ("|										      |")
	print ("| <modo>:									      |")
	print ("|\t-c    para cifrar el archivo			             		      |")
	print ("|\t-d    para decifrar el archivo                  			      |")
	print ("| 										      |")
	print ("| <archivoEntrada>: Ruta y Nombre del archivo de entrada a cifrar o descifrar          ")
	print ("| <clave>: Numero con el que desea cifrar o descifrar                                 |")
	print ("|										      |")
	print ("|         									      |")
	print ("| 										      |")
	print ("| Ejemplo:									      |")
	print ("|		python3 proyecto.py -ces libros/quijote.txt 6			      |")
	print ("|_____________________________________________________________________________________|")
	print ("| Actualización de version, sustituyendo algunos algoritmos criptograficos            |")
	print ("| Elaborado por: Daniel C. Montenegro (montenegrodaniel0@gmail.com)                   |")
	print ("| 		 Fabian D. Guzman     (fabianguzman0220@hotmail.com)                  |")
	print ("| Materia:	 Certificados y Firmas Digitales                              	      |")
	print ("| Docente:       Siler Amador Donado (samador@unicauca.edu.co)                        |")
	print ("|         									      |")
	print ("| Creditos y agradecimientos a los desarrolladores:                                   |")
	print ("| Tania Cañizares (ctania@unicauca.edu.co);Jonathan Ibarra (estivenp@unicauca.edu.co) |")
	print ("| *repositorio: https://github.com/TaniaCanizares/Criptografia			      |")
	print ("|      										      |")
	print ("|",format("UNIVERSIDAD AUTONOMA DE OCCIDENTE",'^83'),"|")
	print ("|",format("OCTUBRE 2019",'^83'),"|")
	print (" --------------------------------------------------------------------------------------")



