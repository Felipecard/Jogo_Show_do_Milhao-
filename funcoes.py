import random

def Rodadas(perguntas, premio=1, soma_premio=1):

    respostas_certas = 0
    numero_pergunta = 1
    contador = 0
    pulos = 1

    while contador < 5:
        # Iterando com a funcao .items(), assim pude declarar valor para (pergunta key) e (pergunta value)
        pk, pv = random.choice(list(perguntas.items()))

        # SE FOR A PERGUNTA DE 1 MILHÃO 
        if pv["pergunta"] == 'Qual a empresa mais legal de se trabalhar?':
            print(f'Pergunta FINAL - Valendo {premio} MILHÃO de reais')
            pulos = 0
            print()
            print(f'{pv["pergunta"]}')
        else:
            print(f'\033[0;35mPergunta {numero_pergunta} \033[m - Valendo {premio} MIL reais')
            print()
            print(f'\033[0;33m{pv["pergunta"]} \033[m')
            numero_pergunta += 1
            premio += soma_premio

        print()
        # COLOCANDO AS ALTERNATIVAS DAS PERGUNTAS
        for rk, rv in pv['respostas'].items():
            rk = rk.upper()
            print(f'\033[0;34m[{rk}] \033[m - {rv}')

        letra_certa = True
        while letra_certa == True:
            print()
            print(f'\033[0;31m\U0001f998: {pulos}  \033[m')
            resposta_jogador = input('Qual sua resposta: ')
            resposta_jogador = resposta_jogador.lower()
            print()

            # TRATAMENTO DE ERRO DO USUÁRIO
            if resposta_jogador == 'a' or resposta_jogador == 'b' or resposta_jogador == 'c' or resposta_jogador == 'd' or resposta_jogador == 'p':
                letra_certa = False
            else:
                print('Digite somente: A, B, C ou D:')
                letra_certa = True

        # FUNCÃO DO PULO
        if resposta_jogador == 'p' and pulos > 0:
            pulos -= 1
            respostas_certas += 1
            continue

        # VERIFICA AS RESPOSTAS
        if resposta_jogador == pv['resposta_certa']:
            print('--' * 30)
            print('\033[0;32m CERTA RESPOSTA!!! \033[m')
            print('--' * 30)
            respostas_certas += 1

            # DELETA A PERGUNTA JA SORTEADA NO DICIONÁRIO
            perguntas.pop(pk, pv)
        else:
            print('\033[0;31mQUE PENA, VOCE ERROU.\033[m')
            print(F'\033[0;31m SEU PRÊMIO FOI DE APENAS: {(int(premio / 3))} mil reais \033[m')
            return respostas_certas
            break

        if respostas_certas == 5:
            return respostas_certas
            break

        # CASO SEJA A PERGUNTA DE 1 MILHÃO
        if pv["pergunta"] == 'Qual a empresa mais legal de se trabalhar?' and respostas_certas == 1 or respostas_certas == 0:
            return respostas_certas
        
        contador += 1
        print()


def Desenho_vitoria():
    print('\033[0;32m      GANHOOOOOOOU!!!  \033[m')
    print()
    print()
    print('        1 MILHÃO        ')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def Tela_inicial():
    print('=-' * 20)
    print('\033[0;32m         \U0001f451 SHOW DO MILHÃO \U0001f451  \033[m')
    print('=-' * 20)
    print('\U0001f4a1 Desafio para a Jovens Gênios')
    print('\U0001f4a1 Dev by Felipe Cardoso')
    print('--' * 20)
    print()
    print('\033[0;34m\u2622\uFE0FPRIMEIRA RODADA DE PERGUNTAS \u2622\uFE0F \033[m')


def Linha_estilo():
    print('--' * 30)


def Game_over():
    print('\033[0;31m    \U0001F634  GAME OVER \U0001F634 \033[m')


def Chamada_rodadas(perguntasA, perguntasB, perguntasC, perguntasFINAL):

    # CHAMA AS RODADAS SEGUINTES, DEPENDENDO DO ACERTO DAS 5 PERGUNTAS (A FUNCÃO 'Rodadas' ESTÁ RETORNANDO A VARIÁVEL 'respostas_certas')
    if Rodadas(perguntasA) == 5:
        print()
        print('\033[0;34m\u2622\uFE0FVAMOS AGORA PARA A SEGUNDA RODADA DE PERGUNTAS \u2622\uFE0F\033[m')
        Linha_estilo()
        if Rodadas(perguntasB, 10, 10) == 5:
            print()
            print('\033[0;34m\u2622\uFE0FMUITO BEM! VAMOS PARA A TERCEIRA RODADA DE PERGUNTAS \u2622\uFE0F\033[m')
            Linha_estilo()
            if Rodadas(perguntasC, 100, 100) == 5:
                print()
                print('\033[0;34m PARABÉNS!!! VOCÊ CHEGOU NA PERGUNTA DE 1 MILHÃO \033[m')
                Linha_estilo()
                if Rodadas(perguntasFINAL, 1, 1) == 1:
                    Desenho_vitoria()

                else:
                    print('\033[0;31m     VOCE PERDEU TUDO \033[m')
            else:
                Game_over()
        else:
            Game_over()
    else:
        Game_over()

    print()
