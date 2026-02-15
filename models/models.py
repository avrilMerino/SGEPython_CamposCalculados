# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

class horoscopo(models.Model):
    #heredamos este modelo res.parther
    _inherit ='res.parther'

    #añadimos tres campos
    #la edad NO SE ALMACENA EN LA BASE DE DATOS
    cumple = fields.Date("Fecha de nacimiento")
    edad = fields.Integer(string="Edad", readonly=True, compute="_calcula_edad", store=True)
    signo = fields.Char(string="Signo zodiaco", readonly=True, compute="_calcula_signo", store=True)

    #los metodos
    #puede que nos llegue mas de un registro por eso esta definido el bucle for
    #si cambia el atributo cumple
    @api.depends("cumple")
    def _calcula_edad(self):
            for registro in self:
                #si existe cumple le asigno 99 sino lo dejo a nulo
                if registro.cumple: 
                    #inserta aqui el codigo para calcular la edad
                    hoyAno = date.today().year
                    hoyMes = date.today().month
                    hoyDia = date.today().day

                    regAno = registro.cumple.year
                    regMes = registro.cumple.month
                    regDia = registro.cumple.day

                    edadProv = hoyAno - regAno

                    if hoyMes < regMes:
                        edadProv = edadProv - 1
                    if hoyMes == regMes and hoyDia < regDia:
                         edadProv = edadProv - 1

                    edad = edadProv
                    registro.edad = edad
                else:
                    registro.edad = 0

    #si cambia el atributo cumple
    @api.depends("cumple")
    def _calula_signo(self):
        for registro in self:
            if not registro.cumple:
                registro.signo = False
                continue

            mes = registro.cumple.month
            dia = registro.cumple.day

            if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
                registro.signo = "Capricornio"
            elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
                registro.signo = "Acuario"
            elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
                registro.signo = "Piscis"
            elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
                registro.signo = "Aries"
            elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
                registro.signo = "Tauro"
            elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
                registro.signo = "Géminis"
            elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
                registro.signo = "Cáncer"
            elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
                registro.signo = "Leo"
            elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
                registro.signo = "Virgo"
            elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
                registro.signo = "Libra"
            elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
                registro.signo = "Escorpio"
            elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
                registro.signo = "Sagitario"
        
