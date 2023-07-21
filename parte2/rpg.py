from random import randint

class Character:

    def __init__(self, user):
        self._user = user.captalize()
        self._level = 1
        self._attack_type = 'Fist'

    def level_up(self):
        self._level += 1

    @property
    def level(self):
        return self._level
    
    @property
    def user(self):
        return self._user
    
    @property
    def attack_type(self):
        return self._attack_type
    
    @attack_type.setter
    def attack_type(self, new_attack_type):
        self._attack_type = new_attack_type
    
    def attack(self):
        print(f"{self.user} uses {self.attack_type} to attack.")
    
class Warrior(Character):

    def __init__(self, user):
        super().__init__(user)
        self.attack_type = 'Sword'

    def protect(self):
        print(f"{self.user} is protecting himself with a shield.")