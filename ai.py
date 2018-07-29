import move
import moveTypes
import random
trainerHealth = 100

class Ai:
    #setter
    def trainerHealth(setTo):
        global trainerHealth
        trainerHealth = setTo

    #getter
    def getTrainerHealth():
        global trainerHealth
        return trainerHealth
    
    #choose move
    def makeMove():
        global trainerHealth
        if(trainerHealth > 49):
            #attack mode
            ran = random.randint(0,2)
            if(ran == 0):
                move.Move.makeMove(moveTypes.MoveTypes.TACKLE)
            else:
                move.Move.makeMove(moveTypes.MoveTypes.UNNERVING_GROWL)
        else:
            #defense mode
            ran = random.randint(0,2)
            if(ran == 0):
                move.Move.makeMove(moveTypes.MoveTypes.CRIMSON_CHARGE)
            else:
                move.Move.makeMove(moveTypes.MoveTypes.DART_BULLET)