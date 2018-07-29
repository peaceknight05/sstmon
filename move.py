import moveTypes
import effect
import random
import player
import ai
ran = 0

class Move:
    #make move
    def makeMove(move):
        if(move == moveTypes.MoveTypes.LEAF_WHIRLWIND):
            print("Player used Leaf Whirlwind")
            if(not(effect.Effect.trainerImmune)):
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
            if(not(effect.Effect.trainerImmune)):
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
            if(not(effect.Effect.trainerImmune)):
                ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 5)
            else:
                print("The opponent's pokemon is immune!")
                effect.Effect.trainerImmuneOff()
            #chance
            ran = random.randint(0,10)
            if(ran < 2):
                effect.Effect.effectDo("crit")
                if(not(effect.Effect.trainerImmune)):
                    ai.Ai.trainerHealth(ai.Ai.getTrainerHealth() - 5)
                else:
                    print("The opponent's pokemon is immune!")
                    effect.Effect.trainerImmuneOff()
        elif(move == moveTypes.MoveTypes.NATURES_FURY):
            print("Player used Nature's Fury")
            if(not(effect.Effect.trainerImmune)):
                player.Player.trainerHealth(ai.Ai.getTrainerHealth() - 8)
            else:
                print("The opponent's pokemon is immune!")
                effect.Effect.trainerImmuneOff()
            #chance
            ran = random.randint(0,100)
            if(ran < 11):
                effect.Effect.effectDo("superpoison")
        elif(move == moveTypes.MoveTypes.CRIMSON_CHARGE):
            print("Trainer used Crimson Charge")
            if(not(effect.Effect.trainerImmune)):
                player.Player.playerHealth(player.Player.getPlayerHealth() - 8)
            else:
                print("Your pokemon is immune!")
                effect.Effect.playerImmuneOff()
            #chance
            ran = random.randint(0,10)
            if(ran == 0):
                effect.Effect.effectDo("immune")
        elif(move == moveTypes.MoveTypes.TACKLE):
            print("Trainer used Tackle")
            if(not(effect.Effect.playerImmune)):
                player.Player.playerHealth(player.Player.getPlayerHealth() - 6)
            else:
                print("Your pokemon is immune!")
                effect.Effect.playerImmuneOff()
            #chance
            ran = random.randint(0,100)
            if(ran < 12):
                effect.Effect.effectDo("crit")
                if(not(effect.Effect.playerImmune)):
                    player.Player.playerHealth(player.Player.getPlayerHealth() - 6)
                else:
                    print("Your pokemon is immune!")
                    effect.Effect.playerImmuneOff()
        elif(move == moveTypes.MoveTypes.UNNERVING_GROWL):
            print("Trainer used Unnerving Growl")
            if(not(effect.Effect.getPlayerImmune)):
                player.Player.playerHealth(player.Player.getPlayerHealth() - 3)
            else:
                print("Your pokemon is immune!")
                effect.Effect.playerImmuneOff()
            #chance
            ran = random.randint(0,100)
            if(ran < 38):
                effect.Effect.effectDo("superpoison")
        else:
            print("Trainer used Dart Bullet")
            if(not(effect.Effect.trainerImmune)):
                player.Player.playerHealth(player.Player.getPlayerHealth() - 5)
            else:
                print("Your pokemon is immune!")
                effect.Effect.playerImmuneOff()
            #chance
            ran = random.randint(0,4)
            if(ran == 0):
                effect.Effect.effectDo("poison")