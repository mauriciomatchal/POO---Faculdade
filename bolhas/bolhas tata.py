
from tupy import *


class Bolha(Image): 
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade 
        self.file = "bolha.png"

    def update(self):
        self.y -= self.velocidade 
        if self.y < -20:
            self.y = 520
        elif self.y > 520:
            self.y = -20
        


    def destroy(self):
        inspector.destroy_object(self)
        objects.remove_object(self)
        window.update_object_pane()





class Crianca(Image):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.file =  'crianca.png'
        self.move = False
        self.pedra = Pedra(self)

    def update(self):
        if keyboard.is_key_just_down('Up'):
            self.y -= 20
        if keyboard.is_key_just_down('Down'):
            self.y += 20
        if keyboard.is_key_just_down('Right'):
            self.x += 20
        if keyboard.is_key_just_down('Left'):
            self.x -= 20
        if keyboard.is_key_just_down('space'): 
            self.lancar() 
        

    def lancar(self):  
      if self.pedra is not None:
            if self.pedra.move is not True:
                self.pedra.moove()
      

    def destroy(self):
        inspector.destroy_object(self)
        objects.remove_object(self)
        window.update_object_pane()   

class Pedra(Image):
    def __init__(self, crianca):
        self.x = crianca.x 
        self.y = crianca.y
        self.crianca = crianca
        self.file = 'pedra.png'
        self.move = False


    def moove(self): 
        if self.move is False:
            self.x = self.crianca.x
            self.y = self.crianca.y
        if self.move:
            self.x += 20
        else:
            self.move = True

    def update(self):
        self.collides_with()
        if self.move is False and self.x != self.crianca.x:
            self.x = self.crianca.x
        if self.move is False and self.y != self.crianca.y:
            self.y = self.crianca.y
        if self.move:
            self.moove() 
        if self.x > 820:
            self.x = self.crianca.x
            self.move = False
            return







    def _collides_with(self, other) -> bool:
        return super()._collides_with(other)

    def collides_with(self) -> None:
        for obj in bolhas:
            if self._collides_with(obj):
                obj.x = 900
                obj.y = 900
                obj.velocidade = 0
                bolhas.remove(obj)
                    




if __name__ == '__main__':

    bolhas = [
    Bolha(710, 20, 5),
    Bolha(720, 30, 10),
    Bolha(730, 40, 15),
    ]



    

    run(globals())

