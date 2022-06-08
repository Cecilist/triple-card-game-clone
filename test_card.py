import pytest
import card


    
@pytest.fixture
def dummyCard():
    return card.Card("test", 1, 2, 3, 4, "Blue")

def test_card_ini(dummyCard):
    print("testing initialization of a card")
    assert ("test", 1, 2, 3, 4, "Blue", -1) == (dummyCard.name, dummyCard.north, dummyCard.south, dummyCard.east, dummyCard.west, dummyCard.player, dummyCard.pos)

def test_card_setPos(dummyCard):
    print("testing the set position function of a card")
    dummyCard.setPos(5)
    assert (5) == (dummyCard.pos)
        
