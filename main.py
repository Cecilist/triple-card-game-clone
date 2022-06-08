import card

board = [0,0,0,0,0,0,0,0,0]
c1 = card.Card("Test1",1,1,1,1,"Red")
c2 = card.Card("Test2",1,1,1,1,"Red")
c3 = card.Card("Test3",1,1,1,1,"Red")
c4 = card.Card("Test4",1,1,1,1,"Red")
c5 = card.Card("Test5",1,1,1,1,"Red")
c6 = card.Card("Test6",1,1,1,1,"Red")
c7 = card.Card("Test7",1,1,1,1,"Red")
c8 = card.Card("Test8",1,1,1,1,"Red")
c9 = card.Card("Test9",1,1,1,1,"Red")
c10 = card.Card("Test10",1,1,1,1,"Red")



def playCard(pos, c):
    playedCard = c
    board[pos] = playedCard
    playedCard.setPos(pos)
    return board
    

def main():

    print(board)
    # playCard(3, c2)    
    print(board)   
    print(board[3])
    # print(c1)
    return 


main()