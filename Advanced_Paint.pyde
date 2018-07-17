rainbow = False
tri = False
circle = False
sqr = False
dim = 50
col = "#000000"
lin = True

def setup():
    size(600,400)
    background(255)
    
    #Button Setup
    #Button 1.1
    fill("#35668E")
    rect(0,0,50,50)
    
    #Button 1.2
    fill(0,0,0)
    rect(0,50,50,50)
    
    #Button 1.3
    fill("#E395CD")
    rect(0,100,50,50)
    
    #Button 1.4
    fill("#9A95E3")
    rect(0,150,50,50)
    
    #Button 1.5
    fill("#95E1E3")
    rect(0,200,50,50)
    
    #Button 1.6 pt. 1
    fill(255,0,0)
    rect(0,250,10,50)
    #Button 1.6 pt. 2
    fill(0,255,0)
    rect(10,250,10,50)
    #Button 1.6 pt. 3
    fill("#FAA83D")
    rect(20,250,10,50)
    #Button 1.6 pt. 4
    fill("#F3FA3D")
    rect(30,250,10,50)
    #Button 1.6 pt. 5
    fill(0,0,255)
    rect(40,250,10,50)
    
    #Button 1.7
    fill(255)
    rect(0,300,50,50)
    
    #Button 1.8
    rect(0,350,50,50)

    #Button 2.1
    fill("#255F2F")
    rect(50,0,50,50)
    
    #Button 2.2
    fill("#644928")
    rect(50,50,50,50)

    #Button 2.3
    fill(255)
    rect(50,100,50,50)
    
    #Button 2.4
    fill("#F3FA49")
    rect(50,150,50,50)
    
    #Button 2.5
    fill(255)
    rect(50,200,50,50)
    
    #Button 2.6
    rect(50,250,50,50)
    
    #Button 2.7
    rect(50,300,50,50)
    
    #Button 2.8
    rect(50,350,50,50)
    
    #Shape Stamps
    fill("#808589")
    ellipse(25, 325, 25, 25) 
    rect(63, 312, 25,25)
    triangle(75,260,60,290,90,290)
    
    #Text Indicators
    fill(0)
    text("Clear", 10,380)
    text("?", 70, 130)
    text("Size", 65, 362)
    text("+", 74, 377)
    text("-", 75, 396)
    rect(60,225,30,1)
    
    
def draw():    
    global rainbow, tri, sqr, circle, dim, col
    if rainbow == True:
        stroke(random(255),random(255),random(255))
    if mousePressed and mouseX > 100:
        if tri == True:
            fill(col)
            triangle(mouseX,mouseY,mouseX - dim, mouseY + dim, mouseX + dim, mouseY+ dim)
        elif sqr == True:
            fill(col)
            rect(pmouseX, pmouseY, dim, dim)
        elif circle == True:
            fill(col)
            ellipse(pmouseX, pmouseY, dim,dim)
        elif lin == True:
            line(pmouseX, pmouseY, mouseX, mouseY)
    
        
def mouseClicked():
    global rainbow, tri, sqr, circle, dim, col
    #Button 1.1
    if mouseX <= 50 and mouseY <= 50:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke("#35668E")
        col = "#35668E"

    #Button 1.2
    elif mouseX <= 50 and mouseY > 50 and mouseY <=100:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke(0,0,0)
        col = "000000"

    #Button 1.3
    elif mouseX <= 50 and mouseY > 100 and mouseY <=150:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke("#E395CD")
        col = "#E395CD"

    #Button 1.4
    elif mouseX <= 50 and mouseY > 150 and mouseY <=200:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke("#9A95E3")
        col = "#9A95E3"

    #Button 1.5
    elif mouseX <= 50 and mouseY > 200 and mouseY <=250:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke("#95E1E3")
        col = "#95E1E3"

    #Button 1.6
    elif mouseX <=50 and mouseY > 250 and mouseY <= 300: 
        rainbow = True
        sqr = False
        circle = False
        tri = False
        
    #Button 1.7
    elif mouseX <= 50 and mouseY >300 and mouseY <=350:
        fill(0)
        tri = False
        sqr = False
        circle = True
        rainbow = False
        
    #Button 1.8
    elif mouseX <= 50 and mouseY >350:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        fill(255)
        noStroke()
        rect(101,0,550,400)

    #Button 2.1
    elif mouseX >50 and mouseX <= 100 and mouseY <=50 and mouseX <= 100:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke("#255F2F")
        col = "#255F2F"

    #Button 2.2
    elif mouseX >50 and mouseX <= 100 and mouseY > 50 and mouseY <=100 and mouseX <= 100:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke("#644928")
        col = "#644928"

    #Button 2.3
    elif mouseX >50 and mouseX <= 100 and mouseY > 100 and mouseY <=150 and mouseX <= 100:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke(random(255),random(255),random(255))
        
    #Button 2.4
    elif mouseX >50 and mouseX <= 100 and mouseY > 150 and mouseY <=200 and mouseX <= 100:
        # rainbow = False
        # tri = False
        # sqr = False
        # circle = False
        stroke("#F3FA49")
        col = "#F3FA49"
        
    #Button 2.5 for fill
    elif mouseX >50 and mouseX <= 100 and mouseY > 200 and mouseY <=250 and mouseX <= 100:
        rainbow = False
        tri = False
        sqr = False
        circle = False
        lin = True

    #Button 2.6
    elif mouseX > 50 and mouseY > 250 and mouseY <= 300 and mouseX <= 100:
        fill(0)
        tri = True
        sqr = False
        circle = False
        rainbow = False
        
    #Button 2.7
    elif mouseX > 50 and mouseY >300 and mouseY <=350 and mouseX <= 100:
        fill(0)
        tri = False
        sqr = True
        circle = False
        rainbow = False
        
    #Button 2.8 pt. 1
    elif mouseX > 50 and mouseX <= 100 and mouseY >350 and mouseY <= 375:
        dim += 5
        
    #Button 2.8 pt. 2
    elif mouseX > 50 and mouseX <= 100 and mouseY >375:
        dim += -5
