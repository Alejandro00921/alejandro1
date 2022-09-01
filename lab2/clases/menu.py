# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:09:22 2022

@author: USUARIO
"""


class Menu:
    def __init__(self, laboratorio):
        self.laboratorio = laboratorio

    def ver(self):
        print("Bienvenido al sistema".center(20, "*"))
        print("laboratorio:" + self.laboratorio)
        print("1.tecnicos")
        print("2.estudiantes")
        op = input(">>>")

        return op


class MenuTecnicos:
    def ver(self):
        print("Menu Tecnicos".center(20, "*"))
        print("1.Registrar equipos")
        print("2.Registrar clase")
        op = input(">>>")
        return op




if __name__ == '__main__':
    m = Menu("xxxx")
    m.ver()
