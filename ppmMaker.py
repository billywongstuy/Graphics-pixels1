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

        
#star diameter = 32 px
        
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

                
makePpm()
makeCircle()
makeFlag()




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


#to do above y=2x+2
#have to put the equation -2x+498 in

def inStar(cx,cy,r,px,py):
    #order is 1,5,4,3,2
    pts = getFivePoints([cx,cy],r,getCircPentSideLen(r))
    line1 = equation4Pic(pts[0][0],pts[0][1],pts[3][0],pts[3][1]) #should be 1 to 3
    line2 = equation4Pic(pts[3][0],pts[3][1],pts[1][0],pts[1][1]) #should be 3 to 5
    line3 = equation4Pic(pts[1][0],pts[1][1],pts[4][0],pts[4][1]) #should be 5 to 2
    line4 = equation4Pic(pts[4][0],pts[4][1],pts[2][0],pts[2][1]) #a bit off 2 to 4
    line5 = equation4Pic(pts[2][0],pts[2][1],pts[0][0],pts[0][1]) #a bit off 4 to 1
    #if onEquat(line1,px,py) or onEquat(line2,px,py) or onEquat(line3,px,py) or onEquat(line4,px,py) or onEquat(line5,px,py):
    #    return True

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
    
def makePentagon():
    a = open("pentagon.ppm",'w')
    a.write("P3\n500 500\n255\n")
    
    pts = getFivePoints([250,250],100,getCircPentSideLen(100))
    print pts
    
    for y in range(1,501):
        for x in range(1,501):
            #l1 = equation4Pic(250,150,308,330)
            radius = int(math.sqrt(math.pow((x-250),2) + math.pow((y-250),2)))
            if [x,y] in pts:
                a.write("255 0 0 ") #red
            elif x == 250 and y == 250:
                a.write("0 0 0 ")
            elif inStar(250,250,100,x,y) and radius <= 100:
                a.write("0 255 255 ") #aqua
            #currently equation calced
            #elif aboveEquat(l1,x,y) and radius <= 100:
            #    a.write("0 255 255 ") #aqua
            elif radius == 100:
                a.write("255 255 0 ") #yellow
            else:
                a.write("255 255 255 ") #white
        a.write("\n")


makePentagon()
