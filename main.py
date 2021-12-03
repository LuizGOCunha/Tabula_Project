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


abominacao = NPC(30, 2, 1, 1, 0, 20, 2, 8, 2, 50)
carnical = NPC(2,20,1,1,1,3,3,2,4,25)
soldado = NPC(8,8,6,4,6,9,8,7,5,15)
campones = NPC(5,5,5,5,5,5,5,5,5,5)

print(abominacao.hp_saude)
