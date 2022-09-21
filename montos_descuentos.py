#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración  
total = 0
descuento = 0

#lectura de datos
total = int( input("Ingrese el monto: \n") )

#operaciones
if(total < 500):
    print("No hay descuento")
    
if(total > 499 and total <1000):
    print("Descuento del 5%")
    descuento = total * 0.05
    print("Total a pagar: ",total-descuento)    
    
if(total > 999 and total <7000):
    print("Descuento del 11%")
    descuento = total * 0.11
    print("Total a pagar: ",total-descuento)  
    
if(total > 6999 and total <15000):
    print("Descuento del 18%")
    descuento = total * 0.18
    print("Total a pagar: ",total-descuento)    
    
if(total > 14999):
    print("Descuento del 25%")
    descuento = total * 0.25
    print("Total a pagar: ",total-descuento)  
    
    
    
    