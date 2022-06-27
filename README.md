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