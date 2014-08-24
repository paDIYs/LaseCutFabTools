import rhinoscriptsyntax as rs

rs.EnableRedraw(False)
# Get Box dimensions
w = rs.GetInteger("Width of the base, this must be the longest side")
h = rs.GetInteger("Height of the base")
H = rs.GetInteger("Depth of the box")
rec = rs.AddRectangle([0,0,0], w, h)
lns = rs.ExplodeCurves(rec, True)
# Get notchedd parameers
jLen = rs.GetInteger("Joins length")
yThick = rs.GetReal("Thickness of the material")
xThick = yThick
# Set the number of teeth
nJoinsW = int (w/jLen)
if nJoinsW%2 == 0:
    nJoinsW += 1

nJoinsV = int (H/jLen)
if nJoinsV%2 == 0:
    nJoinsV += 1
    
nJoinsH = int (h/jLen)
if nJoinsH%2 == 0:
    nJoinsH += 1

# function that merge the list of points
def addList (listA, listB, listC, a, b):
    for i in range (a, b):
        listC.append(listA[i])
    for j in range (a, b):
        listC.append(listB[j])
        
# function that make the notched join
def addJoin (lns, nJoins, xThick, yThick ):
    
    joins = []
    joins_3 = []
    
    points = rs.DivideCurve(lns, nJoins)
    lenP = len(points)
    
    for i in range (lenP):
        joins.append(rs.AddPoint(points[i]))
    
    joins_2 = rs.CopyObjects(joins,[xThick,yThick,0])
    joins_2.remove(joins_2[0])
    joins_2.append([0,0,0])
   
    for j in range (0,len(joins),2):
        c = j + 2
        addList(joins, joins_2, joins_3, j, c)
    
    joins_3.remove(joins_3[len(joins_3)-1])
    joins_3.remove(joins_3[len(joins_3)-1])
    joined = rs.AddPolyline(joins_3)
    rs.DeleteObject(lns)
    
    return joined

# Make the bottom of the box
s_1 = addJoin(lns[0], nJoinsW, 0, -1*yThick)
s_3 = addJoin(lns[2], nJoinsW, 0, yThick)
s_2 = addJoin(lns[1], nJoinsH, xThick,0 )
s_4 = addJoin(lns[3], nJoinsH, -1*xThick,0 )

# Make side one
side = rs.CopyObject(s_3, [0,yThick*4,0])
pt = rs.CurveStartPoint(side)
pt_1 = rs.AddPoint(pt)
pt_2 = rs.CopyObject(pt_1, [0,H,0])
sSide = rs.AddLine(pt_1, pt_2)

st = addJoin(sSide, nJoinsV, xThick, 0)
mir = rs.MirrorObject(st, pt_1, pt_2, True)
rs.MoveObject(mir, [-w, 0, 0])
rs.CopyObject(s_1, [0,(h+yThick*4+H),0])

# Make side two
side_2 = rs.CopyObject(s_2, [xThick*4,0,0])
pt = rs.CurveStartPoint(side_2)
pt_11 = rs.AddPoint(pt)
pt_21 = rs.CopyObject(pt_11, [H,0,0])
sSide_2 = rs.AddLine(pt_11, pt_21)

st_2 = addJoin(sSide_2, nJoinsV, 0, -1*yThick)
mir_2 = rs.MirrorObject(st_2, pt_11, pt_21, True)
rs.MoveObject(mir_2, [0, -1*yThick, 0])
la = rs.CopyObject(s_4, [(w+xThick*4+H),0,0])
rs.MoveObject(st_2, [0, h+yThick, 0])

rs.ExtendCurveLength(side_2,0,1,xThick)
rs.ExtendCurveLength(side_2,0,0,xThick)
rs.ExtendCurveLength(la,0,1,xThick)
rs.ExtendCurveLength(la,0,0,xThick)

# Delete Points
pot=rs.ObjectsByType(1, True)
rs.DeleteObjects(pot)


rs.EnableRedraw(True)
