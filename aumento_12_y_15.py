#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración 
sueldo = 0 
aumento = 0

#lectura de datos
sueldo = int( input("Ingrese el sueldo") )

#operaciones
if(sueldo < 5000):
    aumento = sueldo * 15 / 100
    print("Aplica aumento del 15%")
    print("Nuevo sueldo: ",sueldo+aumento)
else:
    aumento = sueldo * 12 / 100
    print("Aplica aumento del 12%")
    print("Nuevo sueldo: ",sueldo+aumento)


    
    
    
    
    
    