import os.path
import Agenda as a


while True :
    print('-'*40)
    print('''Menu :
    [1]-Registrar Dados
    [2]-Listar Registros
    [3]-Sair''')
    opc=(int(input('opção desejada: ')))
    if opc==3:
        break
    elif opc==1:
        a.registrar()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif opc==2:
        a.listar()
        print('Pressione enter para voltar')
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    
    print('-'*40)