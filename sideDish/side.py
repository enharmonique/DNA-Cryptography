import math
import os
filePath = input("FILE=")

#C:\Users\ericv\Desktop\msclsnts\temp.txt
if(os.path.exists(filePath)):
    with open(filePath) as f:
        bases = f.read()
else:
    bases = filePath

import drawDna


def aspair(base:str):
    if(base.upper() == "A"):
        return drawDna.baseNum['a'],drawDna.baseNum['t']
    if(base.upper() == "T"):
        return drawDna.baseNum['t'],drawDna.baseNum['a']
    if(base.upper() == "C"):
        return drawDna.baseNum['c'],drawDna.baseNum['g']
    if(base.upper() == "G"):
        return drawDna.baseNum['g'],drawDna.baseNum['c']

def spow(v,q=1.0):
    if(v<0):return -math.pow(-v,q)
    return math.pow(v,q)

pi=math.pi
#we want around 50 per line
flips = len(bases)//100 + 1
if(flips==1): flips+=1
strandwidth = 0.9 * 0.3 / flips / 2

midPointsX = [(spow(math.sin(i/len(bases) * flips * pi))*0.9+1)/2 for i in range(len(bases))]
midPointsY = [((-math.sin(2*i/len(bases) * flips * pi)/3)/flips+(i)/len(bases)*0.9+0.05) for i in range(len(bases))]

strands = []

for i in range(len(bases)):
    base = bases[i]
    a,b=aspair(base)
    mid = (midPointsX[i],midPointsY[i])

    normal1=(0,0)
    normal2=(0,0)
    if(i!=0):
        normal1 = (midPointsY[i-1]-midPointsY[i],midPointsX[i]-midPointsX[i-1])
    if(i<len(bases)-1):
        normal2 = (midPointsY[i]-midPointsY[i+1],midPointsX[i+1]-midPointsX[i])
    
    normal = (normal1[0]+normal2[0],normal1[1]+normal2[1])

    normalLen = math.sqrt(normal[0]*normal[0]+normal[1]*normal[1])
    normal = (normal[0]/normalLen,normal[1]/normalLen)

    x1 = mid[0] + normal[0]* strandwidth
    x2 = mid[0] - normal[0]* strandwidth
    y1 = mid[1] + normal[1]* strandwidth
    y2 = mid[1] - normal[1]* strandwidth

    strands.append(((a,x1,y1),(b,x2,y2)))


drawDna.setStrands([strands])


drawDna.win.getMouse()