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
       reserva = int(input("Digite o codigo da reserva que deseja:"))
       for reserva in reservas:
           if reserva['Codigo_Reserva'] == reserva:
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

def ExcluiReserva(reservas):
    reserva = int(input("Digite o codigo da reserva que deseja excluir:"))
    for reserva in reservas:
        if reserva['Codigo_Reserva'] == reserva:
            reservas.remove(reserva)
            break
        else:
            print("Reserva não encontrada!")
            

               
               



