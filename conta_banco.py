"""conta bancaria po POO com heranças e decoradores @property (getter) @XXX.setter"""

class Conta:
    
    contador = 1000 #servirá p registar em sequencia o número das contas abertas
    def __init__(self,nome, sobrenome, saldo, limite):
        """retorna os dados do cliente"""
        
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__saldo = saldo
        self.__limite = limite
        self.__conta = Conta.contador
        Conta.contador += 1
        
    
    
    
cliente1 = Conta("marcelo", "souza", 1000, 3000)
