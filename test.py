import random


class NPC:
    def __init__(self, nome, stg, agi, int, wis, cha, tou, per, wil, luc, ins, time):
        ###Facilita a referencia aos stats
        self.time = time
        self.nome = nome
        self.stg, self.agi, self.int, self.wis, self.cha = stg, agi, int, wis, cha
        self.tou, self.per, self.wil, self.luc, self.ins = tou, per, wil, luc, ins
        #Aqui temos a barra que nos mostra o quanto um personagem tolerou de dano físico
        self.hp_saude = (tou * 5) + stg
        ###Aqui temos a barra que nos mostra o quanto um personagem tolerou de dano mental
        self.hp_stress = (wil * 5) + wis
        ###Dano básico de cada personagem quando desarmado
        self.base_damage = stg + agi/2
        ###Esse número deve ser testado contra o dodge de um inimigo para testar um acerto
        self.base_acc = round(((per * 3) + agi) * 5, 0)
        ###Ao fazer o calculo (base_acc - base_dodge) temos a porcentagem de chance de acerto
        self.base_dodge = round(((agi * 3) + per) * 2, 0)
        ###Esse número deve ser testado num range(n,20): se o rolar do dado for abaixo de n é crit.
        self.base_combat_crit = round((per/2 + agi/2 + luc)/10, 0)
        ###insight_q é testado contra stress_q (iq - sq), como uma defesa mental. INT representa a capacidade de racionalizar.
        self.insight_q = round((ins*2 + wil + int), 0)
        ###Capacidade que um personagem tem de trazer um amigo de volta à sanidade.
        self.pep_talk = cha*2 + wil

rn = random.randint(0,100)

npc_lista = [
    NPC(f'Player4',10, 13, 6, 8, 9, 10, 12, 15, 8, 5,0),
    NPC(f'Player3',10, 14, 6, 8, 9, 10, 12, 15, 8, 5,0),
    NPC(f'Player2',10, 11, 6, 8, 9, 10, 12, 15, 8, 5,0),
    NPC(f'Player1',10, 15, 6, 8, 9, 10, 12, 15, 8, 5,0)
]
#dic2 = {}

#list = [20,40,60,30]

#list2 = ['vinte', 'quarenta', 'sessenta', 'trinta']




npc = []

for indx, x in enumerate(npc_lista):
    npc.append(npc_lista[indx])
npc[1].hp_saude -= 3000
print(npc_lista[1].hp_saude)








#npc_lista_agi = []
#while npc_lista:
#    minimum = npc_lista[0]
#    for x in npc_lista:
#        if x.agi < minimum.agi:
#            minimum = x
#    npc_lista_agi.append(minimum)
#    npc_lista.remove(minimum)
#npc_lista = npc_lista_agi
#for x in npc_lista:
#    print(x.nome)




#for idx1, x in enumerate(list):
#    if x == 40:
#        for idx2, y in enumerate(list2):
#            if y == 'quarenta':
#                list[idx1] = list2[idx2]
#print(list, list2)

#for idx, val in enumerate(list):
#    print(idx, val)




#valores_npc_dic = players_dic.values()
#lista_npc_dic = list(valores_npc_dic)
#lista_npc_agi = []
#for x in lista_npc_dic:
#    lista_npc_agi.append(x.agi)
#
#print(lista_npc_agi)