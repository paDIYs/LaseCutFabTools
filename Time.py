import rhinoscriptsyntax as rs


#import cutting curves and laser cutting speed [mm/s] parameters
curve = rs.GetObjects("Select curves to cut", 4)
n = rs.GetReal("Cutting speed", 45, 5)
# conversion [minutes/mm]
n = (1/(n*60))
#import cutting curves and laser engraving speed [mm/s] parameters
curve_2 = rs.GetObjects("Select curves to engrave", 4)
n_2 = rs.GetReal("Engraving speed", 150, 5)
# conversion [minutes/mm]
n_2 = (1/(n_2*60))
# % factor for adjust the result
c = 1.30 

if  curve is None:
    l=0
# length sum of all cutting curves
else:
    l=0
    i = 0
    while i < len(curve):
        l += rs.CurveLength(curve[i])
        i += 1

if curve_2 is None:
    l_2=0
# length sum of all engraving curves
else:
    l_2=0
    j = 0
    while j < len(curve_2):
       l_2 += rs.CurveLength(curve_2[j])
       j += 1

# multiplication of length [mm], speed and factor of approximation
t_1 = (l*n)*c
t_2 = (l_2*n_2)*c

#print t_1, "minuti taglio"
#print t_2, "minuti incisione"

# print the working time
print round(t_1+t_2,2), "Minutes of working"
