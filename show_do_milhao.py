from banco_perguntas import *
from funcoes import *

Tela_inicial()

ligado = 's'
while ligado == 's':
    Chamada_rodadas(perguntasA, perguntasB, perguntasC, perguntasFINAL)
    Linha_estilo()
    ligado = input('Deseja Jogar novamente? [S ou N] ')
    ligado = ligado.lower()
    Linha_estilo()