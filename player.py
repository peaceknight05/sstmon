import moveTypes
import move
playerHealth = 100

class Player:
    #setter
    def playerHealth(setTo):
        global playerHealth
        playerHealth = setTo

    #getter
    def getPlayerHealth():
        global playerHealth
        return playerHealth

    #makes move
    def makeMove():
        for moveT in moveTypes.MoveTypes:
            if(moveT == moveTypes.MoveTypes.CRIMSON_CHARGE):
                break
            print(str(moveT.value) + ": " + moveT.name)
        move.Move.makeMove(moveTypes.MoveTypes(int(input("Make a move (number)\n"))))