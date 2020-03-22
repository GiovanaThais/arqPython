import os.path
while True:
    menu = int(input("   [1] Novo contato\n[2] Ver contatos\n[3] Apagar agenda\n[4] Sair \n"))
    if menu == 1:
        erro = 0
        nome = str(input("Nome: "))
        email = str(input("Email: "))
        tel= str(input("Telefone: "))
        site = str(input("Site: "))
        twitter = str(input("Twitter: "))
        facebook = str(input("Facebook: "))
       
        if '@' not in email:
            print("Email inválido!")
            erro += 1

        if len(tel) < 8:
            print("Telefone inválido!")
            erro += 1

        if 'www.' not in site:
            print("Site inválido!")
            erro += 1

        if erro == 0:
            arq_agenda = open('agenda.txt', 'a')
            arq_agenda.write(f'Nome: {nome}')
            arq_agenda.write(f'Email: {email}')
            arq_agenda.write(f'Telefone: {tel}')
            arq_agenda.write(f'Site: {site}')
            arq_agenda.write(f'Twitter: {twitter}')
            arq_agenda.write(f'Facebook: {facebook}\n\n')
            arq_agenda.close()

    elif menu == 2:
        if os.path.exists('agenda.txt') == False:
            arq_agenda = open('agenda1.txt', 'w')
        arq_agenda = open('agenda.txt', 'r')
        linha = arq_agenda.read()
        print(linha)
        arq_agenda.close()

    elif menu == 3:
        arq_agenda = open('agenda.txt', 'w')
        arq_agenda.close()

    else:
        break