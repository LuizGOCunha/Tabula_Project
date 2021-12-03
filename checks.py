
class NPC:
    def __init__(self, stg, agi, int, wis, cha, tou, per, wil, luc, ins):
        ###Facilita a referencia aos stats
        self.stg, self.agi, self.int, self.wis, self.cha = stg, agi, int, wis, cha
        self.tou, self.per, self.wil, self.luc, self.ins = tou, per, wil, luc, ins
        ###Aqui temos a barra que nos mostra o quanto um personagem tolerou de dano físico
        self.hp_saude = (tou * 5) + stg
        ###Aqui temos a barra que nos mostra o quanto um personagem tolerou de dano mental
        self.hp_stress = (wil * 5) + wis
        ###Dano básico de cada personagem quando desarmado
        self.base_damage = stg + agi/2
        ###Esse número deve ser testado contra o dodge de um inimigo para testar um acerto
        self.base_acc = round(((per * 3) + agi) * 3, 0)
        ###Ao fazer o calculo (base_acc - base_dodge) temos a porcentagem de chance de acerto
        self.base_dodge = round(((agi * 3) + per), 0)
        ###Esse número deve ser testado num range(n,200): se o rolar do dado for abaixo de n é crit.
        self.base_combat_crit = round((per/2 + agi/2 + luc)/10, 0)
        ###insight_q é testado contra stress_q (iq - sq), como uma defesa mental. INT representa a capacidade de racionalizar.
        self.insight_q = round((ins*2 + wil + int), 0)
        ###Capacidade que um personagem tem de trazer um amigo de volta à sanidade.
        self.pep_talk = cha*2 + wil


players_dic = {
    'PlayerTeste1' : NPC(10, 12, 6, 8, 9, 10, 12, 15, 8, 5),
    'PlayerTeste2' : NPC(10, 12, 6, 8, 9, 10, 12, 15, 8, 5),
    'PlayerTeste3' : NPC(10, 12, 6, 8, 9, 10, 12, 15, 8, 5),
    'PlayerTeste4' : NPC(10, 12, 6, 8, 9, 10, 12, 15, 8, 5)
}

print(players_dic['PlayerTeste1'].stg)