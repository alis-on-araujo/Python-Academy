carne = input('qual carne você deseja? ')

#kg atual:
kg = 0

#kg de cada carne:
kg_patinho = 0
kg_acem = 0
kg_peito = 0
kg_sobrecoxa = 0
kg_bisteca = 0

#carne bovina:
kg_bovina = 0
v_bovina = 0

#valor de cada carne:
v_patinho = 0
v_acem = 0
v_peito = 0
v_sobrecoxa = 0
v_bisteca = 0


#carnes presentes:
bovina = False
frango = False
suina = False

#valor em bandeja:
bandeja = 0

#pergunta bendeja:
pergunta_bandeja = 0 

#valor total:
valor = 0

while carne != 'pagar':
    
    if carne != 'patinho' and carne != 'acem' and carne != 'peito' and carne != 'sobrecoxa' and carne != 'bisteca' and carne != 'pagar':
        print("Carne nao reconhecida - tente novamente." )
        carne = input('qual carne você deseja? ')

    elif carne == 'patinho':

        bovina = True
        kg = float(input('quantos kg vc deseja? '))
        kg_patinho += kg
        kg_bovina += kg
        v_patinho += kg * 40
        v_bovina += v_patinho

        pergunta_bandeja = input('deseja bandeja? (s/n) ')
        if pergunta_bandeja == 's' and kg >= 1:
                bandeja += kg * 0.5
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 's' and kg < 1:
                bandeja += 0
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 'n':
                carne = input('qual outra carne você deseja? ')
    
    elif carne == 'acem':

        bovina = True
        kg = float(input('quantos kg vc deseja? '))
        kg_acem += kg
        kg_bovina += kg
        v_acem += kg * 34
        v_bovina += v_acem

        pergunta_bandeja = input('deseja bandeja? (s/n) ')
        if pergunta_bandeja == 's' and kg >= 1:
                bandeja += kg * 0.5
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 's' and kg < 1:
                bandeja += 0
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 'n':
                carne = input('qual outra carne você deseja? ')

    elif carne == 'peito':

        frango = True
        kg = float(input('quantos kg vc deseja? '))
        kg_peito += kg
        v_peito += kg * 24

        pergunta_bandeja = input('deseja bandeja? (s/n) ')
        if pergunta_bandeja == 's' and kg >= 1:
                bandeja += kg * 0.5
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 's' and kg < 1:
                bandeja += 0
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 'n':
                carne = input('qual outra carne você deseja? ')
    
    elif carne == 'sobrecoxa':

        frango = True
        kg = float(input('quantos kg vc deseja? '))
        kg_sobrecoxa += kg
        v_sobrecoxa += kg * 13

        pergunta_bandeja = input('deseja bandeja? (s/n) ')
        if pergunta_bandeja == 's' and kg >= 1:
                bandeja += kg * 0.5
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 's' and kg < 1:
                bandeja += 0
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 'n':
                carne = input('qual outra carne você deseja? ')

    elif carne == 'bisteca':

        suina = True
        kg = float(input('quantos kg vc deseja? '))
        kg_bisteca += kg
        v_bisteca += kg * 28

        pergunta_bandeja = input('deseja bandeja? (s/n) ')
        if pergunta_bandeja == 's' and kg >= 1:
                bandeja += kg * 0.5
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 's' and kg < 1:
                bandeja += 0
                carne = input('qual outra carne você deseja? ')
        elif pergunta_bandeja == 'n':
                carne = input('qual outra carne você deseja? ')
    
    elif carne == 'pagar':
        break

if kg_bovina >= 3 and kg_bovina < 5:
    valor = (0.95 * v_bovina) + v_peito + v_sobrecoxa + v_bisteca + bandeja

elif kg_bovina >= 5:
    valor = (0.93 * v_bovina) + v_peito + v_sobrecoxa + v_bisteca + bandeja

else:
    valor = v_bovina + v_peito + v_sobrecoxa + v_bisteca + bandeja

if bovina == True and frango == True and suina == True:
    valor *= 0.9

print('O total da sua compra foi {0:.2f}'.format(valor))

