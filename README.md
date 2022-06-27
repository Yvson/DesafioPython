# Desafio Técnico - Desenvolvedor Python Jr.
Este projeto é resultado da solução de um desafio para construir um script que apresenta em tempo real informações e a cotação do par de criptomoedas `BTC-USDT` através de dados fornecidos pela [Binance](https://www.binance.com/en/binance-api) em sua API pública com a ajuda do pacote [Binance Connector Python](https://github.com/binance/binance-connector-python).


## Desafio
Disponibilizar através da execução de um _script_ python informações em tempo real sobre o par de criptomoedas `BTC-USDT`, incluindo a sua cotação. A apresentação dos valores pode ser feita no próprio terminal/console, não há necessidade da criação de uma interface gráfica.


## Entrega
- Conexão com a API da Binance através do encapsulamento do pacote `binance-connector` - CONCLUÍDO
- Atualização e exibição no terminal em tempo real das informações obtidas através do _stream_ de dados fornecidos pela API da Binance - CONCLUÍDO
- Testes unitários da classe _BinanceAPI_ e da função _format_datetime_ com pytest - CONCLUÍDO

## Instalação
```
git clone https://github.com/Yvson/DesafioPython.git
cd DesafioPython
pip install -r requirements.txt
```

## Execução
```
python main.py
```

## Versão do Python
- 3.10.4

## Sistema Operacional
Linux - Pop!_OS

## Exemplo
```
Event type: 24hrTicker
Event time: 27/06/2022 - 10:23:27
Symbol: BTCUSDT
Price change: -168.27000000
Price change percent: -0.787
Weighted average price: 21247.48622286
First trade(F)-1 price (first trade before the 24hr rolling window): 21393.44000000
Last price: 21225.17000000
Last quantity: 0.00356000
Best bid price: 21225.16000000
Best bid quantity: 5.64744000
Best ask price: 21225.17000000
Best ask quantity: 0.18505000
Open price: 21393.44000000
High price: 21539.85000000
Low price: 20926.01000000
Total traded base asset volume: 53938.99838000
Total traded quote asset volume: 1146068124.95408200
Statistics open time: 26/06/2022 - 10:23:27
Statistics close time: 27/06/2022 - 10:23:27
First trade ID: 1425802148
Last trade Id: 1426682444
Total number of trades: 880297

Press CRTL + C to STOP Data Stream.
```