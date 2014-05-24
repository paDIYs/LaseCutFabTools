import rhinoscriptsyntax as rs

rs.EnableRedraw(False)
#Get Kerf parameters for bending
obj_0 = rs.GetObject("Select the bottom line", 4)
obj_1 = rs.GetObject("Select the left line", 4)
l = rs.GetInteger("Segments lenght [mm]")
dis = rs.GetInteger("Distance x from the segments [mm]")
sp = rs.GetInteger("Distance y from the segments [mm]")
# Set the length of the segment
L = rs.CurveLength(obj_0)
x = (L/(l+dis))
xint = int(x+0.5)
d = L/xint-l

L_2 = rs.CurveLength(obj_1)
x_2 = (L_2/sp)
xint_2 = int(x_2+0.5)
s = L_2/xint_2


#----------Generate pattern A----------#
joins = []
a = rs.AddPoint(rs.CurveStartPoint (obj_0))
joins.append(a)
p = rs.CopyObject(a,[(l/2),0,0])
joins.append(p)

for i in range (1, (xint)):
    c = rs.CopyObject(p,[d,0,0])
    joins.append(c)
    p = rs.CopyObject(c,[l,0,0])
    joins.append(p)
lj = len(joins)-1
p = rs.CopyObject(joins[lj],[d,0,0])
joins.append(p)
c = rs.CopyObject(p,[(l/2),0,0])
joins.append(c)

pattern_A = []
for i in range (0, (len(joins)-1), 2):
    pattern_A.append(rs.AddLine(joins[i],joins[i+1]))

#----------Generate pattern B----------#
joins_2 = []
joins_2.append(a)
p_2 = rs.CopyObject(a,[(d/2),0,0])
joins_2.append(p_2)

for i in range (1, (xint+1)):
    c_2 = rs.CopyObject(p_2,[l,0,0])
    joins_2.append(c_2)
    p_2 = rs.CopyObject(c_2,[d,0,0])
    joins_2.append(p_2)

pattern_B = []
for i in range (1, (len(joins_2)-1), 2):
    pattern_B.append(rs.AddLine(joins_2[i],joins_2[i+1]))

p_B = rs.MoveObjects(pattern_B, [0,s,0])

for i in range (0, (xint_2-1), 2):
    pattern_A = rs.CopyObjects(pattern_A, [0,s*2,0])
    p_B = rs.CopyObjects(p_B, [0,s*2,0])


rs.DeleteObjects(joins)
rs.DeleteObjects(joins_2)
rs.DeleteObject(obj_0)

rs.EnableRedraw(True)
