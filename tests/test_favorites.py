from script.deploy import deploy_favorites

def test_starting_values():
    favorites_contract = deploy_favorites()
    assert favorites_contract.retrieve() == 77

def test_can_change_values():
    # Arrange
    favorites_contract = deploy_favorites()
    # Act
    favorites_contract.store(42)
    # Assert
    assert favorites_contract.retrieve() == 42

def test_can_add_people():
    # Arrange
    new_person = "Becca"
    favorites_number = 16
    favorites_contract = deploy_favorites()

    # Act
    favorites_contract.add_person(new_person, favorites_number)

    # Assert
    assert favorites_contract.list_of_people(0) == (favorites_number, new_person)