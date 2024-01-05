def AdicionaCliente(clientes):
    cpf = input("Digite o CPF do cliente:")
    if VerificaCpf(cpf, clientes):
        print("CPF já existente!")
    else:    
        nome = input("Digite o Nome do cliente:")
        endereco = input("Digite o Endereco do cliente:")
        cidade = input("Digite o Cidade do cliente:")
        telefone = input("Digite o Telefone do cliente:")
        data_nascimento = input("Digite o Data de Nascimento do cliente:")

        cliente = {
        'CPF': cpf,
        'Nome': nome,
        'Endereco': endereco,
        'Cidade': cidade,
        'Telefone': telefone,
        'Data_nascimento': data_nascimento
}
        clientes.append(cliente)
        print("Cliente adicionado com sucesso.")

        

def VerificaCpf(cpf, clientes):
    for cliente in clientes:
        if cliente['CPF'] == cpf:
            return True
        else:
            return False

def SubmenuCliente(clientes):
    while True:
        print("Submenu Cliente:")
        print("1 - Listar Todos os Clientes:")
        print("2 - Pesquisar um Cliente:")
        print("3 - Incluir um Cliente:")
        print("4 - Alterar um Cliente:")
        print("5 - Excluir um Cliente:")
        print("6 - Voltar ao Menu Principal")

        escolha_submenu = int(input("O que deseja fazer no Submenu de Clientes?"))
        
        if escolha_submenu == 1:
            print("Listar Todos os Clientes")
        elif escolha_submenu == 2:
            print("Pesquisar um Cliente")
        elif escolha_submenu == 3:
            print("Incluir um Cliente")
            AdicionaCliente(clientes)
        elif escolha_submenu == 4:
            print("Alterar um Cliente")
        elif escolha_submenu == 5:
            print("Excluir um Cliente")
        elif escolha_submenu == 6:
            print("Voltando ao Menu Principal...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
        
        

def Menu():
    lista_clientes = [] 
    while True:
        print("Bem Vindo ao Menu! - Menu Principal")
        print("1 - Submenu de Clientes")
        print("2 - Submenu de Apartamentos")
        print("3 - Submenu de Reserva de Apartamentos")
        print("4 - Relatório")
        print("5 - Sair")
        escolha = int(input("O que deseja fazer?:"))
        if escolha == 1:
            SubmenuCliente(lista_clientes)
        elif escolha == 2:
            print("Submenu de Apartamentos")
        elif escolha == 3:
            print("Submenu de Reserva de Apartamentos")
        elif escolha == 4:
            print("Relatório")
        elif escolha == 5:
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")



Menu()
