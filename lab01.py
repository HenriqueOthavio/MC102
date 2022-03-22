nome = str(input('Nome do material:'))
t_f = float(input('fusao:'))  # solido-> liquido
t_e = float(input('ebulisao:'))  # liquido->gasoso
t_a = float(input('atual:'))
t = (t_a - 32)*5/9               #convertendo
if t < t_f :
    ef='Solido'
elif t < t_e:
    ef='Liquido'
else:
    ef='Gasoso'

t= format(t,'.2f')#formatando a saida
t_e= format(t_e,'.2f')
t_f= format(t_f,'.2f')

print('Material:', nome)
print('Ponto de fusao', t_f)
print('Ponto de ebulicao:', t_e)
print('Temperatura atual:',t)
print('Estado fisico do material:',ef)
