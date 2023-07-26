from base_spaceships import Fighter, Battleship

class BattleshipKiller :
    def fire_on(self,target) :
        if (isinstance(target, Battleship)):
            print("double degats")
            target.take_damages(self.attack * 2)
        else :
            target.take_damages(self.attack)
        return target

class FighterKiller : 
    def fire_on(self, target) :
        if (isinstance(target, Fighter)):
            target.take_damages(self.attack * 2)
        else :
            target.take_damages(self.attack)
        return target

class Interceptor(FighterKiller, Fighter) :
    def __init__(self, attack=0, defense=0):
        super().__init__(180, 1000)

class Bomber(BattleshipKiller, Fighter) :
    def __init__(self, attack=0, defense=0):
        super().__init__(150, 2000)

class Cruiser(Battleship) :
    def __init__(self, attack=0, defense=0):
        super().__init__(800, 3000)

class Frigate(FighterKiller, Battleship) :
    def __init__(self, attack=0, defense=0):
        super().__init__(500, 2500)
    
class Destroyer(BattleshipKiller, Battleship) :
    def __init__(self, attack=0, defense=0):
        super().__init__(650, 5000)
    

