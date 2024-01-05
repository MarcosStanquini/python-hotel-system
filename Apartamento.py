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
        else:
            return False