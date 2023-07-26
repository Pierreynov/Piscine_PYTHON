from base_spaceships import *
from spaceships import *

class Fleet :
    
    def __init__(self, name, ships) :
        self.name = name
        self.ships = ships
    
    def get_all_alive_ships(self):
        result = []
        for ship in self.ships:
            if ship.is_alive == True:
                result.append(ship)
        return result
    
    alive_ships = property(get_all_alive_ships)
    
    def get_alive_battleships(self):
        res = []
        for ship in self.alive_ships :
            if isinstance(ship, Battleship) :
                res.append(ship)
        return res

    def get_alive_fighters(self):
        res = []
        for ship in self.alive_ships :
            if isinstance(ship, Fighter ) :
                res.append(ship)
        return res
    
    alive_fighters = property(get_alive_fighters)
    alive_battleships = property(get_alive_battleships)
    
    def get_report(self):
        cpt_f = 0
        cpt_b = 0
        result = {
            'alive_battleships' : int,
            'alive_fighters' : int,
            'dead_battleships': int,
            'dead_fighters' : int
        }
        for ship in self.ships:
            if isinstance(ship, Fighter):
                cpt_f += 1
            else:
                cpt_b += 1
        result['alive_battleships'] = len(self.alive_battleships)
        result['alive_fighters'] = len(self.alive_fighters)
        result['dead_battleships'] = cpt_b - len(self.alive_battleships)
        result['dead_fighters'] = cpt_f - len(self.alive_fighters)
        return result

    report = property(get_report)