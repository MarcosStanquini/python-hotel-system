def AdicionaApartamento(apartamentos):
    codigo = int(input("Digite o codigo do Apartamento:"))
    if VerificaCodigo(codigo, apartamentos):
        print("Codigo existente!")
    else:    
        tipo = input("Escolha um tipo de apartamento: Standart, Luxo, SuperLuxo:").lower()
        if tipo != "standart" and tipo != "superluxo" and tipo != "luxo":
             print("Escolha um tipo de apartamento válido!")    
        else:    
             numero_pessoas = int(input("Digite a quantidade maxima de pessoas:"))
             valor_diaria = int(input("Qual o valor da diária?:"))

        apartamento = {
            'Codigo': codigo,
            'Tipo': tipo,
            'Numero_Pessoas': numero_pessoas,
            'Valor_Diaria': valor_diaria
}            
        apartamentos.append(apartamento)
        print("Apartamento adicionado com sucesso!")    


def VerificaCodigo(codigo, apartamentos):
    for apartamento in apartamentos:
        if apartamento['Codigo'] == codigo:
            return True
        return False

def ListarApartamentos(apartamentos):
    if not apartamentos:
        print("Não existem apartamentos cadastrados!")
    else:
        print("Lista de apartamentos:")
        for apartamento in apartamentos:
            print(f"Código: {apartamento['Codigo']}")
            print(f"Tipo: {apartamento['Tipo']}")
            print(f"Número de pessoas: {apartamento['Numero_Pessoas']}")
            print(f"Valor da diária: {apartamento['Valor_Diaria']}")
            print("-" * 30)

def ProcuraApartamento(apartamentos):
    codigo = int(input("Digite o codigo que deseja procurar:"))
    for apartamento in apartamentos:
        if apartamento['Codigo'] == codigo:
            print(f"Código: {apartamento['Codigo']}")
            print(f"Tipo: {apartamento['Tipo']}")
            print(f"Número de pessoas: {apartamento['Numero_Pessoas']}")
            print(f"Valor da diária: {apartamento['Valor_Diaria']}")
            print("-" * 30)
        else:
            print("Apartamento não existe!")

def AlterarApartamento(apartamentos):
    codigo = int(input("Digite o codigo que deseja alterar:"))
    for apartamento in apartamentos:
         if VerificaCodigo(codigo, apartamentos):
                apartamento['Codigo'] = int(input("Digite o novo código do apartamento:"))
                apartamento['Tipo'] = input("Escolha um outro tipo de apartamento: Standart, Luxo, SuperLuxo:").lower()
                apartamento['Numero_Pessoas'] = input("Digite o número de pessoas:")
                apartamento['Valor_Diaria'] = input("Digite o valor:")
                print("Apartamento alterado com sucesso!")
         else:
            print("Esse apartamento não existe!")     

def ExcluirApartamento(apartamentos):
    codigo = int(input("Digite o codigo que deseja excluir:"))
    for apartamento in apartamentos:
        if VerificaCodigo(codigo, apartamentos):
            apartamentos.remove(apartamento)
            print("Apartamento excluido com sucesso!")
            
        else:
            print("Código não encontrado!")    
        



            
            





