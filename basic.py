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
        dano = dano_base*2 + roll
    else:
        print("Acertou!")
        dano = dano_base + roll
    return vida_alvo - dano

###Criamos a função combate que toma todas as informações relevantes das classes NPC
###Estabelecemos os objetos dos heróis, então os dos inimigos, criando 2 times. É necessário fazer isso com flexibilidade.
###Então ordenamos o combate através de turnos. Puxando funções de ataque e cheques quando necessário.
###O combate termina quando todos os inimigos ou heróis estiverem mortos.
def combate_prompt():
    rodada = 1
    print('Quais os inimigos? (Quantidade e oponentes separados por espaço, e sempre em singular)')
    inpt_inimigos = input('>')
    lista_inimigos = inpt_inimigos.split(' ')
    numero_inimigos = lista_inimigos[0]
    inimigo_tipo = lista_inimigos[1]
    combate(numero_inimigos, inimigo_tipo)
    while True:
        print(f'Rodada:{rodada}')
        comando = input('>')
        lista_comando = comando.split(' ')
        if comando == "check":
            pass
        elif comando == "combate":
            rodada+=1
            pass
        elif comando == "reset":
            pass

def status_check(numero_inimigo, inimigo, inimigo_dic_loc):
    for x in range(1,numero_inimigo+1):
        print(f'{inimigo}{x}:')
        print(f'HP: {inimigo_dic_loc[x].hp_saude}')
        print(f'SP: {inimigo_dic_loc[x].hp_stress}')
