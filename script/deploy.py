from src import favorites
from moccasin.boa_tools import VyperContract

def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"Starting number is: {starting_number}")

    favorites_contract.store(77)
    ending_number: int = favorites_contract.retrieve()
    print(f"Ending number is {ending_number}")

    return favorites_contract

def moccasin_main() -> VyperContract:
    return deploy_favorites()