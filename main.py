import os
from gerencia_clientes.pessoa_fisica.cadastro import cadastro_fisica


# os.system('cls')



# Condição para escolher se é cliente fisico ou juridico
while True:
    print('Tipo de cliente: [1] Pessoa física [2] Pessoa juridica')
    print()
    cliente = input('Tipo cliente....................................: ')
    
    if cliente != '1' and cliente != '2':
        print('Digite 1 para pessoa física ou 2 para pessoa juridica')
        continue

    else:
        if cliente == '1':
            cadastro_fisica()
        else:
            cliente = "Pessoa Juridica"
         
    
        
    break