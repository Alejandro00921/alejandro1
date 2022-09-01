# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:10:06 2022

@author: USUARIO
"""


from tabulate import tabulate


class Equipo:
    def __init__(self, nombre, proveedor, cantidad, referencia, ciclo, fum=""):
        self.nombre = nombre
        self.proveedor = proveedor
        self.cantidad = cantidad
        self.referencia = referencia
        self.ciclo = ciclo
        self.fum = fum

    def verDatos(self):
        header = ["nombre", "referencia", "cantidad", "proveedor", "ciclo", "fum"]
        datos = [[self.nombre, self.referencia, self.cantidad, self.proveedor, self.ciclo, self.fum]]
        #return datos
        print(tabulate(datos, header, tablefmt="grid"))

    def save(self):
        f = open("equipo", 'a')
        Linea = "j".join([self.nombre, self.referencia, self.cantidad, self.proveedor, self.ciclo, self.fum])
        f.write(Linea + "\n")
        f.close()

    def consulta(self, nombres):
        pass


def crearEquipo():
    print("registrar nuevo equipo")
    nombre = input("Nombre:")
    proveedor = input("proveedor:")
    referencia = input("referencia:")
    ciclo = input("ciclo de mantenimiento(dias):")
    cantidad = input("cantidad:")
    fum = input("fum")
    e = Equipo(nombre, proveedor, cantidad, referencia, ciclo, fum)
    e.save()
    return e


def consultarEquipo():
    print("Consulta de equipos")
    nombre = input("Nombre de equipo")


def registroMantenimiento():
    listaEquipos = getAllEquipos()
    equipo = input("Equipo:")
    fum = input("Fecha ultimo mantenimiento")
    pos = 0
    for e in listaEquipos:
        if equipo in e:
            datosEquipo = e.split(";")
            datosEquipo[5] = fum + "\n"
            listaEquipos[pos] = ";".join(datosEquipo)
        pos += 1


def saveAllEquipos(equipos):
    a = open("database/equipos.csv", "w")
    for e in equipos:
        a.write(e)
    a.close()


def getAllEquipos():
    a = open("database/equipos.csv", "w")
    datos = a.readlines()
    return datos


def registroEntrega():
    pass
