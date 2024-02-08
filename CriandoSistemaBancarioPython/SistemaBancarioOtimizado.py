import datetime

LIMIT_SAQUES_DIARIOS = 3
LIMIT_SAQUE = 500

class Conta:
    numero_conta_atual = 1

    def __init__(self, agencia, usuario):
        self.agencia = agencia
        self.numero_conta = Conta.numero_conta_atual
        Conta.numero_conta_atual += 1
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.data_atual = datetime.date.today()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: +{valor:.2f}')
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if self.data_atual == datetime.date.today():
            if self.saques_diarios < LIMIT_SAQUES_DIARIOS and valor <= LIMIT_SAQUE:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.extrato.append(f'Saque: -{valor:.2f}')
                    self.saques_diarios += 1
                else:
                    print("Saldo insuficiente!")
            else:
                print("Limite diário de saques atingido ou valor de saque inválido!")
        else:
            self.data_atual = datetime.date.today()
            self.saques_diarios = 0
            self.sacar(valor)

    def ver_extrato(self):
        if len(self.extrato) == 0:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for operacao in self.extrato:
                print(operacao)
            print(f"Saldo atual: R$ {self.saldo:.2f}")


class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, agencia):
        nova_conta = Conta(agencia, self)
        self.contas.append(nova_conta)
        return nova_conta


class Banco:
    def __init__(self):
        self.clientes = []

    def cadastrar_usuario(self, nome, data_nascimento, cpf, endereco):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                print("CPF já cadastrado. Não é possível cadastrar o usuário.")
                return

        novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.clientes.append(novo_usuario)
        print("Usuário cadastrado com sucesso.")

    def cadastrar_conta_bancaria(self, cpf, saldo_inicial=0):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                agencia = "0001"
                nova_conta = cliente.adicionar_conta(agencia)
                nova_conta.saldo = saldo_inicial
                print("Conta bancária cadastrada com sucesso.")
                return

        print("CPF não encontrado. Não é possível cadastrar a conta bancária.")
        
    def vincular_usuario_a_conta(self, cpf, numero_conta):
        # Procura o usuário com o CPF informado
        usuario = self.encontrar_usuario(cpf)
        if usuario:
            # Procura a conta com o número informado
            conta = self.encontrar_conta(numero_conta)
            if conta:
                if conta.usuario is None:
                    conta.usuario = usuario
                    print("Usuário vinculado à conta com sucesso.")
                else:
                    print("A conta já está vinculada a um usuário.")
            else:
                print("Conta não encontrada.")
        else:
            print("Usuário não encontrado.")

    def encontrar_usuario(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def encontrar_conta(self, numero_conta):
        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.numero_conta == numero_conta:
                    return conta
        return None

    def exibir_menu(self):
        print("\nMenu:")
        print("[1] Cadastrar Usuário")
        print("[2] Cadastrar Conta Bancária")
        print("[3] Depositar")
        print("[4] Sacar")
        print("[5] Extrato")
        print("[6] Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                nome = input("Digite o nome do usuário: ")
                data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
                cpf = input("Digite o CPF: ")
                endereco = input("Digite o endereço (logradouro, nro, bairro, cidade, estado): ")
                self.cadastrar_usuario(nome, data_nascimento, cpf, endereco)
            elif opcao == "2":
                cpf = input("Digite o CPF do usuário: ")
                saldo = float(input("Digite o saldo inicial: "))
                self.cadastrar_conta_bancaria(cpf, saldo)
                if cpf in [cliente.cpf for cliente in self.clientes]:
                    numero_conta = int(input("Digite o número da conta: "))
                    self.vincular_usuario_a_conta(cpf, numero_conta)
            elif opcao == "3":
                cpf = input("Digite o CPF do usuário: ")
                valor = float(input("Digite o valor para depositar: "))
                conta = self.encontrar_conta_bancaria(cpf)
                if conta:
                    conta.depositar(valor)
                else:
                    print("Conta bancária não encontrada.")
            elif opcao == "4":
                cpf = input("Digite o CPF do usuário: ")
                valor = float(input("Digite o valor para sacar: "))
                conta = self.encontrar_conta_bancaria(cpf)
                if conta:
                    conta.sacar(valor)
                else:
                    print("Conta bancária não encontrada.")
            elif opcao == "5":
                cpf = input("Digite o CPF do usuário: ")
                conta = self.encontrar_conta_bancaria(cpf)
                if conta:
                    conta.ver_extrato()
                else:
                    print("Conta bancária não encontrada.")
            elif opcao == "6":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

    def encontrar_conta_bancaria(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente.contas[-1]  # Retorna a última conta adicionada
        return None


banco = Banco()
banco.executar()