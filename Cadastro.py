cadastro = {}
pessoas = []
mulheres = []
s = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip().title()
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    if cadastro['sexo'] in 'F':
        mulheres.append(cadastro.copy())
    if cadastro['sexo'] not in 'MF':
        while True:
            print('ERRO! Apenas M ou F.')
            cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
            if cadastro['sexo'] in 'MF':
                break
    cadastro['Idade'] = int(input('Idade: '))
    s += cadastro['Idade']
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp not in 'SN':
        while True:
            print('ERRO! Apenas S ou N.')
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()
            if resp in 'SN':
                break
    pessoas.append(cadastro.copy())
    if resp == 'N':
        break
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idades é {s / len(pessoas):.2f}')
print('C) As pessoas do sexo feminino cadastradas foram: ', end='')
for c in range(0, len(mulheres)):
    print(f'{mulheres[c]["nome"]}, ', end='')
print()
print('D) Lista de pessoas acima da média.')
for k in range(0, len(pessoas)):
    if pessoas[k]['Idade'] > (s / len(pessoas)):
        print(f'    =>{pessoas[k]}')
