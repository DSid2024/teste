#entradas do usuário para definição das variáveis
"""Considere que a aplicação solicite ao usuário 
o tempo (em anos) que ele fuma,
o valor atual do maço e
a quantidade média de maços que ele fuma por dia (todos os dados podem ser fracionários).
A partir dessas informações, efetuaremos o cálculo do montante gasto por ele e o que ele poderia ter comprado com esse dinheiro."""

tempo_fumando = float(input("Há quanto tempo você fuma? A resposta deve ser em anos; com frações, se o caso, separadas por ponto. "))
maços_dia = float(input("Quanto você fuma por dia, em média? A resposta deve ser em equivalência a maços de cigarro; com frações, se o caso, separadas por ponto. "))
preço_maço = float(input("Qual o valor atual do maço de cigarro da marca que que você consome? A resposta deve ser em Reais, com centavos separados de Reais por ponto, se o caso: "))

#fórmulas matemáticas sobre variáveis
total_cigarros = tempo_fumando * 365.25 * maços_dia #fórmula matemática para obtenção do total de cigarros fumados no período
montante = total_cigarros * preço_maço #fórmula matemática para obtenção do montante gasto comcigarros fumados no período

#estruturas condicionais para tomada de decisão
"""REFERÊNCIA 
Usaremos o seguinte critério para as mensagens:

Se ele gastou abaixo de 20 mil, exibir a mensagem:
“Com o valor R$ <montante>, você poderia ter dado entrada em um carro.”

Se ele gastou entre 20 e 50 mil, exibir a mensagem: ok.
“Com o valor R$ <montante>, você poderia ter comprado um carro popular usado.”

Se ele gastou acima de 50 mil, exibir a mensagem:
“Com o valor R$ <montante>, você poderia ter comprado um carro zero.”

Para resolver esta Atividade, utilize OBRIGATORIAMENTE as estruturas de decisão (Se Simples, composto ou encadeado)

"""
if 0 < montante < 20000:  
    mensagem = "dado entrada em um carro"
elif 20000 <= montante <= 50000:
    mensagem = "comprado um carro popular usado"
elif montante > 50000:
    mensagem = "comprado um carro zero"
else:
    print("Pelo menos um dos valores digitados em uma das três perguntas foi zero ou número negativo. O programa será encerrado ")

print(f"Com o valor R$ {montante:.2f}, você poderia ter {mensagem}.")

"""não há tratamento de exceções, loops, funções, métodos especiais etc; em respeito ao conteúdo ministrado na fase 1, portanto não
foi possível tratar o caso de o usuário inserir caracteres não-numéricos ou vírgula por exemplo""" 