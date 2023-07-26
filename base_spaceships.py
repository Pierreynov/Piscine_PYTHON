class Spaceship :
    
    is_alive = True

    def __init__(self, attack = 0 , defense = 0 ) :
        self.attack = attack       
        self.defense = defense

    def take_damages(self, damage):
        """
        Définition de la methode pas de façon trop courte
        """
        if damage < 0 : 
            raise ValueError
        if (self.defense - damage) <= 0 :
            self.is_alive = False
            self.defense = 0
        else :
            self.defense -= damage 
    
    def fire_on(self, target) : 
       if target.defense - self.attack <= 0 :
           target.is_alive = False
           target.defense = 0
       else :
           target.defense -= self.attack


class Battleship(Spaceship) :
    """ Définition de la sous-classe Battleship qui hérite de la classe Spaceship"""

class Fighter(Spaceship) : 
    """ Définition de la sous-classe Fighter qui hérite de la classe Spaceship"""


