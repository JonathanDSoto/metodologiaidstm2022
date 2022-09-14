#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 07:04:32 2022

@author: jonathansoto
"""

#declaración 
num1 = 0
num2 = 0 

#lectura de datos  

num1 = int( input("Ingrese el num 1 \n") )
num2 = int( input("Ingrese el num 2 \n") )

#operaciones
if( num1 < num2 ):
    print("El ", num1, " es menor")
    
if( num2 < num1 ):
    print("El ", num2, " es menor")    
