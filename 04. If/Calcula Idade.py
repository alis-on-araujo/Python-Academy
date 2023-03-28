def calcula_idade(dia_nasc, mes_nasc, ano_nasc, dia_data, mes_data, ano_data):

    idade = ano_data - ano_nasc
    
    if mes_data < mes_nasc or (mes_data == mes_nasc and dia_data < dia_nasc):
        idade -= 1
    return idade
