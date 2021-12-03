### STATS:
    ### STRENGTH: A potência dos seus músculos
    ### AGILITY: Sua capacidade de se mover de forma complexa e ligeira.
    ### INTELLIGENCE: Seu potencial na arte de resolução de problemas práticos.
    ### WISDOM: Sua compreensão de conceitos abstratos (sentimentos, culturas, experiências).
    ### CHARISMA: Sua capacidade de convencer, enganar e fazer amizades.
    ### TOUGHNESS: O quão capaz é o seu corpo de suportar dano físico.
    ### PERCEPTION: Seu potencial em observar e ser alertado por detalhes sutis.
    ### WILLPOWER: Sua capacidade de suportar ataques mentais e de se manter coeso em meio à dor e caos.
    ### LUCK: Você é abençoado por boa fortuna, ou é muito bom em manipular as chances por debaixo dos panos.
    ### INSIGHT: Você sabe de acontecidos, entidades e fatos que ninguém deveria. Sem willpower equivalente, pode levar a loucura.

### GIFTED QUOTIENT:
    ### COMUM: 50 points
    ### INCOMUM: 75 points
    ### RARO: 100 points
    ### TALENTOSO: 125 points
    ### ÚNICO: 150 points
    ### LENDÁRIO: 200 points
    ### ABENÇOADO: 500 points
    ### XAMÃ: 1000 points


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

def combate(numero_inimigos, inimigo_tipo, players_dic):
    inim_dic_loc = {}
    ###Criar instancia de inimigo1, depois inimigo2, inimigo3, etc. Então colocar tudo em inim_dic_loc
    for n in range(1,numero_inimigos+1):
        inim_dic_loc[f'{inimigo_tipo}' + '{}'.format(n)] = inimigos_dic[inimigo_tipo]
    npc_dic = players_dic + inim_dic_loc
    ###Ordenar os turnos através dos valores de agilidade de todos dentro de npc_dic
    valores_npc_dic = npc_dic.values()
    lista_npc_dic = list(valores_npc_dic)
    ###Criar a lista de agilidades, preenchê-la com os valores dos players e então ordená-la
    lista_npc_agi = []
    for x in lista_npc_dic:
        lista_npc_agi.append(x.agi)
    lista_npc_agi.sort()




players_dic = {
    'PlayerTeste1' : NPC(10, 12, 6, 8, 9, 10, 12, 15, 8, 5),
    'PlayerTeste2' : NPC(10, 12, 6, 8, 9, 10, 12, 15, 8, 5),
    'PlayerTeste3' : NPC(10, 12, 6, 8, 9, 10, 12, 15, 8, 5),
    'PlayerTeste4' : NPC(10, 12, 6, 8, 9, 10, 12, 15, 8, 5)
}

inimigos_dic = {
'abominacao' : NPC(30, 2, 1, 1, 0, 20, 2, 8, 2, 50),
'carnical' : NPC(2, 20, 1, 1, 1, 3, 3, 2, 4, 25),
'soldado' : NPC(8, 8, 6, 4, 6, 9, 8, 7, 5, 15),
'campones' : NPC(5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
}


print(inimigos_dic['abominacao'].hp_saude)

