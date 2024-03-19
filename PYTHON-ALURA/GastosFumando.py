def funcao_input(mensagem, tipo): 
    """
    Função para tratamento de exceções

    Parâmetros:
    mensagem: Entrada do usuário, pura, sem estilização de vírgula
    tipo: referência para um tipo de dado, passado para um argumento, para uso por uma função; usado para indicar se a entrada deve ser convertida para float
    """
    while True: # iterações em quantidade indefinida exigem uso de loop por meio de while, em detrimento do loop for
        try: #método para tratamento de exceções
            entrada = input(mensagem).replace(',', '.')  # Replace substitui ponto por vírgula
            valor = tipo(entrada)
            if valor <= 0: # tratar entradas negativas ou zeradas, que não fazem sentido nesse contexto
                raise ValueError("Por favor, insira um valor positivo.") # uso do método try para tratar erros decorrentes de entradas inválidas, erro de valor
            return valor #retorna variável valor, para uso posterior
        except ValueError as e: # uso do alias para simplificar chamada de função
            print(f"Entrada inválida. {e}")

# Pedindo entrada de dados ao usuário, com tratamento de exceções; e armazena-os em uma lista
dados_usuario = [
    funcao_input("Há quanto tempo você fuma? A resposta deve ser em anos, com frações, se o caso: ", float),
    funcao_input("Quantos maços de cigarro por dia você fuma? ", float),
    funcao_input("Qual o valor atual do maço de cigarros que você fuma? A resposta deve ser em Reais, com centavos, se o caso: ", float)
]

def calcular_economia(dados_usuario):
    """
    Calcula o montante gasto com cigarros e retorna uma mensagem detalhada sobre o que poderia ter sido adquirido com essa quantia,
    incluindo informações sobre o hábito de fumar do usuário.

    Parâmetros:
    dados_usuario: Lista contendo o tempo fumando em anos, quantidade média de maços por dia e o preço por maço.
    """
    tempo_fumando_anos, cigarros_por_dia, preco_maco = dados_usuario #declara de onde sairão os valores para as variáveis; da lista dados_usuario, no caso
    dias_no_ano = 365.25  # Contabilizando anos bissextos, conforme calendário gregoriano, arredondado para cima
    total_cigarros = tempo_fumando_anos * dias_no_ano * cigarros_por_dia #fórmula matemática para obtenção do total de cigarros fumados no período
    montante = total_cigarros * preco_maco #fórmula matemática para obtenção do montante gasto comcigarros fumados no período

    # fluxo com estruturas condicionais, para decisão
    if montante < 20000:  
        objeto = "dado entrada em um carro"
    elif 20000 <= montante <= 50000:
        objeto = "comprado um carro popular usado"
    else:
        objeto = "comprado um carro zero"

    return (f"Com o valor R$ {montante:.2f}, você poderia ter {objeto}.")

# Por fim, dada a estrutura em funções, necessária a chamada da função, com os dados obtidos; e imprimir a mensagem customizada com as entradas
mensagem = calcular_economia(dados_usuario)
print(mensagem)
