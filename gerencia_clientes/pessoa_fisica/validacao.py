def validar_cpf(cpf):
    while True:
        if not cpf.isdigit() or len(cpf) != 11:  
            print('CPF inválido!')
            cpf = input('CPF.............................................: ')
            continue
        else:
            break    
    return cpf

def validar_genero(genero):
    while True:
       
        if genero == 'M':
            genero = 'Masculino'
            break
        elif genero == 'F':
            genero = 'Feminino'
            break
        elif genero == 'O':
            genero = 'Outros'
            break
        else:
            print('invalido...') 
            genero = str(input('Gênero M - Masculino | F - Feminino | O - Outros: ')).upper() 
            continue    
    return genero  

def validar_cep(cep):
    
    while True:
        posicao = cep.find('-')
        if (not cep.isdigit) or len(cep) != 9 or posicao != 5:
            print('"CEP" invalido. Formato deve ser 00000-000')
            cep = input('CEP.......................: ')
            continue 
        else:
            break
    return cep

def validar_rua(rua):
    rua_lista = []

    if len(rua) == 0 or rua.isnumeric():
        print('Digite o nome da rua') 
    else:    
        rua_lista.append(rua)
        
    return rua

def validar_numero(numero):
    numero = [] 







    '''complemeto = str(input('Complemento: '))
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    uf = input('UF: ')
    data_nascimento = str(input('Data de nascimento: '))
    email = str(input('E-mail:'))'''