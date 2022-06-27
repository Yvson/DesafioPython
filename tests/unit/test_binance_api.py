from src.api.binance_api import BinanceAPI
import pytest
import time




@pytest.fixture(scope='session')
def connection():
    return BinanceAPI()

def test_started_BinanceAPI(connection):
    """
    Tests if the thread has been started by checking the ident property.
    """
    connection.start()
    id_started = connection.ws_client.ident
    assert id_started != None

def test_message_received_BinanceAPI(connection):
    """
    Tests if the websocket is receiving messages from the stream.
    """
    time.sleep(5)
    last_message = connection.last_received_message
    assert last_message != ''

def test_validate_message_BinanceAPI(connection):
    """
    Tests if the message received is legitimate and has all parameters.
    """
    keys = ['e', 'E', 's', 'p', 'P', 'w', 'x', 'c', 'Q', 'b', 'B', 'a', 'A', 'o', 'h', 'l', 'v', 'q', 'O', 'C', 'F', 'L', 'n']
    for key in keys:
        if not key in connection.last_received_message:
            assert False
    assert True

def test_verify_coin_pair_BinanceAPI(connection):
    """
    Tests if the coin pair received is BTCUSDT.
    """
    pair_received = connection.last_received_message['s']
    assert pair_received == 'BTCUSDT'


def test_stoppage_BinanceAPI(connection):
    """
    Tests if the thread has been stopped by executing `is_alive` function.
    """
    connection.stop()
    time.sleep(1)
    connection_status = connection.ws_client.is_alive()
    assert connection_status == False


