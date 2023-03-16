from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.brine_wrapper.client import Client  # noqa: E402
from src.brine_wrapper.bin.blockchain_utils import sign_msg  # noqa: E402
import requests

load_dotenv()
PRIVATE_KEY = os.environ['PRIVATE_KEY']
ETH_ADDRESS = os.environ['ETH_ADDRESS']


def main():

    client = Client()

    # trades = client.get_recent_trades('btcusdt')
    # orderbook = client.get_orderbook('btcusdt')
    # print(trades['message'])
    # print(orderbook['message'])
    login = client.complete_login(ETH_ADDRESS, PRIVATE_KEY)
    client.set_token('fdsfaf')
    print(client.get_profile_info())
    print(client.get_balance())
    print(client.get_profit_and_loss())
    print(login['message'])
    # trades = client.list_trades()
    # print(trades['message'])
    # nonce = Client.create_order_nonce('btcusdt', 'market', 29580.51, 'buy', 0.0001)

    # msg_hash = Client.sign_msg_hash(nonce['payload'], private_key)
    # print(Client.create_new_order(msg_hash))
    try:
        client.create_complete_order(
            'btcusdt', 'market', 29580.51, 'buy', 0.00001, PRIVATE_KEY)['message']
        # print(client.list_trades())
    except requests.exceptions.HTTPError as exc:
        print(exc.response.json())


main()
