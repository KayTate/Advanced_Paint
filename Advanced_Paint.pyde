rainbow = False
tri = False
cirlce = False
sqr = False

def setup():
    size(600,400)
    background(255)
    
    #set up for rectangles
    fill("#35668E")
    rect(0,0,50,50)
    
    fill(0,0,0)
    rect(0,50,50,50)
    
    fill("#E395CD")
    rect(0,100,50,50)
    
    fill("#9A95E3")
    rect(0,150,50,50)
    
    fill("#95E1E3")
    rect(0,200,50,50)
    
    fill(255,0,0)
    rect(0,250,10,50)
    
    fill(0,255,0)
    rect(10,250,10,50)
    fill("#FAA83D")
    rect(20,250,10,50)
    fill("#F3FA3D")
    rect(30,250,10,50)
    fill(0,0,255)
    rect(40,250,10,50)
    
    fill(255)
    rect(0,300,50,50)
    rect(0,350,50,50)
    rect(50,100,50,50)
    rect(50,150,50,50)
    rect(50,200,50,50)
    rect(50,250,50,50)
    rect(50,300,50,50)
    rect(50,350,50,50)
    
    fill("#808589")
    ellipse(25, 325, 25, 25) 
    rect(63, 312, 25,25)
    triangle(75,260,60,290,90,290)
    
    fill(0)
    text("Clear", 10,380)
    text("?", 70, 130)
    
    fill("#62BF5A")
    rect(50,0,50,50)
    
    fill("#438393")
    rect(50,50,50,50)
    
    
def draw():    
    global rainbow, tri, sqr, circle
    if rainbow == True:
        stroke(random(255),random(255),random(255))
    if mousePressed and mouseX > 100:
        if tri = True:
            triangle(
        elif sqr = True:
        elif circle = True:
            ellipse(pmouseX, pmouseY, 50,50)
        else:
            line(pmouseX, pmouseY, mouseX, mouseY)
        
def mouseClicked():
    global rainbow, tri, sqr, circle
    if mouseX <= 50 and mouseY <= 50:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        stroke("#35668E")

    elif mouseX <= 50 and mouseY > 50 and mouseY <=100:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        stroke(0,0,0)

    elif mouseX <= 50 and mouseY > 100 and mouseY <=150:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        stroke("#E395CD")

    elif mouseX <= 50 and mouseY > 150 and mouseY <=200:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        stroke("#9A95E3")

    elif mouseX <= 50 and mouseY > 200 and mouseY <=250:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        stroke("#95E1E3")

    elif mouseX <= 50 and mouseY >350:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        fill(255)
        noStroke()
        rect(101,0,550,400)

    elif mouseX >50 and mouseX <= 100 and mouseY <=50:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        stroke ("#62BF5A")

    elif mouseX >50 and mouseX <= 100 and mouseY > 50 and mouseY <=100:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        stroke ("#438393")

    elif mouseX >50 and mouseX <= 100 and mouseY > 100 and mouseY <=150:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        stroke(random(255),random(255),random(255))

    elif mouseX <=50 and mouseY > 250 and mouseY <= 300: 
        rainbow = True
        sqr = False
        circle = False
        tri = False
        
    elif mouseX > 50 and mouseY > 250 and mouseY <= 300:
        tri = True
        sqr = False
        circle = False
        rainbow = False
