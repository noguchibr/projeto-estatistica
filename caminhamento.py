# -*- coding: utf-8 -*-
'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF971 - Estatística para Computação

---Autores---
Nome completo (iniciais)
Nome completo (iniciais)
Nome completo (iniciais)
Nome completo (iniciais)
Emerson Victor Ferreira da Luz (evfl)
Nome completo (iniciais)

Emails:  {iniciais, iniciais, iniciais, iniciais, evfl, iniciais}@cin.ufpe.br
Data:   2017-11-28
'''


class Particle:
    '''
    Classe que representa uma particula no grid.
    Ela possui os atributos x e y referentes a sua posição no grid
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self, direction):
        '''
            Método que realiza caminhada da particula de acordo
            com a direção passada como parâmetro
        '''
        if direction == "top":
            self.y -= 1
        elif direction == "right":
            self.x += 1
        elif direction == "bottom":
            self.y += 1
        elif direction == "left":
            self.x -= 1
        else:
            raise ValueError("Direction {0} invalid".format(direction))
