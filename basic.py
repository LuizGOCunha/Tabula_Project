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
def combate():
    while True:
        rodada=1
        print(f'Rodada:{rodada}')
        comando = input('>')
        lista_comando = comando.split(' ')
        if comando = 'check':
            continue
        if comando = 'combate':
            continue

        rodada+=1