from cartola_functions import *

#patrim = input('Qual seu patrimonio? ')
#print patrim

goleiro = ['nome', 'time', 'preco']
zagueiro1 = ['nome', 'time', 'preco']
zagueiro2 = ['nome', 'time', 'preco']
zagueiro3 = ['nome', 'time', 'preco']
meia1 = ['nome', 'time', 'preco']
meia2 = ['nome', 'time', 'preco']
meia3 = ['nome', 'time', 'preco']
meia4 = ['nome', 'time', 'preco']
atacante1 = ['nome', 'time', 'preco']
atacante2 = ['nome', 'time', 'preco']
atacante3 = ['nome', 'time', 'preco']
tecnico = ['nome', 'time', 'preco']

jogadoresConfirmados = popularJogadoresConfirmados()
goleirosConfirmados = jogadoresConfirmados[1]
lateraisConfirmados = jogadoresConfirmados[2]
zagueirosConfirmados = jogadoresConfirmados[3]
meiasConfirmados = jogadoresConfirmados[4]
atacantesConfirmados = jogadoresConfirmados[5]
tecnicos = jogadoresConfirmados[6]

print goleirosConfirmados
print lateraisConfirmados
print zagueirosConfirmados
print meiasConfirmados
print atacantesConfirmados
print tecnicos