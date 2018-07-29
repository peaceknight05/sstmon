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
    e.turn("trainer")
    a.makeMove()
    e.updateEffect()
    print("Your health: " + str(p.getPlayerHealth()))
    print("Opponent's health: " + str(a.getTrainerHealth()))