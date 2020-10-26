ballX = 0
ballY = 0

Bspeed = 0.2
bSpeedX = 0
bSpeedY = 0
Bangle = PI/5

ballRadius = 2
BangleMax = PI/1.9

rackW = 100
rackH = 10
rackX = 0
rackY = 0

LFT = 0
dt = 0
#Delta Time

#ici on definit la fonction setup qui sera exécuté comme point d'entré dans mon code
def setup():
    global ballX, ballY, rackX, rackY, rackW
    global LFT
    #on appel la fonction print pour écrire dans la console
    print("Hello World")
    #on definit la taille de la fenêtre
    size(500, 550)
    #vide la fenêtre
    clear()
    #on change le frameRate de l'application
    frameRate(30)
    ballX = width/2
    ballY = height/2
    
    rackX = mouseX - (rackW/2)
    rackY = height - 50
    
    LFT = millis()
    
    #random(255)
    
def draw():
    global LFT, dt
    
    clear()
    
    dt = millis() - LFT
    LFT = millis()
    
    drawRacket ()
    drawBall ()
    drawBricks ()

    
def drawRacket():
    global rackX, rackY, rackW, rackH
    fill(255, 255, 50)
    # Desinner un réctangle avec les coordonées.
    #X : MouseX – 1/2 width.
    #Y : Height of Windows – 20.
    # width : 50
    # height : 10
    rackX = mouseX - (rackW/2)
    rect(rackX, rackY, rackW, rackH, 10)

def drawBall():
    global ballX, ballY, ballRadius, Bangle, Bspeed
    global rackY, rackX, rackW, rackH
    global dt
    global BangleMax
    
    #raccourci =
    speedX = cos(Bangle) * Bspeed * dt
    speedY = sin(Bangle) * Bspeed * dt
    ballX += speedX
    ballY -= speedY

    #haut et bas   
    if(ballY-ballRadius < 0):
        Bangle = -Bangle
        ballY = ballRadius
    elif(ballY+ballRadius > height):
        Bangle = -Bangle
        ballY = height-ballRadius
        rackW = rackW-10
    
    #droite et gauche
    if(ballX+ballRadius > width):
        Bangle = PI - Bangle
        ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
        Bangle = PI-Bangle
        ballX = ballRadius
        
        
    if(rackY < ballY+ballRadius < rackY+rackH and speedY < 0):
        if(rackX < ballX < rackX + rackW):
           ratio = (ballX - rackX - rackW/2) / (rackW/2)
           print(ratio)
           Bangle = PI/2 - ratio * BangleMax
           ballY = rackY-ballRadius

    #draw circle
    circle(ballX, ballY, 2*ballRadius)

def drawBricks():
    
    global ballX, ballY, ballRadius, bSpeedX, bSpeedY, Bangle
    fill(1 , 162, 253)
    bX = width/3
    bY = height/10
    bW = width/3
    bH = height/10

    rect(bX, bY, bW, bH)

#haut et bas   
    if(bY-ballRadius < ballY and bY+ballRadius > ballY and bX+bW+ballRadius > ballX and bX-ballRadius < ballX):
        Bangle = -Bangle
        ballY = bY-ballRadius
    elif(bY+bH+ballRadius > ballY and bY+bH-ballRadius < ballY and bX+ballRadius < ballX and bX+bW+ballRadius > ballX):
        Bangle = -Bangle
        ballY = bY+bH+ballRadius

#droite et gauche
    if(bX-ballRadius < ballX and bX+ballRadius > ballX and bY+bH+ballRadius > ballY and bY+ballRadius < ballY):
        Bangle = PI-Bangle
        ballX = bX-ballRadius
    elif(bX+bW-ballRadius < ballX and bX+bW+ballRadius > ballX and bY+ballRadius < ballY and bY+bH+ballRadius > ballY):
        Bangle = PI-Bangle
        ballX = bX+bW+ballRadius
