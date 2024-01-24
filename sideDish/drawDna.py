import graphics
W=800;H=800
win = graphics.GraphWin("Simple visu",W,H,autoflush=False)

baseNum={"_":0,"a":1,"t":2,"c":3,"g":4}
clrs=[None,"#FF5555","#5555FF","#55FF55","#FFFF55"]
fix="#777777"

def setStrands(strands:list[list[tuple[tuple[int,float,float],tuple[int,float,float]]]]):
    win.update()
    win.setBackground("#000000")
    for line in strands:
        last = None
        for left,right in line:
            c1,x1,y1 = left
            c2,x2,y2 = right
            x1*=W;x2*=W;y1*=H;y2*=H
            if(last!=None):
                l1=graphics.Line(graphics.Point(*last[0]),graphics.Point(x1,y1))
                l1.draw(win)
                l1.setOutline(fix)
                l2=graphics.Line(graphics.Point(*last[1]),graphics.Point(x2,y2))
                l2.setOutline(fix)
                l2.draw(win)
                pass
            xc=(x1+x2)/2;yc=(y1+y2)/2
            if(c1!=0):
                l1=graphics.Line(graphics.Point(xc,yc),graphics.Point(x1,y1))
                l1.setOutline(clrs[c1])
                l1.draw(win)
            if(c2!=0):
                l2=graphics.Line(graphics.Point(xc,yc),graphics.Point(x2,y2))
                l2.setOutline(clrs[c2])
                l2.draw(win)
            last = ((x1,y1),(x2,y2))
    win.update()

if __name__ == "__main__":
    setStrands([
        [
            ((0,0.5,0.5),(2,0.5,0.6)),
            ((3,0.6,0.5),(4,0.6,0.6)),
            ((2,0.7,0.5),(1,0.7,0.6)),
            ((4,0.8,0.5),(0,0.8,0.6)),
        ]
    ])
    win.getMouse() # pause for click in window
    win.close()