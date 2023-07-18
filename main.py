"""Module for interacting with Web3."""
import json

from web3 import Web3


def main() -> None:
    """Execute the main process."""

    with open("private/creds.json", "r", encoding="utf8") as file:
        creds = json.load(file)

    alchemy_key = creds["alchemy_key"]
    # wallet_addr = creds["wallet_addr"]
    # transaction_id = creds["transaction_id"]

    alchemy_url = f"https://eth-goerli.g.alchemy.com/v2/{alchemy_key}"
    w3_client = Web3(Web3.HTTPProvider(alchemy_url))

    # Print if web3 is successfully connected
    print(w3_client.is_connected())

    # Get the latest block number
    latest_block = w3_client.eth.block_number
    print(latest_block)

    # Get the balance of an account
    # balance = w3_client.eth.get_balance(wallet_addr)
    # print(balance)

    # Get the information of a transaction
    # tx = w3_client.eth.get_transaction(transaction_id)
    # print(tx)


if __name__ == "__main__":
    main()
