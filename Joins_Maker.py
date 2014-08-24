import rhinoscriptsyntax as rs

rs.EnableRedraw(False)


# Get curve and the length
lns = rs.GetObject("Select one curve", 4, True, True )
w = rs.CurveLength(lns)

# Get the parameters of the notched
jLen = rs.GetInteger("Joins length")
yThick = rs.GetReal("Thickness of the material")
xThick = yThick
vers = rs.GetReal("put 1 if the line is vertical, put 2 if the line is horizontal")

#set the number of the tooth
nJoinsW = int (w/jLen)
if nJoinsW%2 == 0:
    nJoinsW += 1

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

# set if the curve is vertical or horizontal
if (vers == 1):
    xThick = xThick
    yThick = 0 
elif (vers == 2):
    xThick = 0
    yThick = yThick 

# apply the notched join function to the curve
s_1 = addJoin(lns, nJoinsW, xThick, yThick)

# Delete Points
pot=rs.ObjectsByType(1, True)
rs.DeleteObjects(pot)


rs.EnableRedraw(True)
