import moveTypes
import effect
import random
import player
import ai

class Move:
    #make move
    def makeMove(move):
        if(move == moveTypes.MoveTypes.LEAF_WHIRLWIND):
            print("Player used Leaf Whirlwind")
            if(not(effect.Effect.getTrainerImmune())):
                ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 5)
            else:
                print("The opponent's pokemon is immune!")
                effect.Effect.trainerImmuneOff()
            #chance
            ran = random.randint(0,4)
            if(ran == 0):
                effect.Effect.effectDo("poison")
        elif(move == moveTypes.MoveTypes.QUASI_PROTECT):
            print("Player used Quasi Protect")
            if(not(effect.Effect.getTrainerImmune())):
                ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 6)
            else:
                print("The opponent's pokemon is immune!")
                effect.Effect.trainerImmuneOff()
            #chance
            ran = random.randint(0,5)
            if(ran == 0):
                effect.Effect.effectDo("immune")
        elif(move == moveTypes.MoveTypes.REBOUND_SMASH):
            print("Player used Rebound Smash")
            if(not(effect.Effect.getTrainerImmune())):
                ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 5)
            else:
                print("The opponent's pokemon is immune!")
                effect.Effect.trainerImmuneOff()
            #chance
            ran = random.randint(0,10)
            if(ran < 2):
                effect.Effect.effectDo("crit")
                if(not(effect.Effect.getTrainerImmune())):
                    ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 2)
                else:
                    print("The opponent's pokemon is immune!")
                    effect.Effect.trainerImmuneOff()
        elif(move == moveTypes.MoveTypes.NATURES_FURY):
            print("Player used Nature's Fury")
            if(not(effect.Effect.getTrainerImmune())):
                ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 8)
            else:
                print("The opponent's pokemon is immune!")
                effect.Effect.trainerImmuneOff()
            #chance
            ran = random.randint(0,100)
            if(ran < 11):
                effect.Effect.effectDo("superpoison")
        elif(move == moveTypes.MoveTypes.CRIMSON_CHARGE):
            print("Trainer used Crimson Charge")
            if(not(effect.Effect.getPlayerImmune())):
                player.Player.playerHealth(player.Player.getPlayerHealth() - 7)
            else:
                print("Your pokemon is immune!")
                effect.Effect.playerImmuneOff()
            #chance
            ran = random.randint(0,100)
            if(ran < 14):
                effect.Effect.effectDo("poison")
        elif(move == moveTypes.MoveTypes.TACKLE):
            print("Trainer used Tackle")
            if(not(effect.Effect.getPlayerImmune())):
                player.Player.playerHealth(player.Player.getPlayerHealth() - 7)
            else:
                print("Your pokemon is immune!")
                effect.Effect.playerImmuneOff()
            #chance
            ran = random.randint(0,100)
            if(ran < 24):
                effect.Effect.effectDo("crit")
                if(not(effect.Effect.getPlayerImmune())):
                    player.Player.playerHealth(player.Player.getPlayerHealth() - 2)
                else:
                    print("Your pokemon is immune!")
                    effect.Effect.playerImmuneOff()
        elif(move == moveTypes.MoveTypes.UNNERVING_GROWL):
            print("Trainer used Unnerving Growl")
            if(not(effect.Effect.getPlayerImmune())):
                player.Player.playerHealth(player.Player.getPlayerHealth() - 4)
            else:
                print("Your pokemon is immune!")
                effect.Effect.playerImmuneOff()
            #chance
            ran = random.randint(0,100)
            if(ran < 21):
                effect.Effect.effectDo("immune")
        else:
            print("Trainer used Dart Bullet")
            if(not(effect.Effect.getPlayerImmune())):
                player.Player.playerHealth(player.Player.getPlayerHealth() - 4)
            else:
                print("Your pokemon is immune!")
                effect.Effect.playerImmuneOff()
            #chance
            ran = random.randint(0,4)
            if(ran == 0):
                effect.Effect.effectDo("superpoison")