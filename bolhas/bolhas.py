#!/usr/bin/env python3
from tupy import *

class Campo(Image):
    def __init__(self):
        self.file = 'campo.png'
        self.x = 320
        self.y = 240

class Bolha(Image):
    def __init__(self, x, y, velocidade):
        self.file = 'bolha.png'
        self.x = x
        self.y = y
        self.velocidade = velocidade
    def update(self):
        self.y -= self.velocidade
        if self.y < -20:
            self.y = 520
        elif self.y > 520:
            self.y = -20
    
class Crianca(Image):
    def __init__(self, x, y):
        self.file = 'crianca.png'
        self.dir = 'right'
        self.x = x
        self.y = y
        self.pedra = Pedra(self)
        
    def update(self):
        if keyboard.is_key_just_down('Left'):
            self.file = 'humanleft.png'
            self.x -= 20
        if keyboard.is_key_just_down('Right'):
            self.file = 'humanright.png'
            self.x += 20
        if keyboard.is_key_just_down('Up'):
            self.file = 'humanup.png'
            self.y -= 20
        if keyboard.is_key_just_down('Down'):
            self.file = 'humandown.png'
            self.y += 20
        if keyboard.is_key_just_down('space'):
            self.lancar()
            
    def lancar(self):
        if self.pedra is not None:
            if self.pedra.moving is not True:
                self.pedra.throw()
            
class Pedra(Image):
    def __init__(self, child):
        self.file = 'empty.png'
        self.child = child
        self.x = child.x
        self.y = child.y
        '''initiates the first state of the rock being it not moving'''
        self.moving = False
    
    def throw(self):
        if not self.moving:
            self.x = self.child.x
            self.y = self.child.y
        if self.moving:
            self.angle -= 10
            self.x += 20
        else:
            self.moving = True
    
    def update(self):
        self.collides_with()
        if not self.moving:
            self.file = 'empty.png'
            if self.x != self.child.x:
                self.x = self.child.x
            if self.y != self.child.y:
                self.y = self.child.y
        if self.moving:
            self.file = 'coracao.png'
            
            if not self.moving:
                self.x = self.child.x
                self.y = self.child.y
            if self.moving:
                self.angle -= 10
                self.x += 20
            else:
                self.moving = True
                
            self.moving = True
        if self.x > 820:
            self.moving = False
            self.file = 'empty.png'
            self.x = self.child.x

            return 
    
    def collides_with(self):
        for i in bolhas:
            if super()._collides_with(i) is True:
                i.x = 1000
                i.y = 1000
                i.velocidade = 0
                bolhas.remove(i)
    
if __name__ == '__main__':
    campo = Campo()
    bolhas = [
    Bolha(710, 20, 5),
    Bolha(720, 30, 10),
    Bolha(730, 40, 15),
    ]
    kid = Crianca(40, 375)
    
    run(globals())
