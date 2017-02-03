import math

def makePpm():
    a = open("picture.ppm",'w')
    a.write("P3\n500 500\n255\n")
    for x in range(0,500):
        for y in range(0,500):
            a.write("%d %d %d " % ( (x % 256), (y % 256), (((x+y)/2) % 256) ) )
        a.write("\n")


def makeCircle():
    a = open("circle.ppm",'w')
    a.write("P3\n500 500\n255\n")
    for x in range(1,501):
        for y in range(1,501):
            radius = math.floor(math.sqrt(math.pow((x-250),2) + math.pow((y-250),2)))
            if radius == 100:
                a.write("0 0 255 ") #blue
            else:
                a.write("255 255 255 ") #white

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
