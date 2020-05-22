import os.path

def registrar():
    erros = 0
    print("-"*40)

    nome = str(input("Nome: "))
    email = input('Email: ')
    tel = input("Telefone: ")
    facebook = input("Facebook: ")
    linkedin = input('Linkedin: ')
    data = input('Data de Nascimento: ')

    print("-"*40)

    if erros == 0:
        try:
            arq_reg = open('listaAgenda.txt', 'a')
            arq_reg.write(f'\n Nome:  {nome}')
            arq_reg.write(f"\n Email: {email}")
            arq_reg.write(f'\n Telefone: {tel}')
            arq_reg.write(f"\n Facebook: {facebook}")
            arq_reg.write(f'\n Linkedin: {linkedin}')
            arq_reg.write(f'\n Data de Nascimento: {data}\n\n')
            arq_reg.close()
            print("Salvo com sucesso!")
        except FileNotFoundError:
            print("Não foi possivel salvar o registro!")

def listar():
    try:
        arq_reg = open('listaAgenda.txt', 'r')
        texto = arq_reg.read()
        print(texto)
        return texto
        arq_reg.close()
    except FileNotFoundError: 
        print('Nenhum registro encontrado')