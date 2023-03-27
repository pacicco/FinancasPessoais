from _datetime import datetime


data = datetime.now()

class Despesa:
    def __init__(self, categoria, valor, descricao=""):
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao
        self.data = datetime.now()


class FinancasPessoais:
    def __init__(self, saldo_inicial):
        self.transacoes = []
        self.saldo_atual = saldo_inicial
        self.despesas = []
        self.investimentos = []
        self.metas = []

    def deposito(self, valor):
        self.saldo_atual += valor
        self.transacoes.append((datetime.datetime.now(), valor))

    def adicionar_despesa(self, categoria, descricao, data, valor):
        self.despesas.append((categoria, descricao, datetime.now(), valor))
        self.saldo_atual -= valor

        # Adicionar investimentos
    def adicionar_investimento(self, categoria, descricao, objetivo, valor):
        self.investimentos.append((categoria, descricao, objetivo, datetime.now(), valor))
        self.saldo_atual -= valor

    def definir_meta(self, objetivo, valor_meta):
        self.metas[objetivo] = valor_meta

    def imprimir_despesas(self):
        for despesa in self.despesas:
            print(f"{despesa[2]}: {despesa[0]} - {despesa[1]} - R${despesa[3]:.2f}")


        # Imprimir investimentos
    def imprimir_investimentos(self):
        for investimento in self.investimentos:
            print(f"{investimento[3]}: {investimento[0]} - {investimento[1]} ({investimento[2]}) - R${investimento[4]:.2f}")


    def imprimir_saldo_atual(self):
        print(f"Saldo atual: R${self.saldo_atual:.2f}")

# Exemplo de uso:
fp = FinancasPessoais(5000)


# Adicionar despesas
supermercado = Despesa("Supermercado", "Compras da semana", 200.50)
contas = Despesa("Contas", 1000, "Pagamento de contas")
transporte = Despesa("Transporte", 150, "Uber")
restaurantes = Despesa("Restaurantes", 120, "Jantar com amigos")
roupas = Despesa("Roupas", 350, "Roupas novas")
casa = Despesa("Gastos com casa", 500, "Manutenção")
carro = Despesa("Gastos com carro", 300, "Manutenção")



fp.adicionar_despesa("Supermercado", "Compras da semana", datetime.now(), 200.50)
#fp.adicionar_despesa(contas)
#fp.adicionar_despesa(transporte)
#fp.adicionar_despesa(restaurantes)
#fp.adicionar_despesa(roupas)
#fp.adicionar_despesa(casa)
#fp.adicionar_despesa(carro)

# Imprimir despesas e saldo atual
fp.imprimir_despesas()
fp.imprimir_saldo_atual()

#Adicionar investimentos
fp.adicionar_investimento("Investimentos", "Investimento em ações", "Viagem", 5000.00)

#Adicionar metas e objetivos
fp.definir_meta("Viagem", 10000.00)

