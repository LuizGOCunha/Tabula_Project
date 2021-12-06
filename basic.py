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




players_dic = {
    'PlayerTeste1' : NPC('Player1', 10, 12, 6, 8, 9, 10, 12, 15, 8, 5, 0),
    'PlayerTeste2' : NPC('Player2', 10, 12, 6, 8, 9, 10, 12, 15, 8, 5, 0),
    'PlayerTeste3' : NPC('Player3', 10, 12, 6, 8, 9, 10, 12, 15, 8, 5, 0),
    'PlayerTeste4' : NPC('Player4', 10, 12, 6, 8, 9, 10, 12, 15, 8, 5, 0)
}

inimigos_dic = {
'abominacao' : NPC(f'abominacao{rn}', 30, 2, 1, 1, 0, 20, 2, 8, 2, 50, 1),
'carnical' : NPC(f'carnical{rn}', 2, 20, 1, 1, 1, 3, 3, 2, 4, 25, 1),
'soldado' : NPC(f'soldado{rn}', 8, 8, 6, 4, 6, 9, 8, 16, 5, 15, 1),
'campones' : NPC(f'campones{rn}', 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1)
}


def ataque(roll, vida_alvo, dano_base,combate_crit,acc,dodge):
    roll_crit = 20 - combate_crit
    chance_acerto = acc - dodge
    dano = dano_base + roll
    if roll*5 > chance_acerto:
        print("Desviou!")
    elif roll >= roll_crit:
        print("CRITICO!")
        dano = dano*2
    else:
        print("Acertou!")
        vida_alvo-=dano
    return vida_alvo, dano

###Criamos a função combate que toma todas as informações relevantes das classes NPC
###Estabelecemos os objetos dos heróis, então os dos inimigos, criando 2 times. É necessário fazer isso com flexibilidade.
###Então ordenamos o combate através de turnos. Puxando funções de ataque e cheques quando necessário.
###O combate termina quando todos os inimigos ou heróis estiverem mortos.

def prompt(players_dic, npc_dic):
    print('Bem vindo ao projeto tábula.')
    while True:
        comando = input('>')
        if comando == "inserir":
           print('Inserir quem?')
           print(players_dic)
           insert_input = input('>')
           if insert_input == 'tudo':
               npc_dic.update(players_dic)
           else:
               # Não consigo fazer ele acrescentar um item por vez, lembra de consertar isso
               npc_dic.update(players_dic[insert_input])
        elif comando == "combate":
            npc_dic = combate_prompt(npc_dic)
        elif comando == "reset":
            print('Resetar quem?')
            reset_input = input('>')
            npc_dic[reset_input] = players_dic[reset_input]
        elif comando == 'check':
            print(npc_dic)
        elif comando == "exit":
            print('Até a próxima.')
            break

def status_check(npc_dic):
    for npc in npc_dic:
        print(f'{npc}:')
        print(f'HP: {npc_dic[npc].hp_saude}')

def combate_prompt(npc_dic):
    print('Quais os inimigos? (Quantidade e oponentes separados por espaço, e sempre em singular)')
    inpt_inimigos = input('>')
    lista_inimigos = inpt_inimigos.split(' ')
    numero_inimigos = int(lista_inimigos[0])
    inimigo_tipo = lista_inimigos[1]
    inim_dic_loc = {}
    ###Criar instancia de inimigo1, depois inimigo2, inimigo3, etc. Então colocar tudo em inim_dic_loc
    for n in range(1,numero_inimigos+1):
        inim_dic_loc[f'{inimigo_tipo}' + '{}'.format(n)] = inimigos_dic[inimigo_tipo]
    npc_dic.update(inim_dic_loc)
    ###Ordenar os turnos através dos valores de agilidade de todos dentro de npc_dic
    valores_npc_dic = npc_dic.values()
    lista_npc_dic = list(valores_npc_dic)
    ###Criar a lista de agilidades, preenchê-la com os valores dos players e então ordená-la
    lista_npc_agi = []
    for x in lista_npc_dic:
        lista_npc_agi.append(x.agi)
    lista_npc_agi.sort()
    ###Após isso rodar as rodadas em ordem de velocidade (magnitude de agi)
    # tudo está dando errado pois o player 2 3 e 4 tem a mesma agilidade que 1, então o 1 acaba indo varias vezes
    combat_end_flag = 0
    rodada = 1
    npc_dic = combate(combat_end_flag,rodada,lista_npc_dic,lista_npc_agi,npc_dic)
    print(npc_dic)


def players_adicao(npc_dic,players_dic):
    npc_dic += players_dic
    return npc_dic

def combate(combat_end_flag, rodada, lista_npc_dic, lista_npc_agi, npc_dic):
    while combat_end_flag == 0:
        print(f'Rodada:{rodada}')
        combat_continue_flag = 0
        for npc in lista_npc_dic:
            for n in range(1, len(lista_npc_dic) + 1):
                if npc.agi == lista_npc_agi[n]:
                    print(npc.nome)
                    print('O que fazer?')
                    acao = input('>')
                    if acao == 'atacar':
                        print('Qual o alvo?')
                        print(npc_dic)
                        # É necessário ter uma marca para os stats originais e ter um grupo para os stats alterados pelo combate
                        # Logo, é preciso utilizar o dicionario de players e inimigos como referencia, e o de npcs como valor alterável no rpg
                        alvo = input('>')
                        print('Qual o valor do dado?')
                        roll = int(input('>'))
                        npc_dic[alvo].hp_saude, dano_efetivo = ataque(roll, npc_dic[alvo].hp_saude, npc.base_damage,
                                                                      npc.base_combat_crit, npc.base_acc,
                                                                      npc_dic[alvo].base_dodge)
                        print(dano_efetivo)
                        print(npc_dic[alvo].hp_saude)
                        if npc_dic[alvo].hp_saude < 0:
                            print('O alvo morreu!')
                            del npc_dic[alvo]
                        if npc.hp_saude < 0:
                            print('Você morreu!')
                            del npc_dic[npc]
                        rodada += 1
                    if acao == 'check':
                        status_check(npc_dic)
                    else:
                        print('___________')
                    # Após checar as ações é necessário checar os times para saber se o combate continua para o próximo round
                    # Se todos forem do mesmo time dos players, o combate se encerra. Caso contrario continua.
                    for time in npc_dic:
                        if npc_dic[time].time == 0:
                            # Esse é dos nossos, checa o próximo
                            continue
                        else:
                            # Esse é inimigo, continua o combate
                            combat_continue_flag += 1
                            break
                    if combat_continue_flag == 0:
                        combat_end_flag += 1
                    rodada += 1
    return npc_dic
