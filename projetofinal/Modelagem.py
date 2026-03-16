#Projeto final - Sistema de venda de passagens de ônibus

class Onibus():
    def __init__(self,identificador,trajeto,assentos,passageiros):
        self.identificador=identificador
        self.trajeto=trajeto #lista de todas as cidades do itinerário
        self.assentos=assentos #lista de poltronas
        self.passageiros=passageiros #lista de passageiros do onibus
        
    def setPassageiros(self,novopassageiros):
        self.passageiros=novopassageiros
        
    def adicionarPassageiro(self,passageiro):
        self.passageiros.append(passageiro)
        
    def removerPassageiro(self,passageiro):
        self.passageiros.remove(passageiro)
        
    def getPassageiros(self):
        return self.passageiros
    
    def setAssentos(self,listassentos):
        self.assentos=listassentos
    
    def getAssentos(self):
        return self.assentos
    
    def setTrajeto(self,novotrajeto):
        self.trajeto=novotrajeto
    
    def getTrajeto(self):
        return self.trajeto
    
    def setIdentificador(self,novoidentificador):
        self.identificador=novoidentificador
    
    def getIdentificador(self):
        return self.identificador
        
#=============================================================================================================================#

class Usuario(): #usar para ter uma base de dados
    def __init__(self,nome,cpf):
        self.nome=nome
        self.id=cpf
    
    def consulta(self,identificador,selecDesemb):
        print("\nO usuário não possuí passagens compradas.")
        print(f"Nome cadastrado: {self.nome}")
        print(f"CPF cadastrado: {self.id}")
        
    def setNome(self,novonome):
        self.nome=novonome
        
    def getNome(self):
        return self.nome
        
    def setId(self,novocpf):
        self.id=novocpf
        
    def getId(self):
        return self.id

#=============================================================================================================================#

class Passageiro(Usuario):
    def __init__(self,nome,cpf,itinerario,assento,embarque,creditos,valorpago):
        super().__init__(nome,cpf)
        self.itinerario=itinerario #guarda o itinerário (index da instância de Onibus da lista "linhas") da viagem que tem passagem comprada
        self.assento=assento
        self.embarque=embarque #cidade que irá embarcar
        self.creditos=creditos #número de cidades entre sua origem e seu destino
        self.valorpago=valorpago
        
    def consulta(self,identificador,selecDesemb):
        print(f"\nNome: {self.nome}     CPF: {self.id}")
        print(f"Itinerário escolhido: {identificador}")
        print(f"Seu embarque: {self.embarque}")
        print(f"Seu desembarque: {selecDesemb}")
        print(f"Seu assento: {self.assento}")
        print(f"Valor pago: R${self.valorpago}\n")
    
    def setAssento(self,novoassento):
        self.assento=novoassento
        
    def getAssento(self):
        return self.assento
        
    def setEmbarque(self,novoembarque):
        self.embarque=novoembarque
        
    def getEmbarque(self):
        return self.embarque
        
    def setCreditos(self,novocredito):
        self.creditos=novocredito
    
    def getCreditos(self):
        return self.creditos
    
    def setValorPago(self,novovalor):
        self.valorpago=novovalor
        
    def getValorPago(self):
        return self.valorpago
    
    def getItinerario(self):
        return self.itinerario
    
    def setId(self,novocpf):
        self.id=novocpf
        
    def getId(self):
        return self.id
