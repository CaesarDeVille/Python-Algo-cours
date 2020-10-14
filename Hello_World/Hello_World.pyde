#ceci est un commentaire.

#Ceci sert a définir la fonction setup qui sera éxécuté comme point d'entré dans mon code.
def setup():
    #on appelle la fonction print pour écrire dans la console.
    print("Hello world")
    #On définit la taille de la fenestre
    size(400, 400)
    #vide la fenêtre
    clear()
    #on change le framerate de l'application
    frameRate(100)


def draw():
    fill(random(225), random(225), random(225))
    #clear()
    #ellipse(mouseX,mouseY, 80, 80)
    ellipse(width/2 + cos(millis() * 0.005)*100, height/2 + cos(millis() * 0.009)*100, 35, 45)
    
