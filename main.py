import ai
import moveTypes
import player
import effect
import random
score = 0
trainerHealthReset = 100

#shorthands
p = player.Player
a = ai.Ai
e = effect.Effect

#intro
print("Made By FOA Inc.")
print("Welcome to the world of SSTmon! I'm Professor Oak.")
nPlayer = str(input("What is your name?"))
print("All right " + str(nop) + ", Let's start your SSTmon adventure!")
print("A trainer is approaching! What will you do?")

#main code
while(p.getPlayerHealth() > 0):
    p.playerHealth(100)
    a.trainerHealth(trainerHealthReset)
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
    if(p.getPlayerHealth() <= 0):
        break
    else:
        print("You won! The next trainer is approaching. What will you do?")
        score += 1
        trainerHealthReset += random.randint(5,10)

print("You lost! Your score is:")
print(str(score))