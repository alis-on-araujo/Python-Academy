def valida_senha(senha):

    especiais = ['?', '!', '@', '#', '$', '%', '&', '*']

    count_especiais = 0
    prev_char = ''

    for char in senha:

        if char in especiais:

            if char != prev_char:
                count_especiais += 1
            prev_char = char

    if count_especiais < 2 or len(senha) < 8:
        return False
    
    for i in range(len(senha) - 1):

        if senha[i] == senha[i + 1]:
            return False
        
    return True