from src import favorites
import time

def deploy_favorites():
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Starting number is: {starting_number}")

    favorites_contract.store(77)
    ending_number = favorites_contract.retrieve()
    print(f"Ending number is {ending_number}")
    time.sleep(5)
    return favorites_contract

def moccasin_main():
    deploy_favorites()