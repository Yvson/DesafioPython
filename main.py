from src.api.binance_api import BinanceAPI




def main():
    connection = BinanceAPI()
    connection.start()




if __name__ == '__main__':
    main()

