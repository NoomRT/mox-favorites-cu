from script.deploy import deploy_favorites

def test_starting_values():
    favorites_contract = deploy_favorites()
    assert favorites_contract.retrieve() == 77

def test_can_change_values():
    favorites_contract = deploy_favorites()
    favorites_contract.store(42)
    assert favorites_contract.retrieve() == 42