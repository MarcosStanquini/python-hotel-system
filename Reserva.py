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
                    nomes_ocupantes = input("Digite o nome dos ocupantes!")

                    reserva = {
                        'Codigo_Reserva': codigo_reserva,
                        'CPF': cpf,
                        'Codigo': codigo,
                        'Data_entrada': data_entrada,
                        'Data_saida': data_saida,
                        'Nomes_Ocupantes': nomes_ocupantes
                    }

                    reservas.append(reserva)
                    print("Reserva cadastrada com sucesso!")


                


        reserva = {
        'Codigo_Reserva': codigo_reserva,
        'CPF': cpf,
        'Codigo': codigo,
        'Data_entrada': data_entrada,
        'Data_saida': data_saida,
        'Nomes_Ocupantes': nomes_ocupantes
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
    for reserva in reservas:
        print(reservas)

