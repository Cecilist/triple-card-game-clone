import pytest
import card
import main


    
@pytest.fixture
def dummyCard():
    return card.Card("test", 1, 2, 3, 4, "Blue")

# @pytest.fixture
# def board():
#     return [0,0,0,0,0,0,0,0,0]

def test_card_ini(dummyCard):
    print("testing initialization of a card")
    assert ("test", 1, 2, 3, 4, "Blue", -1) == (dummyCard.name, dummyCard.north, dummyCard.south, dummyCard.east, dummyCard.west, dummyCard.player, dummyCard.pos)

def test_card_setPos(dummyCard):
    print("testing the set position function of a card")
    dummyCard.setPos(5)
    assert (5) == (dummyCard.pos)

def test_play_card(dummyCard):
    print("testing that the playCard funtion adds a card to the board in correct position")
    assert ([0,0,0,0,dummyCard,0,0,0,0]) == main.playCard(4, dummyCard)

