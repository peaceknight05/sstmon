import ai
import moveTypes
import player
import effect

#shorthands
p = player.Player
a = ai.Ai
e = effect.Effect

#main code
p.playerHealth(100)
a.trainerHealth(100)
e.nullify()
while((p.getPlayerHealth() > 0) & (a.getTrainerHealth() > 0)):
    e.turn("player")
    p.makeMove()
    if(a.getTrainerHealth() <= 0):
        break
    e.turn("trainer")
    a.makeMove()
    if(p.getPlayerHealth() <= 0):
        break
    e.updateEffect()
    if((p.getPlayerHealth() <= 0) | (a.getTrainerHealth() <= 0)):
        break
    print("Your health: " + str(p.getPlayerHealth()))
    print("Opponent's health: " + str(a.getTrainerHealth()))