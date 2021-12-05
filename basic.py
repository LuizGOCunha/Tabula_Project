from main import *

### Combate:
    ### Combate vai ocorrer através de um cheque de velocidade (feito através de agilidade), e a partirdaí todos irão
    ### obedecer a ordem ditada. Então aliados e oponentes irão seguir a ordem de ação e decidir o que fazer em cada turno,
    ### liberdade de ação sendo limitada pela criatividade do jogador e do DM.

def ataque(roll, vida_alvo, dano_base,combate_crit,acc,dodge):
    roll_crit = 20 - combate_crit
    chance_acerto = acc - dodge
    if roll*5 > chance_acerto:
        print("Desviou!")
    if roll >= roll_crit:
        print("CRITICO!")
        dano = dano_base*2 + roll/2
    else:
        print("Acertou!")
        dano = dano_base + roll
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
               npc_dic.append(players_dic)
           else:
               npc_dic.append(players_dic[insert_input])
        elif comando == "combate":
            npc_dic = combate_prompt(npc_dic)
        elif comando == "reset":
            print('Resetar quem?')
            reset_input = input('>')
            npc_dic[reset_input] = players_dic[reset_input]
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
    numero_inimigos = lista_inimigos[0]
    inimigo_tipo = lista_inimigos[1]
    inim_dic_loc = {}
    ###Criar instancia de inimigo1, depois inimigo2, inimigo3, etc. Então colocar tudo em inim_dic_loc
    for n in range(1,numero_inimigos+1):
        inim_dic_loc[f'{inimigo_tipo}' + '{}'.format(n)] = inimigos_dic[inimigo_tipo]
    npc_dic += inim_dic_loc
    ###Ordenar os turnos através dos valores de agilidade de todos dentro de npc_dic
    valores_npc_dic = npc_dic.values()
    lista_npc_dic = list(valores_npc_dic)
    ###Criar a lista de agilidades, preenchê-la com os valores dos players e então ordená-la
    lista_npc_agi = []
    for x in lista_npc_dic:
        lista_npc_agi.append(x.agi)
    lista_npc_agi.sort()
    ###Após isso rodar as rodadas em ordem de velocidade (magnitude de agi)
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
                    print('O que fazer?')
                    acao = input('>')
                    if acao == 'atacar':
                        print('Qual o alvo?')
                        print(npc_dic)
                        # É necessário ter uma marca para os stats originais e ter um grupo para os stats alterados pelo combate
                        # Logo, é preciso utilizar o dicionario de players e inimigos como referencia, e o de npcs como valor alterável no rpg
                        alvo = input('>')
                        print('Qual o valor do dado?')
                        roll = input('>')
                        npc_dic[alvo].hp_saude, dano_efetivo = ataque(roll, npc_dic[alvo], npc.base_damage,
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
                        print('não entendi')
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
