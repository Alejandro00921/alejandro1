# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:15:49 2022

@author: USUARIO
"""

from clases.menu import Menu, MenuTecnicos
from clases.equipo import *

if __name__ == '__main__':
    menu = Menu("Escuela de ingenieria")
    op = menu.ver()
    if op == "1":
        menu2 = MenuTecnicos()
        op2 = menu2.ver()
        if op2 == "1":
            e = crearEquipo()
            e.verDatos()
        #elif op2 == "2":
        #    registroMantenimiento()

