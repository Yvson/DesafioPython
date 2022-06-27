from os import system as consoleCommand
import random
from src.api.utils.format_date import format_datetime
import threading
import signal
import os
import logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient
from binance.lib.utils import config_logging


# This adds logging features to messages received from the websocket
config_logging(logging, logging.DEBUG)

# Creates an exit event
exit_event = threading.Event()


# Signal activated after clicking CTRL + C
def signal_handler(signum, frame):
    exit_event.set()

# Creating Signal
signal.signal(signal.SIGINT, signal_handler)



class BinanceAPI:
    """
    Class responsible for starting the connection with the Binance Websocket
    and displaying the message received on the terminal.
    """

    def __init__(self) -> None:
        self.ws_client = WebsocketClient()
        self.symbol = 'btcusdt'
        self.id = random.randrange(10000)
        self.callback = self.message_handler
        self.last_received_message = ''

    
    def start(self):

        self.ws_client.start()
        self.ws_client.ticker(
            symbol=self.symbol,
            id=self.id,
            callback=self.callback
        )

    def message_handler(self, message):
        # Update last_received_message
        self.last_received_message = message

        # Stop Websocket data stream
        if exit_event.is_set():
            self.ws_client.stop()

        # Console Cleaning command
        consoleCommand('clear') if os.name == 'posix' else consoleCommand('cls')
        
        if not 'result' in message:
            print(f'Event type: {message["e"]}')
            print(f'Event time: {format_datetime(message["E"])}')
            print(f'Symbol: {message["s"]}')
            print(f'Price change: {message["p"]}')
            print(f'Price change percent: {message["P"]}')
            print(f'Weighted average price: {message["w"]}')
            print(f'First trade(F)-1 price (first trade before the 24hr rolling window): {message["x"]}')
            print(f'Last price: {message["c"]}')
            print(f'Last quantity: {message["Q"]}')
            print(f'Best bid price: {message["b"]}')
            print(f'Best bid quantity: {message["B"]}')
            print(f'Best ask price: {message["a"]}')
            print(f'Best ask quantity: {message["A"]}')
            print(f'Open price: {message["o"]}')
            print(f'High price: {message["h"]}')
            print(f'Low price: {message["l"]}')
            print(f'Total traded base asset volume: {message["v"]}')
            print(f'Total traded quote asset volume: {message["q"]}')
            print(f'Statistics open time: {format_datetime(message["O"])}')
            print(f'Statistics close time: {format_datetime(message["C"])}')
            print(f'First trade ID: {message["F"]}')
            print(f'Last trade Id: {message["L"]}')
            print(f'Total number of trades: {message["n"]}')
            print(f'')
            print(f'Press CRTL + C to STOP Data Stream.')


    def stop(self):
        self.ws_client.stop()
        






