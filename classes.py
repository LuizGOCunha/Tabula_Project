import copy
from functools import total_ordering


@total_ordering
class NPC:
    def __init__(self, stg, agi, int, wis, cha, tou, per, wil, luc, ins):
        self.stg, self.agi, self.int, self.wis, self.cha = stg, agi, int, wis, cha
        self.tou, self.per, self.wil, self.luc, self.ins = tou, per, wil, luc, ins

    def __eq__(self, other):
        return self.agi == other.agi

    def __lt__(self, other):
        if self.agi == other.agi:
            return self.luc < other.luc
        return self.agi < other.agi

    @property
    def strength(self):
        return self.stg

    @property
    def agility(self):
        return self.agi

    @property
    def intelligence(self):
        return self.int

    @property
    def wisdom(self):
        return self.wis

    @property
    def charisma(self):
        return self.cha

    @property
    def toughness(self):
        return self.tou

    @property
    def perception(self):
        return self.per

    @property
    def willpower(self):
        return self.wil

    @property
    def luck(self):
        return self.luc

    @property
    def insight(self):
        return self.ins

    # função serve para retornar uma cópia perfeita do objeto, a fim de instanciá-lo no stage
    def instantiate(self):
        incarnate = copy.deepcopy(self)
        return incarnate

    class Palco:
        pass
