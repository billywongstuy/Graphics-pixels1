import math

def makePpm():
    a = open("picture.ppm",'w')
    a.write("P3\n500 500\n255\n")
    for y in range(0,500):
        for x in range(0,500):
            a.write("%d %d %d " % ( (x % 256), (y % 256), (((x+y)/2) % 256) ) )
        a.write("\n")


def makeCircle():
    a = open("circle.ppm",'w')
    a.write("P3\n500 500\n255\n")
    for y in range(1,501):
        for x in range(1,501):
            radius = math.floor(math.sqrt(math.pow((x-250),2) + math.pow((y-250),2)))
            if radius == 100:
                a.write("0 0 255 ") #blue
            else:
                a.write("255 255 255 ") #white
        a.write("\n")


def getCircPentSideLen(r):
    return r*math.sqrt(2-2*math.cos((2*math.pi)/5))

#c is a x,y list for center, s is side length
def getFivePoints(c,r,s):
    pts = []
    startAng = math.pi/2
    centAng = (2*math.pi)/5
    i = 0
    while i < 5:
        ang = startAng + (i*centAng)
        x = int(c[0] + r*math.cos(ang))
        y = int(c[1] - r*math.sin(ang))
        pts.append([x,y])
        i+=1
    return pts

def aboveALine(m,b,x,y):
    return y <= m*x + b

def aboveEquat(l,x,y):
    return y <= l[0]*x+l[1]

def onEquat(l,x,y):
    val = l[0]*x+l[1]
    diff = abs(val-y)*100/y
    return diff < 0.4

def equation4Pic(x1,y1,x2,y2):
    data = []
    data.append( ( (y2-y1) *1.0) /(x2-x1))
    data.append(y1-x1*data[0])
    return data


def inStar(cx,cy,r,px,py):
    #order is 1,5,4,3,2
    pts = getFivePoints([cx,cy],r,getCircPentSideLen(r))
    line1 = equation4Pic(pts[0][0],pts[0][1],pts[3][0],pts[3][1]) 
    line2 = equation4Pic(pts[3][0],pts[3][1],pts[1][0],pts[1][1]) 
    line3 = equation4Pic(pts[1][0],pts[1][1],pts[4][0],pts[4][1]) 
    line4 = equation4Pic(pts[4][0],pts[4][1],pts[2][0],pts[2][1]) 
    line5 = equation4Pic(pts[2][0],pts[2][1],pts[0][0],pts[0][1]) 

    if aboveEquat(line3,px,py) and not aboveEquat(line5,px,py) and not aboveEquat(line1,px,py):
        return True
    elif aboveEquat(line2,px,py) and not aboveEquat(line3,px,py) and aboveEquat(line5,px,py):
        return True
    elif not aboveEquat(line5,px,py) and not aboveEquat(line1,px,py) and aboveEquat(line4,px,py) and aboveEquat(line2,px,py):
        return True
    elif aboveEquat(line1,px,py) and not aboveEquat(line3,px,py) and aboveEquat(line4,px,py):
        return True
    elif not aboveEquat(line5,px,py) and aboveEquat(line4,px,py) and not aboveEquat(line2,px,py):
        return True
    elif not aboveEquat(line1,px,py) and aboveEquat(line2,px,py) and not aboveEquat(line4,px,py):
        return True   
    return False


def getFlagStarCenters():
    centers = []
    for y in range (1,10):
        if y % 2 == 1:
            x = 32
        else:
            x = 64
        while x < 384:
            centers.append([x,y*27])
            x+=64
    return centers


def checkStarsRange(centers,x,y,r):
    for center in centers:
        if inStar(center[0],center[1],r,x,y):
            return True
    return False


#US FLAG WITHOUT STARS
def makeFlag():
    red = True
    a = open("fpicture.ppm",'w')
    a.write("P3\n963 507\n255\n")
    for y in range(1,508):
        if (y) % 39 == 0:
            red = not red
        for x in range(1,964):
            if x <= 385 and y <= 272:
                a.write("0 0 255 ") #blue
            elif red:
                a.write("255 0 0 ")
            else: 
                a.write("255 255 255 ") #white


#COMPLETE US FLAG WITH STARS
# MAY TAKE UP TO 50 SEC - 1 MIN AVERAGE   ON LINUX SYSTEM

#star diameter = 32 px    0.0616
#horizontal dist btw diam = 32px     0.063
#vertical dist btw diam = 27 px    0.054

def makeFlagWithStars():
    red = True
    a = open("us-flag.ppm",'w')
    a.write("P3\n963 507\n255\n")

    centers = getFlagStarCenters()
    for y in range(1,508):
        if (y) % 39 == 0:
            red = not red
        for x in range(1,964):
            #print x,y
            #385 272
            if x >= 16 and y >= 11 and x <= 369 and y <= 261 and checkStarsRange(centers,x,y,16): 
                a.write("255 255 255 ") #white
            elif x <= 385 and y <= 272:
                a.write("0 0 255 ") #blue
            elif red:
                a.write("255 0 0 ")
            else: 
                a.write("255 255 255 ") #white

                
makePpm()
makeCircle()
makeFlag()

#COMMENT THIS OUT IF DON'T WANT LONG TIME
makeFlagWithStars()




def makeStar():
    a = open("star.ppm",'w')
    a.write("P3\n500 500\n255\n")
    
    for y in range(1,501):
        for x in range(1,501):
            radius = int(math.sqrt(math.pow((x-250),2) + math.pow((y-250),2)))
            if inStar(250,250,100,x,y) and radius <= 100:
                a.write("255 255 0 ") #yellow
            else:
                a.write("255 255 255 ") #white
        a.write("\n")

#makeStar()
