#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración 
pantalones = 0 
total = 0
descuento = 0

#lectura de datos
pantalones = int( input("Ingrese la cantidad") )

#operaciones
if( pantalones < 5):
    print("No hay descuento")
    total = pantalones*200
    print("Total: ", total)

if( pantalones > 4 and pantalones < 12 ):
    print("Descuento del 15%")
    total = pantalones*200
    descuento = total*0.15 
    print("Total: ", total - descuento)
    
if( pantalones > 11):
    print("Descuento del 30%")
    total = pantalones*200
    descuento = total*0.30 
    print("Total: ", total - descuento)
    
    
    
    
    
    
    
    
    
    