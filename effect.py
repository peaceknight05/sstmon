import ai
import player
turn = "player"
poisonTurnsPlayer = 0
poisonTurnsTrainer = 0
superpoisonTurnsPlayer = 0
superpoisonTurnsTrainer = 0
isTrainerPoisoned = False
isTrainerSuperpoisoned = False
isPlayerPoisoned = False
isPlayerSuperpoisoned = False
playerImmune = False
trainerImmune = False

class Effect:
    #getters
    def getPlayerImmune():
        global playerImmune
        return playerImmune

    def getTrainerImmune():
        global trainerImmune
        return trainerImmune

    #setters
    def turn(setTo):
        global turn
        turn = setTo

    #off-ers
    def playerImmuneOff():
        global playerImmune
        playerImmune = False

    def trainerImmuneOff():
        global trainerImmune
        trainerImmune = False

    #do effect
    def effectDo(effectName):
        global turn
        global isPlayerPoisoned
        global isPlayerSuperpoisoned
        global poisonTurnsPlayer
        global superpoisonTurnsPlayer
        global isTrainerPoisoned
        global isTrainerSuperpoisoned
        global trainerImmune
        global playerImmune
        if(effectName == "poison"):
            if(turn == "trainer"):
                isPlayerPoisoned = True
                poisonTurnsPlayer = 2
                print("Your pokémon is poisoned")
            elif(turn == "player"):
                isTrainerPoisoned = True
                poisonTurnsTrainer = 2
                print("The opponent's pokémon is poisoned")
            else:
                print("The pokémon is already poisoned")
        elif(effectName == "superpoison"):
            if(turn == "trainer"):
                isPlayerSuperpoisoned = True
                superpoisonTurnsPlayer = 4
                print("Your pokémon is super-poisoned")
            elif(turn == "player"):
                isTrainerSuperpoisoned = True
                superpoisonTurnsTrainer = 4
                print("The opponent's pokémon is super-poisoned")
            else:
                print("The pokémon is already super-poisoned")
        elif(effectName == "crit"):
            print("Critical hit!")
        elif(effectName == "immune"):
            print("Immunity gained")
            if(turn == "trainer"):
                trainerImmune = True
            elif(turn == "player"):
                playerImmune = True
        

    #update effect
    def updateEffect():
        global poisonTurnsPlayer
        global isPlayerPoisoned
        global superpoisonTurnsPlayer
        global isPlayerSuperpoisoned
        global poisonTurnsTrainer
        global isTrainerPoisoned
        global superpoisonTurnsTrainer
        global isTrainerSuperpoisoned     
        if((poisonTurnsPlayer == 0) & isPlayerPoisoned):
            isPlayerPoisoned = False
            print("Your pokemon is no longer poisoned")
        if((poisonTurnsTrainer == 0) & isTrainerPoisoned):
            isTrainerPoisoned = False
            print("The opponent's pokemon is no longer poisoned")
        if((superpoisonTurnsPlayer == 0) & isPlayerSuperpoisoned):
            isPlayerSuperpoisoned = False
            print("Your pokemon is no longer super-poisoned")
        if((superpoisonTurnsTrainer == 0) & isTrainerSuperpoisoned):
            isTrainerSuperpoisoned = False
            print("The opponent's pokemon is no longer super-poisoned")
        if(isTrainerPoisoned):
            print("The opponent's poisoned pokemon is damaged")
            ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 2)
            poisonTurnsTrainer -= 1
        if(isPlayerPoisoned):
            print("Your poisoned pokemon is damaged")
            player.Player.playerHealth(player.Player.getPlayerHealth() - 2)
            poisonTurnsPlayer -= 1
        if(isTrainerSuperpoisoned):
            print("The opponent's super-poisoned pokemon is damaged")
            ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 2)
            superpoisonTurnsTrainer -= 1
        if(isPlayerSuperpoisoned):
            print("Your super-poisoned pokemon is damaged")
            player.Player.playerHealth(player.Player.getPlayerHealth() - 2)
            superpoisonTurnsPlayer -= 1

    #nullify all effects
    def nullify():
        global poisonTurnsPlayer
        global poisonTurnsTrainer
        global superpoisonTurnsPlayer
        global superpoisonTurnsTrainer
        global isTrainerPoisoned
        global isTrainerSuperpoisoned
        global isPlayerPoisoned
        global isPlayerSuperpoisoned
        global playerImmune
        global trainerImmune
        poisonTurnsPlayer = 0
        poisonTurnsTrainer = 0
        superpoisonTurnsPlayer = 0
        superpoisonTurnsTrainer = 0
        isTrainerPoisoned = False
        isTrainerSuperpoisoned = False
        isPlayerPoisoned = False
        isPlayerSuperpoisoned = False
        playerImmune = False
        trainerImmune = False