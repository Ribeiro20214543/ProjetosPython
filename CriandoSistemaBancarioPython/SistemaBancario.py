import datetime

class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.data_atual = datetime.date.today()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: +{valor:.2f}')  # Adiciona a operação de depósito ao extrato
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if self.data_atual == datetime.date.today():
            if self.saques_diarios < 3 and valor <= 500:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.extrato.append(f'Saque: -{valor:.2f}')  # Adiciona a operação de saque ao extrato
                    self.saques_diarios += 1
                else:
                    print("Saldo insuficiente!")
            else:
                print("Limite diário de saques atingido ou valor de saque inválido!")
        else:
            self.data_atual = datetime.date.today()
            self.saques_diarios = 0
            self.sacar(valor)  # Reinicia o contador de saques diários e realiza o saque novamente

    def ver_extrato(self):
        if len(self.extrato) == 0:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for operacao in self.extrato:
                print(operacao)
            print(f"Saldo atual: R$ {self.saldo:.2f}")

# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")

# Testando o sistema
banco = Banco()

while True:
    exibir_menu()
    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depositar: "))
        banco.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para sacar: "))
        banco.sacar(valor)
    elif opcao == "3":
        banco.ver_extrato()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")

