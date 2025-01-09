import json
import os
import sys

# Classe para definir as informações de cada cliente
class Cliente:
    def __init__(self, nome, idade, telefone, qtd_dias):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.qtd_dias = qtd_dias

    def to_dict(self):
        return {
            'nome': self.nome,
            'idade': self.idade,
            'telefone': self.telefone,
            'qtd_dias': self.qtd_dias
        }


# Função para cadastrar um novo cliente
def cadastrar_cliente():
    # Coleta informações do cliente pelo terminal
    nome = input("Digite o nome do cliente: ")
    idade = int(input("Digite a idade do cliente: "))
    telefone = int(input("Digite o telefone do cliente: "))
    qtd_dias = int(input('Digite a quantidade de dias que você ficará com o carro: '))

    # Verifica se a idade é maior ou igual a 18
    if idade < 18:
        print("Desculpe, você precisa ter 18 anos ou mais para alugar um veículo.")
        sys.exit()  # Encerra o programa imediatamente

    
    # Cria um objeto Cliente com as informações inseridas
    cliente = Cliente(nome, idade, telefone, qtd_dias)
    print("\nCliente cadastrado com sucesso!")
    return cliente  # Retorna o cliente cadastrado

# Classe para definir as características de cada veículo
# Classe para definir as características de cada veículo
class Veiculo:
    def __init__(self, modelo, marca, ano, tipo, valor_diaria, disponivel=True):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.tipo = tipo  # Exemplo: SUV, Sedan, Hatch
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel  # Indica se o veículo está disponível para locação (padrão: True)
    
    def to_dict(self):
        return {
            'modelo': self.modelo,
            'marca': self.marca,
            'ano': self.ano,
            'tipo': self.tipo,
            'valor_diaria': self.valor_diaria,
            'disponivel': self.disponivel
        }
    
    # Método para exibir todos os detalhes do veículo
    def exibir_detalhes(self):
        disponibilidade = "Disponível" if self.disponivel else "Indisponível"
        print(f"Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.ano}, Tipo: {self.tipo}, Valor Diária: R${self.valor_diaria}, Status: {disponibilidade}")


# Subclasse SUV
class SUV(Veiculo):
    def __init__(self, modelo, marca, ano, valor_diaria, tracao_4x4=True, disponivel=True):
        super().__init__(modelo, marca, ano, "SUV", valor_diaria, disponivel)
        self.tracao_4x4 = tracao_4x4

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Tração 4x4: {'Sim' if self.tracao_4x4 else 'Não'}")


# Subclasse Sedan
class Sedan(Veiculo):
    def __init__(self, modelo, marca, ano, valor_diaria, espaco_bagagem="Médio", disponivel=True):
        super().__init__(modelo, marca, ano, "Sedan", valor_diaria, disponivel)
        self.espaco_bagagem = espaco_bagagem

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Espaço de bagagem: {self.espaco_bagagem}")


# Lista de veículos disponíveis na locadora
veiculos_disponiveis = [
    Sedan("Civic", "Honda", 2020, 150),
    Sedan("Corolla", "Toyota", 2019, 140),
    SUV("Renegade", "Jeep", 2021, 180, tracao_4x4=True),
    Veiculo("HB20", "Hyundai", 2018, "Hatch", 120),
    SUV("Creta", "Hyundai", 2022, 200, tracao_4x4=False),  # Agora estamos criando instâncias de SUV, que esperam o parâmetro tracao_4x4
    Sedan("Accord", "Honda", 2021, 160),
    Sedan("Fusion", "Ford", 2018, 145),
    SUV("Compass", "Jeep", 2020, 190, tracao_4x4=True),
    SUV("Evoque", "Land Rover", 2022, 250, tracao_4x4=True),
    Veiculo("Onix", "Chevrolet", 2021, "Hatch", 110),
    Veiculo("Gol", "Volkswagen", 2019, "Hatch", 100),
    SUV("Tucson", "Hyundai", 2019, 170, tracao_4x4=False),
    SUV("Outlander", "Mitsubishi", 2021, 220, tracao_4x4=True),
    Sedan("Passat", "Volkswagen", 2020, 150),
    Veiculo("Kwid", "Renault", 2022, "Hatch", 95)
]

# Função para o cliente escolher um critério de busca para o veículo
def escolher_criterio():
    print("\nEscolha o critério de busca:")
    print("1 - Modelo")
    print("2 - Marca")
    print("3 - Ano")
    print("4 - Tipo")
    
    # Criamos uma lista que se o numero escolhido nao estiver dentro dos permitidos, ele vai pedir para refazer a escolha
    escolhas = [1, 2, 3, 4]
    while True:
        escolha = int(input("Digite o número do critério de sua escolha: "))# Cliente escolhe um critério digitando o número correspondente
        if escolha in escolhas:
            return escolha  # Retorna o critério selecionado
        else:
            print('Digite uma opção válida')
            continue #caso seja escolhido um valor inválido, vai voltar para o primeiro if

# Função para listar as opções com base no critério escolhido pelo cliente
def listar_opcoes_por_criterio(criterio):
    opcoes = set()  # Usamos um conjunto (set) para garantir que as opções sejam únicas

    # Povoamos o conjunto `opcoes` com os valores únicos do critério escolhido
    for veiculo in veiculos_disponiveis:
        if criterio == 1:
            opcoes.add(veiculo.modelo)
        elif criterio == 2:
            opcoes.add(veiculo.marca)
        elif criterio == 3:
            opcoes.add(veiculo.ano)
        elif criterio == 4:
            opcoes.add(veiculo.tipo)

    # Convertemos o conjunto para uma lista para exibir em ordem e permitir seleção pelo cliente
    opcoes = list(opcoes)

    # Verificamos se há opções disponíveis
    if not opcoes:
        print("Nenhuma opção disponível para o critério escolhido.")
        return None

    print("\nEscolha uma das opções disponíveis:")
    for i, opcao in enumerate(opcoes):
        print(f"{i + 1} - {opcao}")

    # Entrada do usuário para escolher uma opção válida
    while True:
        try:
            escolha = int(input("Digite o número da opção escolhida: "))
            # Verifica se a escolha está dentro do intervalo de opções
            if 1 <= escolha <= len(opcoes):
                return opcoes[escolha - 1]  # Retorna o valor da opção selecionada
            else:
                print(f"Por favor, escolha um número entre 1 e {len(opcoes)}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número correspondente a uma das opções.")

def buscar_veiculo_por_criterio(criterio, valor_escolhido):
    print(f"\nVeículos disponíveis para '{valor_escolhido}':")
    opcoes_encontradas = []

    # Pergunta sobre tração apenas se o critério for "SUV"
    if criterio == 4 and valor_escolhido == "SUV":
        resposta_tracao = input("Você deseja uma SUV com tração 4x4? (s/n): ").strip().lower()

    for veiculo in veiculos_disponiveis:
        if ((criterio == 1 and veiculo.modelo == valor_escolhido) or
            (criterio == 2 and veiculo.marca == valor_escolhido) or
            (criterio == 3 and veiculo.ano == valor_escolhido) or
            (criterio == 4 and veiculo.tipo == valor_escolhido)):

            if criterio == 4 and veiculo.tipo == "SUV":
                if resposta_tracao == 's' and isinstance(veiculo, SUV) and veiculo.tracao_4x4:
                    opcoes_encontradas.append(veiculo)
                elif resposta_tracao == 'n' and isinstance(veiculo, SUV) and not veiculo.tracao_4x4:
                    opcoes_encontradas.append(veiculo)
            else:
                opcoes_encontradas.append(veiculo)

    if not opcoes_encontradas:
        print("Nenhum veículo encontrado com esses critérios.")
        return None

    # Exibindo as opções encontradas para o usuário selecionar
    print("\nEscolha um veículo da lista:")
    for i, veiculo in enumerate(opcoes_encontradas):
        print(f"{i + 1} - {veiculo.modelo}, {veiculo.marca}, Ano: {veiculo.ano}, Tipo: {veiculo.tipo}, Valor Diária: R${veiculo.valor_diaria}")

    while True:
        try:
            escolha = int(input("Digite o número do veículo escolhido: "))
            if 1 <= escolha <= len(opcoes_encontradas):
                return opcoes_encontradas[escolha - 1]
            else:
                print(f"Por favor, escolha um número entre 1 e {len(opcoes_encontradas)}.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número correspondente a uma das opções.")
def exibir_relatorio_final(cliente, veiculo):
    print("\n--- Relatório Final ---")
    print(f"Cliente: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"Telefone: {cliente.telefone}")
    print(f"Quantidade de dias com o carro: {cliente.qtd_dias}")
    print("Detalhes do Veículo Escolhido:")
    veiculo.exibir_detalhes()
    print("-----------------------")

     # Criando o relatório final como um dicionário
    relatorio = {
        'cliente': cliente.to_dict(),
        'veiculo': veiculo.to_dict()
    }

   # Caminho do arquivo onde os relatórios serão salvos
    caminho_arquivo = 'relatorios.json'

    # Verificando se o arquivo já existe
    if os.path.exists(caminho_arquivo):
        try:
            # Abrindo o arquivo existente e lendo os dados
            with open(caminho_arquivo, 'r') as arquivo:
                relatorios = json.load(arquivo)  # Carrega os relatórios existentes
        except Exception as e:
            print(f"Erro ao carregar o arquivo existente: {e}")
            relatorios = []  # Em caso de erro, cria uma lista vazia
    else:
        relatorios = []  # Caso o arquivo não exista, cria uma lista vazia

    # Adicionando o novo relatório à lista de relatórios
    relatorios.append(relatorio)

    # Salvando todos os relatórios no arquivo
    try:
        with open(caminho_arquivo, 'w') as arquivo:
            json.dump(relatorios, arquivo, indent=4)  # Sobrescreve o arquivo com a lista de relatórios
        print("Relatório final salvo em 'relatorios.json'.")
    except Exception as e:
        print(f"Erro ao salvar o relatório: {e}")


# Fluxo principal do programa
cliente = cadastrar_cliente()  # Realiza o cadastro do cliente
criterio = escolher_criterio()  # Cliente escolhe um critério de busca
valor_escolhido = listar_opcoes_por_criterio(criterio)  # Cliente escolhe um valor com base no critério
veiculo_escolhido = buscar_veiculo_por_criterio(criterio, valor_escolhido)  # Busca e retorna o veículo escolhido

if veiculo_escolhido:
    exibir_relatorio_final(cliente, veiculo_escolhido)  # Exibe o relatório final
else:
    print("Não foi possível gerar o relatório, pois nenhum veículo foi selecionado.")