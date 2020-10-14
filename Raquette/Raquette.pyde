ballX = 0
ballY = 0

rackX = 0
rackY = 0
rackW = 125
rackH = 10

BSpeedX = 5
BSpeedY = 5
ballRadius = 5

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    global ballX, ballY, rackX, rackY, rackW, rackH
    #noCursor()
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on definit la taille de la fenêtre
    size(500, 550)
    #vide la fenêtre
    clear()
    #on change le frameRate de l'application
    frameRate(60)
    ballX = width/2
    ballY = height/2
    
    rackX = mouseX - (rackW/2)
    rackY = height - 20
    #random(255)
    
def draw():
   clear()
   drawRacket ()
   drawBall ()
    
def drawRacket():
    global rackX, rackY, rackW, rackH
    fill(255)
    # Desinner un réctangle avec les coordonées.
    #X : MouseX – 1/2 width.
    #Y : Height of Windows – 20.
    # width : 50
    # height : 10
    rackX = mouseX - (rackW/2)
    rect(rackX, rackY, rackW, rackH, 10)

def drawBall():
    global ballX, ballY, BSpeedX, BSpeedY, ballRadius, rackW, rackY, rackX, rackH
    #draw circle centered on window.
    fill(random(120, 255), 0, 0)
    circle(ballX, ballY, 10)
    
    #ballX = ballX + BSpeedX
    #ballY = ballY + BSpeedY
    #raccourci =
    ballX += BSpeedX
    ballY += BSpeedY
    
    #droite et gauche
    if(ballX+ballRadius > width):
        BSpeedX *= -1.0
        ballX = width-ballRadius
    elif(ballX < ballRadius):
        BSpeedX *= -1.0
        
    #Haut et bas
    if(ballY < ballRadius):
        BSpeedY *= -1.0
    elif(ballY+ballRadius > height):
        BSpeedY *= -1.0
        rackW = rackW*0.95
        
    if(rackY < ballY+ballRadius < rackY+rackH and BSpeedY > 0):
        if(rackX < ballX < rackX + rackW):
            BSpeedY *= -1
            ballY = rackY-ballRadius

    #draw circle
    #circle(ballX, ballY, 2*ballRadius)
    #cos90° : 0 pour x.
#Ajouter notion d'angle avec calcul mathématique.
