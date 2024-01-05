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

def ListarClientes(clientes):
    if not clientes:
        print("Não há clientes cadastrados.")
        return

    print("Lista de Clientes:")
    for cliente in clientes:
        print(f"Nome: {cliente['Nome']}")
        print(f"CPF: {cliente['CPF']}")
        print(f"Endereço: {cliente['Endereco']}")
        print(f"Cidade: {cliente['Cidade']}")
        print(f"Telefone: {cliente['Telefone']}")
        print(f"Data de Nascimento: {cliente['Data_nascimento']}")
        print("-" * 30) 

def ProcuraCliente(clientes):
    cpf = input("Digite o CPF do cliente que deja pesquisar:")
    for cliente in clientes:
        if cliente['CPF'] == cpf:
            print(f"Nome: {cliente['Nome']}")
            print(f"CPF: {cliente['CPF']}")
            print(f"Endereço: {cliente['Endereco']}")
            print(f"Cidade: {cliente['Cidade']}")
            print(f"Telefone: {cliente['Telefone']}")
            print(f"Data de Nascimento: {cliente['Data_nascimento']}")
            print("-" * 30) 
        else:
            print("Esse cliente não existe!")

def AlterarCliente(clientes):
    cpf = input("Digite o CPF do cliente que deseja alterar:")
    for cliente in clientes:
            if VerificaCpf(cpf, clientes):
                cliente['CPF'] = cpf = input("Digite o novo CPF do cliente:")
                cliente['Nome'] = input("Digite o novo Nome do cliente:")
                cliente['Endereco'] = input("Digite o novo Endereco do cliente:")
                cliente['Cidade'] = input("Digite o novo Cidade do cliente:")
                cliente['Telefone'] = input("Digite o novo Telefone do cliente:")
                cliente['Data_nascimento'] = input("Digite a nova Data de Nascimento do cliente:")
                print("Cliente alterado com sucesso!")
            else:
                print("Cliente não encontrado.")

def ExcluirCliente(clientes):
    cpf = input("Digite o CPF do cliente que deseja excluir:")
    for cliente in clientes:
        if VerificaCpf(cpf, clientes):
            clientes.remove(cliente)
            print("Cliente excluido com sucesso!")
            break
        else:
            print("Cliente não encontrado!")     
