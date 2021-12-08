import random

### Combate:
    ### Combate vai ocorrer através de um cheque de velocidade (feito através de agilidade), e a partirdaí todos irão
    ### obedecer a ordem ditada. Então aliados e oponentes irão seguir a ordem de ação e decidir o que fazer em cada turno,
    ### liberdade de ação sendo limitada pela criatividade do jogador e do DM.

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




players_lista = [
    NPC('Player1', 10, 12, 6, 8, 9, 10, 12, 15, 8, 5, 0),
    NPC('Player2', 10, 12, 6, 8, 9, 10, 12, 15, 8, 5, 0),
    NPC('Player3', 10, 12, 6, 8, 9, 10, 12, 15, 8, 5, 0),
    NPC('Player4', 10, 12, 6, 8, 9, 10, 12, 15, 8, 5, 0)
]

inimigos_lista = [
NPC(f'abominacao{rn}', 30, 2, 1, 1, 0, 20, 2, 8, 2, 50, 1),
NPC(f'carnical{rn}', 1, 13, 1, 1, 1, 3, 3, 2, 4, 25, 1),
NPC(f'soldado{rn}', 8, 8, 6, 4, 6, 9, 8, 16, 5, 15, 1),
NPC(f'campones{rn}', 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1)
]


def ataque(roll, vida_alvo, dano_base,combate_crit,acc,dodge):
    roll_crit = 20 - combate_crit
    chance_acerto = acc - dodge
    dano = dano_base + roll
    if roll*5 < chance_acerto:
        print("Desviou!")
    elif roll >= roll_crit:
        print("CRITICO!")
        dano = dano*2
        vida_alvo-=dano
    else:
        print("Acertou!")
        vida_alvo-=dano
    return vida_alvo, dano

###Criamos a função combate que toma todas as informações relevantes das classes NPC
###Estabelecemos os objetos dos heróis, então os dos inimigos, criando 2 times. É necessário fazer isso com flexibilidade.
###Então ordenamos o combate através de turnos. Puxando funções de ataque e cheques quando necessário.
###O combate termina quando todos os inimigos ou heróis estiverem mortos.

def prompt(players_lista, npc_lista):
    print('Bem vindo ao projeto Tabula.')
    while True:
        comando = input('>')
        if comando == "inserir":
            # comando inserir adiciona personagens do nosso "players_lista" ao nosso cercado "npc_lista".
           print('Inserir quem?')
           for x in players_lista:
                print(x.nome)
           insert_input = input('>')
           if insert_input == 'tudo':
               for x in players_lista:
                   npc_lista.append(x)
               for x in npc_lista:
                   print(x.nome)
           else:
               for npc in players_lista:
                    if npc.nome == insert_input:
                        npc_lista.append(npc)
        elif comando == "combate":
            npc_lista = combate_prompt(npc_lista)
        elif comando == "reset":
            print('Resetar quem?')
            reset_input = input('>')
            for idx1, npc in enumerate(npc_lista):
                if npc.nome == reset_input:
                    for idx2, npc_stat in enumerate(players_lista):
                        if npc.nome == npc_stat.nome:
                            npc_lista[idx1] = npc_stat[idx2]
        elif comando == 'check':
            for x in npc_lista:
                print(x.nome, x.hp_saude)
        elif comando == "exit":
            print('Até a próxima.')
            exit()

def status_check(npc_lista):
    for indxc, npc in enumerate(npc_lista):
        print(f'{npc_lista[indxc].nome}:')
        print(f'HP: {npc_lista[indxc].hp_saude}')

def combate_prompt(npc_lista):
    print('Quais os inimigos? (Quantidade e oponentes separados por espaço, e sempre em singular)')
    for indx, x in enumerate(inimigos_lista):
        print(indx, inimigos_lista[indx].nome, inimigos_lista[indx].hp_saude)
    inpt_inimigos = input('>')
    lista_input = inpt_inimigos.split(' ')
    numero_inimigos = int(lista_input[0])
    inimigo_tipo = lista_input[1]
    ###Criar instancia de inimigos. Então colocar tudo em npc_lista
    for indx, x in enumerate(inimigos_lista):
        if x.nome == inimigo_tipo:
            for n in range(0,numero_inimigos):
                npc_lista.append(inimigos_lista[indx]) # Aqui ele vai adicionar o mesmo inimigo varias vezes, é bom ter uma identificação, olha isso depois
    ###Ordenar os turnos através dos valores de agilidade de todos dentro de npc_lista
    npc_lista_agi = []
    while npc_lista:
        max = npc_lista[0]
        for x in npc_lista:     # Esse for serve para saber qual o maior valor
            if x.agi > max.agi:
                max = x
        npc_lista_agi.append(max)       # Então acrescentamos o maior valor nessa lista
        npc_lista.remove(max)           # E removemos nesta
    npc_lista = npc_lista_agi               # Depois é só igualar a lista antiga à organizada e pronto, tudo em ordem
    for x in npc_lista:
        print(x.nome)
    ###Após isso rodar as rodadas em ordem de velocidade (magnitude de agi)
    combat_end_flag = 0
    rodada = 1
    npc_lista = combate(combat_end_flag, rodada,npc_lista)
    print(npc_lista)
    return npc_lista


def players_adicao(npc_dic,players_dic):
    npc_dic += players_dic
    return npc_dic

def combate(combat_end_flag, rodada, npc_lista):
    while combat_end_flag == 0:
        print(f'Rodada:{rodada}')
        combat_continue_flag = 0
        for indxr, npc in enumerate(npc_lista):
             print(indxr,npc.nome)
             print('O que fazer?')
             acao = input('>')
             if acao == 'atacar':
                 # Esse for loop nada mais é que a rodada inteira, ordenada pelo atributo agilidade
                 # O for vai rodar em ordem decrescente de agi, e cada um terá seu turno na ordem adequada
                 print('Qual o alvo? (Use o index para identificar)')
                 for indx, x in enumerate(npc_lista):
                     print(indx, npc_lista[indx].nome, npc_lista[indx].hp_saude)
                 alvo = int(input('>'))
                 print('Qual o valor do dado?')
                 roll = int(input('>'))
                 npc_lista[alvo].hp_saude, dano_efetivo = ataque(roll,
                                                                 npc_lista[alvo].hp_saude,
                                                                 npc_lista[indxr].base_damage,
                                                                 npc_lista[indxr].base_combat_crit,
                                                                 npc_lista[indxr].base_acc,
                                                                 npc_lista[alvo].base_dodge)
                 print(f'Dano: {dano_efetivo}')
                 print(f'Vida do alvo:{npc_lista[alvo].hp_saude}')
                 if npc_lista[alvo].hp_saude < 0:
                    print('O alvo morreu!')
                    npc_lista.remove(npc_lista[alvo])
                 if npc.hp_saude < 0:
                    print('Você morreu!')
                    npc_lista.remove(npc_lista[indxr])
                 rodada += 1
             if acao == 'check':
                 status_check(npc_lista)
             else:
                 print('___________')
             # Após checar as ações é necessário checar os times para saber se o combate continua para o próximo round
             # Se todos forem do mesmo time dos players, o combate se encerra. Caso contrario continua.
             for indx,npc in enumerate(npc_lista):
                 if npc_lista[indx].time == 0:
                     # Esse é dos nossos, checa o próximo
                     continue
                 else:
                     # Esse é inimigo, continua o combate
                     combat_continue_flag += 1
                     break
             if combat_continue_flag == 0:
                 combat_end_flag += 1
             rodada += 1
    return npc_lista
