# definições
pessoa = {
    'Nome':
    'CPF'
    'RG'
    'Data de Nascimento'
    'Gênero'
    'E-mail'
    'Telefone'
    'Tipo Sanguíneo'
    'Profissão'
    'Empresa'
}
# insira os dados
pessoa['Nome'] = input('Informe o nome: ')
pessoa['CPF'] = input('Informe o seu CPF: ')
pessoa['RG'] = input('Informe o seu RG: ')
pessoa['Data de Nascimento'] = input('Informe a sua data de nascimento: ').replace('/','-')
pessoa['Gênero'] = input('Informe o seu Gênero: ')
pessoa['E-mail'] = input('Informe o seu E-mail: ')
pessoa['Telefone'] = input('Informe o seu Telefone: ')
pessoa['Tipo Sanguíneo'] = input('Informe o seu tipo sanguíneo: ')
pessoa['Profissão'] = input('Informe a sua profissão: ')
pessoa['Empresa'] = input('Informe o nome da empresa onde trabalha: ')


print(pessoa)


while True:

# verifica se o usuário deseja continuar
    continuar = input('Deseja continuar (s/n)? ')


# verifica se o usuário deseja continuar
    if continuar == 's':
        continue
    elif continuar == 'n':
        break
    else:
        print('Opção inválida')
        continue


