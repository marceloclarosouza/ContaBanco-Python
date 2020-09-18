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

    @property#usando o decorador para acessar (GET) uma variável privada fora da classe
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter#usando o decorador para alterar (SET) uma variável privada fora da classe
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def titular(self):
        return f'Cliente: {self.__nome} {self.__sobrenome}, Conta: {self.__conta}'

    def saldo_c(self):
        return f'O Saldo do Sr(a) {self.__nome} {self.__sobrenome} é de R$ {self.__saldo}'

    def limite_c(self):
        return f'O limite do Sr(a) {self.__nome} {self.__sobrenome} é de R$ {self.__limite}'

    def sacar(self, valor):
        self.__saldo -= valor
        return f'Valor sacado: {valor}\tSeu saldo atual é de {self.__saldo}'

    def depositar(self, valor):
        self.__saldo += valor
        return f'Valor depositado: {valor}\tSeu saldo atual é de {self.__saldo}'

    def transferir(self, valor, destino):
        """transfere um valor da conta A para a conta B"""
        self.__saldo -= valor
        destino.__saldo += valor##adiciona o valor a conta de destino



cliente1 = Conta("marcelo", "souza", 1000, 3000)
cliente2 = Conta("Michael", "Kiske", 9999, 9999)
print(cliente1.limite_c())
print(cliente1.saldo_c())
print(cliente1.titular())
print(cliente1.sacar(200))
print(cliente1.depositar(500))

cliente1.transferir(100, cliente2)
print(cliente2.saldo_c())

soma = cliente1.saldo + cliente2.saldo ##por causa dos decoradores usamos cliente.saldo no lugar de cliente.saldo()
print(soma)

cliente1.limite = 5000##alterar o limite do cliente1 pelo decorador @limite.setter
print(cliente1.limite_c())
