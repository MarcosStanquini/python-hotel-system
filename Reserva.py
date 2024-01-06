from datetime import datetime
from Cliente import *
from Apartamento import *

def AdicionarReserva(clientes, apartamentos, reservas):
    codigo_reserva = int(input("Digite o código da reserva:"))
    if VerificaCodigoReserva(codigo_reserva, reservas):
        print("Código de Reserva já cadastrado!")
    else:
        cpf = input("Digite o CPF do cliente:")
        if VerificaClienteAssociado(cpf, reservas):
            return  # Encerrar a função se o cliente já tiver uma reserva associada

        cliente_encontrado = None
        for cliente in clientes:
            if cliente['CPF'] == cpf:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            print("Cliente não encontrado!")
        else:
            codigo = int(input("Digite o Código do apartamento:"))
            if VerificaApartamentoAssociado(codigo, reservas):
                return  # Encerrar a função se o apartamento já estiver em uso

            apartamento_encontrado = None
            for apartamento in apartamentos:
                if apartamento['Codigo'] == codigo:
                    apartamento_encontrado = apartamento
                    break

            if apartamento_encontrado is None:
                print("O apartamento não foi encontrado!")
            else:
                data_entrada = input("Digite a Data de entrada:")
                data_saida = input("Digite a Data de saída:")
                try:
                    data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y")
                    data_saida = datetime.strptime(data_saida, "%d/%m/%Y")
                except ValueError:
                    print("Formato de data inválido. Certifique-se de usar o formato DD/MM/AAAA.")
                else:
                    for apartamento in apartamentos:
                        if apartamento['Codigo'] == codigo:
                            cont = 0
                            ocupantes = []
                            tamanho = apartamento['Numero_Pessoas']
                            while cont < tamanho:
                                cpf_cliente = input("Digite o CPF do ocupante (cliente): ")
                                if VerificaCpf(cpf_cliente, clientes):
                                    ocupantes.append([cliente['Nome'] for cliente in clientes if cliente['CPF'] == cpf_cliente][0])
                                    cont += 1
                                else:
                                    print("Cliente não encontrado. Por favor, insira um CPF válido.")

                            print("Nomes dos ocupantes:", ocupantes)
                            break
                    else:
                        print("Apartamento não encontrado.")

                    reserva = {
                        'Codigo_Reserva': codigo_reserva,
                        'CPF': cpf,
                        'Codigo': codigo,
                        'Data_entrada': data_entrada,
                        'Data_saida': data_saida,
                        'Nomes_Ocupantes': ocupantes
                    }

                    reservas.append(reserva)
                    print("Reserva cadastrada com sucesso!")


def VerificaCodigoReserva(codigo_reserva, reservas):
    for reserva in reservas:
        if reserva['Codigo_Reserva'] == codigo_reserva:
            return True
    return False
    
def VerificaClienteAssociado(cpf, reservas):
    for reserva in reservas:
        if reserva['CPF'] == cpf:
            print("Esse cliente já tem uma reserva associada!")
            return True
    return False


def VerificaApartamentoAssociado(codigo, reservas):
    for reserva in reservas:
        if reserva['Codigo'] == codigo:
            print("Esse apartamento já está em uso!")
            return True
    return False


def ListarReservas(reservas):
    if not reservas:
        print("Não há reservas no momento!")
        return
    else:
        for reserva in reservas:
            print("\nCódigo da Reserva:", reserva['Codigo_Reserva'])
            print("CPF do Cliente:", reserva['CPF'])
            print("Código do Apartamento:", reserva['Codigo'])
            print("Data de Entrada:", reserva['Data_entrada'])
            print("Data de Saída:", reserva['Data_saida'])
            print("Nomes dos Ocupantes:", ', '.join(reserva['Nomes_Ocupantes']))
            print("-" * 30)

def ProcuraReserva(reservas):
       codigo_reserva = int(input("Digite o codigo da reserva que deseja:"))
       for reserva in reservas:
           if reserva['Codigo_Reserva'] == codigo_reserva:
                print("\nCódigo da Reserva:", reserva['Codigo_Reserva'])
                print("CPF do Cliente:", reserva['CPF'])
                print("Código do Apartamento:", reserva['Codigo'])
                print("Data de Entrada:", reserva['Data_entrada'])
                print("Data de Saída:", reserva['Data_saida'])
                print("Nomes dos Ocupantes:", ', '.join(reserva['Nomes_Ocupantes']))
                print("-" * 30)
                break
           else:
               print("Reserva não encontrada!")


def AlterarReserva(clientes, apartamentos, reservas):
    codigo_reserva = int(input("Digite o código da reserva que deseja alterar:"))
    for reserva in reservas:
        if reserva['Codigo_Reserva'] == codigo_reserva:
            novo_codigo_reserva = int(input("Digite o novo código da reserva:"))

            if VerificaCodigoReserva(novo_codigo_reserva, reservas):
                print("Novo código de Reserva já cadastrado!")
            else:
                cpf = input("Digite o CPF do cliente:")

                if VerificaClienteAssociado(cpf, reservas):
                    print("CPF já cadastrado em outra reserva. Alteração não permitida.")
                    return

                cliente_encontrado = next((cliente for cliente in clientes if cliente['CPF'] == cpf), None)

                if cliente_encontrado is None:
                    print("Cliente não encontrado!")
                else:
                    novo_codigo_apartamento = int(input("Digite o novo Código do apartamento:"))

                    if VerificaApartamentoAssociado(novo_codigo_apartamento, reservas):
                        print("Novo Código do apartamento já está em uso. Alteração não permitida.")
                        return

                    apartamento_encontrado = next((ap for ap in apartamentos if ap['Codigo'] == novo_codigo_apartamento), None)

                    if apartamento_encontrado is None:
                        print("O novo apartamento não foi encontrado!")
                    else:
                        nova_data_entrada = input("Digite a nova Data de entrada:")
                        nova_data_saida = input("Digite a nova Data de saída:")
                        try:
                            nova_data_entrada = datetime.strptime(nova_data_entrada, "%d/%m/%Y")
                            nova_data_saida = datetime.strptime(nova_data_saida, "%d/%m/%Y")
                        except ValueError:
                            print("Formato de data inválido. Certifique-se de usar o formato DD/MM/AAAA.")
                        else:
                            cont = 0
                            novos_ocupantes = []
                            tamanho = apartamento_encontrado['Numero_Pessoas']
                            while cont < tamanho:
                                cpf_cliente = input("Digite o CPF do novo ocupante (cliente): ")
                                if VerificaCpf(cpf_cliente, clientes):
                                    novos_ocupantes.append([cliente['Nome'] for cliente in clientes if cliente['CPF'] == cpf_cliente][0])
                                    cont += 1
                                else:
                                    print("Cliente não encontrado. Por favor, insira um CPF válido.")

                            # Atualizar os dados da reserva
                            reserva['Codigo_Reserva'] = novo_codigo_reserva
                            reserva['CPF'] = cpf
                            reserva['Codigo'] = novo_codigo_apartamento
                            reserva['Data_entrada'] = nova_data_entrada
                            reserva['Data_saida'] = nova_data_saida
                            reserva['Nomes_Ocupantes'] = novos_ocupantes

                            print("Reserva alterada com sucesso!")
                            return

    print("Reserva não encontrada para alteração.")

               



def ExcluiReserva(reservas):
    codigo_reserva = int(input("Digite o codigo da reserva que deseja excluir:"))
    for reserva in reservas:
        if reserva['Codigo_Reserva'] == codigo_reserva:
            reservas.remove(reserva)
            print("Reserva excluida com sucesso!")
            break
        else:
            print("Reserva não encontrada!")
            

def Relatorio(reservas):
    if not reservas:
        print("Não há reservas para gerar relatório.")
        return

    try:
        data_inicio = input("Digite a Data de início (DD/MM/AAAA): ")
        data_fim = input("Digite a Data de fim (DD/MM/AAAA): ")

        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

        reservas_no_periodo = [reserva for reserva in reservas if data_inicio <= reserva['Data_entrada'] <= data_fim]
        
        if not reservas_no_periodo:
            print(f"\nNão há reservas no período de {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}.")
        else:
            print(f"\nReservas no período de {data_inicio.strftime('%d/%m/%Y')} a {data_fim.strftime('%d/%m/%Y')}:")
            for reserva in reservas_no_periodo:
                print("\nCódigo da Reserva:", reserva['Codigo_Reserva'])
                print("CPF do Cliente:", reserva['CPF'])
                print("Código do Apartamento:", reserva['Codigo'])
                print("Data de Entrada:", reserva['Data_entrada'].strftime('%d/%m/%Y'))
                print("Data de Saída:", reserva['Data_saida'].strftime('%d/%m/%Y'))
                print("Nomes dos Ocupantes:", ', '.join(reserva['Nomes_Ocupantes']))
                print("-" * 30)

    except ValueError:
        print("Formato de data inválido. Certifique-se de usar o formato DD/MM/AAAA.")


