from base_spaceships import *
from spaceships import *
from fleet import *
import random

class Simulator :
    
    @staticmethod
    def _duel_fight(Attacker: Spaceship, Defender: Spaceship):
        if Defender.is_alive == True :
            Attacker.fire_on(Defender)
            if Defender.is_alive == True :
                Defender.fire_on(Attacker)
            
    @staticmethod
    def _simulate_fight(Attackers: list, Defenders: list):
        if len(Defenders) != 0:
            for attacker in Attackers:
                if attacker.is_alive == True:
                    Simulator._duel_fight(attacker, random.choice(Defenders))
                    
    def __init__(self, Attackers : Fleet, Defenders : Fleet):
        self.attackers = Attackers
        self.defenders = Defenders
        
    def fight(self):
        battleship_attack = self.attackers.get_alive_battleships()
        fighter_attack = self.attackers.get_alive_fighters()
        battleship_defend = self.defenders.get_alive_battleships()
        fighter_defend = self.defenders.get_alive_fighters()
                
        #step 1
        Simulator._simulate_fight(battleship_attack, battleship_defend)
        
        #step 2
        Simulator._simulate_fight(fighter_attack, fighter_defend)
        
        #step 3
        attack = self.attackers.get_all_alive_ships()
        defend = self.defenders.get_all_alive_ships()
        Simulator._simulate_fight(attack, defend)
        
    def get_report(self):
        result = {self.attackers.name : self.attackers.get_report(), self.defenders.name : self.defenders.get_report()}
        return result