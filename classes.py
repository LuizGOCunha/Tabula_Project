class NPC:
    def __init__(self, stg, agi, int, wis, cha, tou, per, wil, luc, ins):
        ###Facilita a referencia aos stats
        self.stg, self.agi, self.int, self.wis, self.cha = stg, agi, int, wis, cha
        self.tou, self.per, self.wil, self.luc, self.ins = tou, per, wil, luc, ins