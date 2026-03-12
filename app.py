import os

restaurantes = [{'nome': 'Praça', 'categoria': 'japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False},
                {'nome': 'Burguer', 'categoria': 'Hamburguer', 'ativo': True}]


def exibir_nome_do_programa():
    '''Essa função é responsável por exibir o nome do programa no topo'''
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')


def exibir_opcoes():
    '''Essa função é responsável por exibir as opções do menu'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar estado do Restaurante')
    print('4. Alterar nome do Restaurante')
    print('5. Sair\n')


def finalizar_app():
    '''Essa função é responsável por finalizar o app'''
    exibir_subtitulo('App finalizado')


def voltar_ao_menu_principal():
    '''Essa função é responsável por voltar ao menu principal

    Input:
    - Tecla para retornar ao menu

    Output:
    - Voltar ao menu

    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    '''Essa função é responsável por informar a opção inválida e voltar ao menu'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir os subtítulos de outras funcionalidades'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Output:
    - Adiciona novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(
        f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrado'''

    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alterar_nome_restaurante():
    '''Essa função é responsável por alterar o nome de algum restaurante já existente,
       recebe como dados de input: nome do restaurante que deseja alterar, nome novo
       output: muda o nome do restaurante já existente para um novo nome'''

    exibir_subtitulo('Alterar nome do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o nome: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            novo_nome = input('Digite o novo nome do restaurante: ')
            restaurante['nome'] = novo_nome
            print(
                f'O nome do restaurante {nome_restaurante} foi alterado para {novo_nome} com sucesso!')
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado do restaurante'''

    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            escolha = input(
                'Você gostaria de ativar ou desativar o restaurante? ')
            if escolha.lower() == 'ativar':
                restaurante['ativo'] = True
                print(
                    f'O restaurante {nome_restaurante} foi ativado com sucesso!')
            elif escolha.lower() == 'desativar':
                restaurante['ativo'] == False
                print(
                    'O restaurante {nome_restaurante} foi desativado com sucesso!')
            else:
                print('Opção inválida! O estado do restaurante não foi alterado.')

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''Essa função é responsável por escolher as opções do menu'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            alterar_nome_restaurante()
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    '''Função principal por iniciar o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
