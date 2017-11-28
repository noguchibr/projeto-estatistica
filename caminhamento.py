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
Ewerton Felipe Ferreira da Silva (effs)

Emails:  {iniciais, iniciais, iniciais, iniciais, evfl, effs}@cin.ufpe.br
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

    def __str__(self):
        return "(x:{0}, y:{1})".format(self.x, self.y)

    def walk(self, direction):
        '''
            Método que realiza caminhada da particula de acordo
            com a direção passada como parâmetro
        '''
        if direction == "top":
            if self.y > 0:
                self.y -= 1
            else:
                self.y = 24

        elif direction == "right":
            if self.x < 25:
                self.x += 1
            else:
                self.x = 1

        elif direction == "bottom":
            if self.y < 25:
                self.y += 1
            else:
                self.y = 1

        elif direction == "left":
            if self.x > 0:
                self.x -= 1
            else:
                self.x = 24

        else:
            raise ValueError("Direction {0} invalid".format(direction))
