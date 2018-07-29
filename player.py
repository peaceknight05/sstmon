import moveTypes
import move
playerHealth = 100

class Player:
    #setter
    def playerHealth(setTo):
        playerHealth = setTo

    #getter
    def getPlayerHealth():
        return playerHealth

    #makes move
    def makeMove():
        for moveT in moveTypes.MoveTypes:
            if(moveT == moveTypes.MoveTypes.CRIMSON_CHARGE):
                break
            print(str(moveT.value) + ": " + moveT.name)
        move.Move.makeMove(moveTypes.MoveTypes(int(input("Make a move (number)\n"))))