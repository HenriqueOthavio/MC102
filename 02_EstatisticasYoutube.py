canal = input()
n = int(input())
a18 = 0
a19 = 0
a20 = 0
v18 = 0
v19 = 0
v20 = 0
# armazenando os dados#
for i in range(n):
    data = input()
    views = int(input())
    data_split = data.split('-')

    if data_split[0] == '2018':
        a18 += 1
        v18 += views
    elif data_split[0] == '2019':
        a19 += 1
        v19 += views
    elif data_split[0] == '2020':
        a20 += 1
        v20 += views
# calculando as informações pedidas#
vt = v18 + v19 + v20
at = a18 + a19 + a20
mv = vt / at
m18 = v18 / a18
m19 = v19 / a19
m20 = v20 / a20

# cuidado ao dividir por ZER0
if v18 != 0:
    p18 = v18 / vt
else:
    p18 = 'indeterminada'
if v19 != 0:
    p19 = v19 / vt
else:
    p19 = 'indeterminada'
if v20 != 0:
    p20 = v20 / vt
else:
    p20 = 'indeterminada'
# Printando os valores
print('Canal:', canal)
print('Total de views do trienio:', vt)
print('Media de views do trienio:', format(mv, '.2f'), "\n")
print('2018')
print('Total:', v18)
print('Porcentagem das views do trienio:', format(100*p18, '.2f'))
print('Media:', format(m18, '.2f'), "\n")
print(2019)
print('Total:', v19)
print('Porcentagem das views do trienio:', format(100*p19, '.2f'))
print('Media:', format(m19, '.2f'), "\n")
print('2020')
print('Total:', v20)
print('Porcentagem das views do trienio:', format(100*p20, '.2f'))
print('Media:', format(m20, '.2f'))
# agradecimentos a larissa ayumi okabayashi,  por me ensinar a usar o comando format <3
