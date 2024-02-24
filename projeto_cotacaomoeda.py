import requests
import json
#Projeto API cotacao de moedas
#1: Importar as bibliotecas necessarias e depois fazer a requisicao da API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#print(cotacoes) -- o print retorna o codigo 200, o que indica que tudo ocorreu pereitamente
#Proximo passo e converter as cotacoes para json, tendo entao varias bibliotecas...
cotacoes = cotacoes.json()
#print(cotacoes)
print("Bem-vindo ao conversor de moedas em tempo real!")
print("O valor da cotacao e atualizado a cada 30 segundos.")
print("Opcoes disponiveis: USD[Dolar - Real]")
print("Opcoes disponiveis: EUR[Euro - Real]")
print("Opcoes disponiveis: BTC[Bitcoin - Real]")
print("Para encerrar digite 'SAIR'")

#vou criar variaveis apenas com o valor do bid das moedas e depois fazer uma fstring para colocar na resposta...
#VALORES DOLAR
valor_dolar = (cotacoes["USDBRL"]["bid"])
valor_dolar = float(valor_dolar)
valor_dolar = "{:.2f}".format(valor_dolar)
dia_hora_dolar = cotacoes["USDBRL"]["create_date"]
#print(valor_dolar)

#VALORES EURO
valor_euro = (cotacoes["EURBRL"]["bid"])
valor_euro = float(valor_euro)
valor_euro = "{:.2f}".format(valor_euro)
dia_hora_euro = cotacoes["EURBRL"]["create_date"]
#VALOR BITCOIN
valor_bitcoin = (cotacoes["BTCBRL"]["bid"])
valor_bitcoin = float(valor_bitcoin)
valor_bitcoin = "{:.2f}".format(valor_bitcoin)
dia_hora_bitcoin = cotacoes["BTCBRL"]["create_date"]
#Fazer um loop infinito com while true e se precisar quebrar / encerrar a api usar o break // Fazer validacoes de entrada...
while True: 
    opcao_usuario = input("Digite a moeda desejada:")
    opcao_usuario_upper = opcao_usuario.upper()
    if opcao_usuario_upper == "USD":
        print(f"O valor do dolar e R${valor_dolar} ultima att: {dia_hora_dolar}")
    elif opcao_usuario_upper == "EUR":
        print(f"O valor do euro e R${valor_euro} ultima att: {dia_hora_euro}")
    elif opcao_usuario_upper == "BTC":
        print(f"O valor do bitcoin e R${valor_bitcoin} ultima att: {dia_hora_bitcoin}")
    elif opcao_usuario_upper == "SAIR":
        break    
    else:
        print("Favor digitar a moeda desejada seguindo o modelo de exemplo")            
#FIM