#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL

Tema: Proyecto Final - Usando Agentes Inteligentes
Profesor: Dr. Asdrúbal López Chau
Descripción: plicacion de Agentes Inteligentes Para la Convinación correcta de
colores para generar pinturas con colores secundarios
    
Created on Tue Nov 23 22:35:30 2021

@author: rogelioortegabarrera
"""

ACCIONES = {'Moneda': 'Ingresa el Color',
            'Magenta': 'Realiza Mezcla Magenta',
            'Amarillo': 'Realiza Mezcla Amarillo',
            'Azul': 'Realiza Mezcla Azul',
            'Magenta, Amarillo': 'Realiza Mezcla Naranja',
            'Magenta, Azul': 'Realiza Mezcla Violeta',
            'Magenta, Naranja': 'Realiza Mezcla Rojo-anaranjado',
            'Magenta, Violeta': 'Realiza Mezcla Violeta-rojizo',
            'Amarillo, Naranja': 'Realiza Mezcla Amarillo-anaranjado',
            'Amarillo, Verde': 'Realiza Mezcla Amarillo-verdoso',
            'Azul, Amarillo': 'Realiza Mezcla Verde',
            'Azul, Verde': 'Realizar Mezcla Azul-verdoso', 
            'Azul, Violeta': 'Realizar Mezcla Violeta-azulado'
            }
# %%
class AgenteTabla:
    #Agente Inteligente de Tipo Tabla
    
    def __init__(self, acciones):
        self.acciones = acciones
        self.percepciones = ""
        
    def actuar(self, percepcion, accion_basica=''):
    #Actua segun la percepcion, devolviendo una accion
        if not percepcion:
            return accion_basica
        if len(self.percepciones) != 0:
            self.percepciones += ','
        self.percepciones += percepcion
        if self.percepciones in self.acciones.keys():
            return self.acciones[self.percepciones]
        self.percepciones = ''
        return accion_basica

# %%
print("- - Maquina Mezcladora de Pinturas - -")
mexcladora = AgenteTabla(ACCIONES)
percepcion = input("Ingresa una moneda: ")
while percepcion:
    accion = mexcladora.actuar(percepcion, 'Color No Encontrado')
    print(accion)
    percepcion = input("Indicar Conbinacion: ")