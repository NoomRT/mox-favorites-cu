def test_starting_values(favorites_contract):
    assert favorites_contract.retrieve() == 77

def test_can_change_values(favorites_contract):
    # Act
    favorites_contract.store(42)
    # Assert
    assert favorites_contract.retrieve() == 42

def test_can_add_people(favorites_contract):
    # Arrange
    new_person = "Becca"
    favorites_number = 16

    # Act
    favorites_contract.add_person(new_person, favorites_number)

    # Assert
    assert favorites_contract.list_of_people(0) == (favorites_number, new_person)