#Caio Reibnitz Willemann     25200394
#Projeto final - Sistema de venda de passagens de ônibus
from Modelagem import Onibus,Usuario,Passageiro
import random
from time import sleep

def imprimeRecebendo(): #função puramente estética
    print('Recebendo pagamento',end='') ; sleep(0.4)
    print('.',end='') ; sleep(1)
    print('.',end='') ; sleep(1)
    print('.',end='') ; sleep(1)
    print('.',end='') ; sleep(1)
    print('.',end='') ; sleep(1)
    print('.',end='') ; sleep(1)
    print("\nAgradecemos a preferência. Até breve e boa viagem!")

def gerarCPF(): #gera "cpf" (sequência de números aleatória, não deve ser válido como cpf)
    cpf=[str(random.randint(0,9)) for _ in range(11)]
    cpf=''.join(cpf)
    return cpf

def gerarPessoasFake(itinerario):
    repnomes=["Alice", "Bernardo", "Cecília", "Daniel", "Eduarda", "Felipe", "Guilherme", "Heloísa", "Isabela", "João", "Karina", "Lucas", "Mariana", "Nicolas", "Olivia", "Pablo", "Chloe", "Rafael", "Sofia", "Thiago", "Ursula", "Vicente", "Yasmin", "Zoe", "André", "Beatriz", "Cauã", "Débora", "Emanuel", "Fernanda", "Gabriel", "Henrique", "Irene", "Júlia", "Carla", "Leandro", "Monique", "Natália", "Otávio", "Paula", "Quintino", "Rodrigo", "Sandra", "Tiago", "Ulisses", "Viviane", "Linda", "Xuxa", "Yara"]
    lugares=list(int(x) for x in range(1,41))
    listaviajantes=[]
    cidades=itinerario.getTrajeto()
    for _ in range(30):
        pessoa=Usuario('','')
        nome=random.choice(repnomes)
        pessoa.setNome(nome)
        cpf=gerarCPF()
        if len(allusers)>0:
            foi=0
            falhou=0
            while foi==0:
                for outros in allusers:
                    if outros.getId()==cpf:
                        falhou=1
                if falhou==1:
                    cpf=gerarCPF()
                else:
                    foi=1
        pessoa.setId(cpf)
        allusers.append(pessoa)
        
        viajante=Passageiro(nome,cpf,linhas.index(itinerario),'','','','')
        viajante.setEmbarque(random.choice(cidades[:-1]))
        contador=cidades.index(viajante.embarque)+1
        viajante.setCreditos(random.randint(1,len(cidades)-contador))
        viajante.setAssento(random.choice(lugares))
        viajante.setValorPago(32.25*viajante.getCreditos())
        allpassangers.append(viajante)
        
        lugares.remove(viajante.getAssento())
        repnomes.remove(nome)
        listaviajantes.append(viajante)
    
    itinerario.setPassageiros(listaviajantes)

def verificaAssentosOcupados(selecBus,selecEmbarq,selecDesemb): #foi separado como função para ser chamado novamente no processo de alterar detalhes da compra.
    mostrarassentos=selecBus.getAssentos()
    trajeto=selecBus.getTrajeto()
    assentosocupados=[]
    for individuo in selecBus.getPassageiros(): #percorre a lista de passageiros (lista de objetos Passageiro) da instância de Onibus selecionada.

        #comparar a posição do embarque do indivíduo na lista de cidades do itinerário com a posição da cidade de embarque selecionada.
        if trajeto.index(individuo.getEmbarque())<selecEmbarq: #significa que o indivíduo embarca ANTES do usuário realizando a compra.
            
            #somar o index da cidade de embarque do indivíduo com a quantidade de créditos para descobrir em qual cidade irá desembarcar, e fazer as comparações necessariás.
            if (trajeto.index(individuo.getEmbarque())+individuo.getCreditos())<=selecEmbarq: #significa que o indivíduo irá desembarcar antes ou junto do embarque do usuário realizando a compra.
                #LIVRE
                acusado=''
            else: #significa que o indivíduo irá desembarcar depois do embarque do usuário realizando a compra
                #OCUPADO
                acusado=individuo.getAssento()
        
        elif trajeto.index(individuo.getEmbarque())>selecEmbarq: #significa que o indivíduo embarca DEPOIS do usuário realizando a compra
            
            if trajeto.index(individuo.getEmbarque())>=selecDesemb: #analisa se o embarque do indivíduo é depois ou na mesma cidade que o desembarque do usuário realizando a compra
                #LIVRE
                acusado=''
            else: #significa que o indivíduo (que já possuí passagem comprada) embarca durante o trajeto que o usuário deseja realizar
                #OCUPADO
                acusado=individuo.getAssento()
        
        else: #significa que o indivíduo embarca junto do usuário realizando a compra. a preferência é de quem já comprou a passagem
            #OCUPADO
            acusado=individuo.getAssento()
        
        if acusado!='': #Se achou um indivíduo em conflito com a seleção do usuário, seu assento é acusado e recebe '--', indicando que está ocupado
            assentosocupados.append(acusado)
            for fileira in range(10):
                for banco in mostrarassentos[fileira]:
                    if banco==acusado:
                        mostrarassentos[fileira][mostrarassentos[fileira].index(banco)]='--'
    
    print(f'[{" Frente":9}]',end=' ')
    for fileira in mostrarassentos:
        print()
        for banco in fileira:
            print(f"{banco:02}",end=' ')
    return assentosocupados

def pesquisaCPF():
    aux=True
    print("\n-----Pesquisa por CPF-----\nPara voltar, digite 'voltar'")
    while aux: #verificar se o cpf contém apenas números
        login=input("Por favor, digite o CPF cadastrado: ")
        if login.isdigit():
            aux=False
        elif login=='voltar':
            aux=False
            return 0
        else:
            print("Apenas números são aceitos, tente novamente.")
    
    achouuser=False
    for cadastrado in allusers:
        if login==cadastrado.getId():
            achouuser=True
            cliente=cadastrado
    
    if achouuser:
        for passageiro in allpassangers:
            if passageiro.getId()==cliente.getId():
                cliente=passageiro
        print(f"\n-----Bem vindo(a) de volta, {cliente.getNome()}!-----")
        return cliente
    
    else:
        print("\nCPF não cadastrado.")
        return 0

#main
allusers=[] #Segura todas as instâncias de Usuario.
allpassangers=[] #Segura todas as instâncias de Passageiro.
linhas=[] #Segura todas as instâncias de Onibus.

#criando as linhas de onibus
itinerarios=[['Criciuma','Tubarao','Imbituba','Florianopolis','Tijucas','Itapema','Balneario Camboriu','Itajai','Blumenau'],['Navegantes','São Francisco do Sul','Joinville','Jaragua do Sul','São Bento do Sul','Mafra',]]
itinerarios.insert(1,itinerarios[0][::-1])
itinerarios.insert(3,itinerarios[2][::-1])
for i in range(len(itinerarios)):
    busao=Onibus('','','','')
    busao.setIdentificador(str(f"{itinerarios[i][0]}-->{itinerarios[i][-1]}"))
    busao.setTrajeto(itinerarios[i])
    assentos=[]
    contador=1
    for _ in range(10): #criação de matriz dos assentos
        fileira=[]
        for _ in range(4):
            fileira.append(contador) #todas as posições da matriz dos assentos da instância do Onibus recebem uma instância de Poltrona
            contador+=1
            if len(fileira)==4:
                assentos.append(fileira) 
    busao.setAssentos(assentos)
    linhas.append(busao)
    gerarPessoasFake(busao)
    busao=0

#interação com o usuário
while True:
    print("\n","= "*30,"\n{:^60}\n".format("Viação CTC"),"= "*30)
    print("\n-----MENU-----\n1-Comprar passagem.\n2-Consultar itinerários disponíveis.\n3-Já tenho passagem comprada!\n4-Administração\n5-Sair.")
    escolhamenu=input()
    match escolhamenu:
        case '1': #PROCESSO DE COMPRA DE PASSAGEM
            print("\n-----Comprar passagem-----")
            nome=''
            while nome=='':
                print("Por favor, informe.\n1-Já tenho cadastro.\n2-Não possuo cadastro.\n3-Voltar")
                escolhacadastro=input()
                if escolhacadastro=='1':  #acessa os dados do usuário, se presente em allusers
                    cliente=pesquisaCPF()
                    if isinstance(cliente,Passageiro):
                        print("Você já possuí uma passagem comprada para hoje. Não é possível comprar passagens para outros dias.\nSe deseja alterar sua passagem, acesse a opção 'Já tenho passagem comprada!' no menu inicial")
                        cliente=0
                        nome=0
                    elif isinstance(cliente,Usuario):
                        nome=cliente.getNome()
                        cpf=cliente.getId()
                    else:
                        cliente=0
                        nome=0
                        
                elif escolhacadastro=='2':  #cadastra um novo usuário em allusers
                    print("\n-----Seja bem vindo! Cadastre-se-----")
                    nome=input("Por favor, digite o primeiro nome do viajante:").capitalize()
                    while ' ' in nome:
                        nome=input("Por favor, digite APENAS o PRIMEIRO nome do viajante:").capitalize()
                    
                    aux=True
                    while aux:
                        cpf=input("Por favor, digite o cpf do viajante: ")
                        while len(str(cpf))!=11:
                            cpf=input("Números de CPF precisam ter 11 dígitos. Tente novamente: ")
                        for users in allusers:
                            aux=False
                            cliente=1
                            if cpf==users.getId():
                                cliente=0
                                print("\nCPF já cadastrado.")
                    
                    if cliente!=0:
                        allusers.append(Usuario(nome,cpf))
                        print(f"\nUsuário '{nome}' portador do CPF número {cpf} cadastrado!")
                    
                elif escolhacadastro=='3':
                    cliente=0
                    nome=0
                    
                else:
                    print("Seleção indisponível.")
                    input("Pressione 'Enter' para voltar ao menu e tentar novamente.")
            
            if cliente!=0:
                print("\nSelecione o itinerário desejado.") #seleção de itinerário
                contador=0
                for it in linhas:
                    contador+=1
                    print(f"{contador}-{it.identificador}")
                selecItine=int(input())-1
                while not selecItine in range(4):
                    selecItine=int(input("Seleção indisponível. Tente novamente: "))-1
                
                selecBus=linhas[selecItine] #selecBus recebe a instância de Onibus referente ao itinerário escolhido para facilitar o resto do processo de compra
                
                contador=0
                print(f"\nItinerário '{selecItine+1}' escolhido! Selecione a cidade que deseja embarcar.") #seleção de embarque
                for parada in selecBus.getTrajeto()[:-1]:
                    contador+=1
                    print(f"{contador}-{parada}")
                selecEmbarq=int(input())-1
                while not selecEmbarq in range(len(selecBus.getTrajeto())-1):
                    selecEmbarq=int(input("Seleção indisponível. Tente novamente: "))-1
                
                contador=selecEmbarq+2
                print(f"\nEmbarque em {itinerarios[selecItine][selecEmbarq]}. Selecione a cidade que deseja desembarcar.") #seleção de desembarque
                for parada in selecBus.getTrajeto():
                    if selecBus.getTrajeto().index(parada)>selecEmbarq:
                        print(f"{contador}-{parada}")
                        contador+=1
                selecDesemb=int(input())-1
                while not selecDesemb in range(selecEmbarq+1,len(selecBus.getTrajeto())):
                    selecDesemb=int(input("Seleção indisponível. Tente novamente: "))-1
                
                print(f"\nTrajeto selecionado: {itinerarios[selecItine][selecEmbarq]} --> {itinerarios[selecItine][selecDesemb]}.\n-----Selecione seu assento.-----\n-> Atenção, assentos ocupados exibem '--' em sua posição.")
                assentosocupados=verificaAssentosOcupados(selecBus,selecEmbarq,selecDesemb) #mostrar matriz de assentos e obter lista com os números dos assentos ocupados
                
                selecAssento=int(input("\nPor favor, informe sua seleção de assento: ")) #seleção de assento
                while selecAssento in assentosocupados or selecAssento not in range(1,41):
                    selecAssento=int(input("\nAssento indisponível, por favor, escolha outro assento: "))
                
                creditos=selecDesemb-selecEmbarq #calculo de créditos do usuário realizando a compra
                
                confirma=0
                while confirma==0:
                    print("\n-----Detalhes do pedido-----")
                    print(f"Comprador(a): {nome}     CPF: {cpf}")
                    print(f"Itinerário escolhido: {selecBus.getIdentificador()}")
                    print(f"Seu embarque: {itinerarios[selecItine][selecEmbarq]}")
                    print(f"Seu desembarque: {itinerarios[selecItine][selecDesemb]}")
                    print(f"Seu assento: {selecAssento:02}")
                    print(f"Valor total a pagar (calculado por trecho): R${32.25*creditos}")
                    pagamento=input("\nQual a forma de pagamento?\n1-Cartão\n2-Boleto\n3-Pix (5% de desconto)\n\nPara cancelar a compra, digite 'cancelar'\n").lower()
                    if pagamento=='3':
                        valor=30.64*creditos
                        print(f"Seu novo total é de: R${valor}")
                        imprimeRecebendo()
                        input("Pressione 'Enter' para voltar ao menu principal.")
                        confirma=1
                    elif pagamento in ['1','2']:
                        valor=32.25*creditos
                        imprimeRecebendo()
                        input("Pressione 'Enter' para voltar ao menu principal.")
                        confirma=1
                    elif pagamento=='cancelar':
                        confirma=''
                    else:
                        print("Opção não disponível")
                if confirma==1:
                    selecEmbarq=itinerarios[selecItine][selecEmbarq] #transforma selecEmbarq de número (posição da cidade escolhida na lista) para o nome da cidade escolhida
                    cliente=Passageiro(nome,cpf,selecItine,selecAssento,selecEmbarq,creditos,valor)
                    allpassangers.append(cliente)
                    selecBus.adicionarPassageiro(cliente)
                else:
                    print("Compra cancelada. Volte sempre!")
            
        case '2': #consulta pronta
            print("\n-----Consulta de itinerários-----")
            contador=1
            for itin in linhas:
                print(f"Itinerário {contador}:")
                for cidade in itin.trajeto:
                    if cidade!=itin.trajeto[-1]:
                        print(f" {cidade} ",end='-->')
                    else:
                        print(cidade)
                        print()
                contador+=1
            input("Pressione 'Enter' para voltar ao menu principal.")
            
        case '3':
            print("\n-----'Já tenho passagem comprada!'-----")
            cliente=pesquisaCPF()
            aux=True
            if isinstance(cliente,Passageiro):
                nome=cliente.getNome()
                cpf=cliente.getId()
            elif isinstance(cliente,Usuario):
                nome=cliente.getNome()
                cpf=''
            else:
                aux=False
                cpf=''
                
                
                
            if cpf!='':
                selecBus=linhas[cliente.getItinerario()]
                trajeto=selecBus.getTrajeto()
                selecEmbarq=int(trajeto.index(cliente.getEmbarque()))
            
            while aux==True:
                print(f"\nO que deseja fazer?\n1-Consultar detalhes da passagem\n2-Alterar seu assento\n3-Exluir passagem\n4-Voltar")
                selec=input()
                match selec:
                    case '1':
                        if cpf!='':
                            identificador=selecBus.getIdentificador()
                            selecDesemb=trajeto[selecEmbarq+cliente.getCreditos()]
                            cliente.consulta(identificador,selecDesemb)
                        else:
                            cliente.consulta('','')
                    
                    case '2':
                        if cpf!='':
                            selecDesemb=int(selecEmbarq+cliente.getCreditos())
                            print("\nAtenção, caso queira alterar embarque/desembarque, exclua sua passagem e comece o processo de compra novamente.")
                            
                            assentoantigo=cliente.getAssento()
                            cliente.setAssento('')
                            assentosocupados=verificaAssentosOcupados(selecBus,selecEmbarq,selecDesemb) #mostrar matriz de assentos e obter lista com os números dos assentos ocupados
                            selecAssento=int(input("\nPor favor, informe sua seleção de assento: ")) #seleção de assento
                            
                            while selecAssento in assentosocupados or selecAssento not in range(1,41):
                                selecAssento=int(input("\nAssento indisponível, por favor, escolha outro assento: "))
                            cliente.setAssento(selecAssento)
                            assentonovo=cliente.getAssento()
                            print(f"Alteração de assento: {assentoantigo} --> {assentonovo}. Concluída com sucesso!")
                        else:
                            print("\nVocê não possuí passagens ativas no momento. Impossível alterar assento.")
                    
                    case '3':
                        if cpf!='':
                            print("\n-----Excluir passagem?-----\n1-Confirma\n2-Cancela")
                            confirma=input()
                            if confirma=='1':
                                selecBus.removerPassageiro(cliente)
                                allpassangers.remove(cliente)
                                cliente=0
                                aux=False
                                print("Passagem excluída com sucesso. O valor será ressarcido para sua conta!")
                        else:
                            print("\nVocê não possuí passagens ativas no momento. Impossível excluir.")
                    
                    case '4':
                        aux=False
                        
                    case _:
                        print("Entrada não reconhecida, tente novamente.")
        case '4':
            aux=True
            while aux==True:
                print("\n-----Área administrativa-----\n1-Visualizar usuários cadastrados\n2-Visualizar clientes com passagem comprada\n3-Exluir passagem\n4-Excluir cadastro de usuário\n5-Voltar")
                selec=input()
                flag=False
                sinal=True
                if selec in ['3','4']:
                    flag=True
                    print("\n-----Pesquisa por CPF-----\nPara voltar, digite 'voltar'")
                    while flag: #verificar se o cpf contém apenas números
                        login=input("Por favor, digite o CPF cadastrado: ")
                        if login.isdigit():
                            login=int(login)
                            sinal=True
                        elif login=='voltar':
                            sinal=False
                            flag=False
                        else:
                            print("Apenas números são aceitos, tente novamente.")
                            sinal=False
                    
                        if sinal:
                            achouuser=False
                            for cadastrado in allusers:
                                if login==int(cadastrado.getId()):
                                    achouuser=True
                                    cliente=cadastrado
                            
                            if achouuser:
                                for passageiro in allpassangers:
                                    if int(passageiro.getId())==int(cliente.getId()):
                                        cliente=passageiro
                                print(f"\n-----Alterando dados para {cliente.getId()}-----")
                                flag=False
                            
                            else:
                                print("\nCPF não cadastrado.")
                                sinal=False
                                flag=False
                                
                if not flag and sinal:
                    match selec:
                        
                        case '1':
                            todos=[['------------','-----------']]
                            for user in allusers:
                                tabelar=[user.getNome(),user.getId()]
                                todos.append(tabelar)
                            print("\n{:<12} {:<11}".format("Nome", "CPF"))
                            for a in todos:
                                nome,cpf=a
                                print("{:<12} {:<11}".format(nome, cpf))
                        
                        case '2':
                            print("\nInsira o número do itinerário para vizualizar seus clientes, ou digite 'todos' para vizualizar os clientes de todos os itinerários")
                            contador=0
                            for it in linhas:
                                contador+=1
                                print(f"{contador}-{it.identificador}")
                            qst=input()
                            if qst=='todos':
                                todos=[['-----------','-----------','----------','-------','-------------------','--------','----------',]]
                                total=0
                                for passageiro in allpassangers:
                                    tabelar=[passageiro.getNome(),passageiro.getId(),passageiro.getItinerario()+1,passageiro.getAssento(),passageiro.getEmbarque(),passageiro.getCreditos(),passageiro.getValorPago()]
                                    todos.append(tabelar)
                                    total+=passageiro.getValorPago()
                                print("\n{:<11} {:<12} {:<12} {:<10} {:<21} {:<10} {:<10}".format("Nome", "CPF", "Itinerário", "Assento", "Embarque", "Créditos", "Valor pago"))
                                for a in todos:
                                    nome,cpf,itin,assen,embarq,cred,valor=a
                                    print("{:<11} {:<12} {:<12} {:<10} {:<21} {:<10} {:<10}".format(nome,cpf,itin,assen,embarq,cred,valor))
                                
                                print(f"\nReceita obtida de todos os clientes: R${total} ----------------------------------------")
                                
                            elif qst in ['1','2','3','4']:
                                todos=[['-----------','-----------','----------','-------','-------------------','--------','----------',]]
                                total=0
                                for passageiro in allpassangers:
                                    if passageiro.getItinerario()+1==int(qst):
                                        tabelar=[passageiro.getNome(),passageiro.getId(),passageiro.getItinerario()+1,passageiro.getAssento(),passageiro.getEmbarque(),passageiro.getCreditos(),passageiro.getValorPago()]
                                        todos.append(tabelar)
                                        total+=passageiro.getValorPago()
                                print("\n{:<11} {:<12} {:<12} {:<10} {:<21} {:<10} {:<10}".format("Nome", "CPF", "Itinerário", "Assento", "Embarque", "Créditos", "Valor pago"))
                                for a in todos:
                                    nome,cpf,itin,assen,embarq,cred,valor=a
                                    print("{:<11} {:<12} {:<12} {:<10} {:<21} {:<10} {:<10}".format(nome,cpf,itin,assen,embarq,cred,valor))
                                
                                print(f"\nReceita obtida dos clientes do itinerário {qst}: R${total} ---------------------------------")
                                
                            else:
                                print("Entrada não reconhecida")
                                
                        case '3': #exluir passagem
                            print(f"Excluindo passagem do usuário {cliente.getNome()}.")
                            if isinstance(cliente,Passageiro):
                                selecBus=linhas[cliente.getItinerario()]
                                print("\nConfirma? S/N ")
                                selec=input().upper()
                                if selec=='S':
                                    allpassangers.remove(cliente)
                                    selecBus.removerPassageiro(cliente)
                                    print("\nSolicitação finalizada com sucesso.")
                            else:
                                print("O CPF informado não possuí passagem ativa.")
                        
                        case '4': #excluir usuário
                            print("Atenção, caso o usuário tenha passagem comprada, elá também será excluída.\nConfirma exclusão do cadastro? S/N ")
                            selec=input().upper()
                            if selec=='S':
                                for u in allusers:
                                    if str(login)==u.getId():
                                        temp=u
                                        allusers.remove(temp)
                                if isinstance(cliente,Passageiro):
                                    selecBus=linhas[cliente.getItinerario()]
                                    allpassangers.remove(cliente)
                                    selecBus.removerPassageiro(cliente)
                                cliente=0
                                print("\nSolicitação finalizada com sucesso.")
                        
                        case '5':
                            aux=False
                        
                        case _:
                            print("Entrada não reconhecida, tente novamente.")
        case '5':
            break
        
        case _:
            print("Entrada não reconhecida, tente novamente.")