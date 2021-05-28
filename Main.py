from Map import Map
from Backtracking import Backtracking

def map():
    x = Map()
    numPoints = 10
    x.generate_points(numPoints)
    x.connect_points()
    pkt = list(range(0, numPoints))
    double_constraints = []
    for p in x.points:
        for pp in p.connected_points:
            double_constraints += ([(lambda a, b: a != b, [x.points.index(p), x.points.index(pp)])])
    backtracking = Backtracking([1,2,3,4],pkt, [], double_constraints, [])
    backtracking.solutions(0)
    for i in pkt:
        x.points[i].color = backtracking.solution[0][i]
    x.draw()

Narodowosc = ["Niemiec",   "Szwed", "Anglik", "Dunczyk","Norweg"]
Kolor =["Czerwony","Zolty", "Bialy", "Niebieski", "Zielony"]
Napoj=["Woda", "Herbata",  "Mleko", "Piwo","Kawa"]
Tyton=[ "Light","Cygaro", "BezFiltra", "Mentolowe", "Fajka"]
Zwierze=["Koty", "Konie", "Ptaki", "Psy",  "Rybki"]
Domy=[1,2,3,4,5]

def houses():

    single_constraints = []
    double_constraints = []
    multi_constraints = []
    single_constraints += ([(lambda a: a == 1, "Norweg")])
    single_constraints += ([(lambda a: a == 3, "Mleko")])
    double_constraints += ([(lambda a,b: a == b, ["Anglik", "Czerwony"])])
    double_constraints += ([(lambda a,b: a - b == -1, ["Zielony", "Bialy"])])
    double_constraints += ([(lambda a,b: a == b, ["Dunczyk", "Herbata"])])
    double_constraints += ([(lambda a,b: abs(a-b) == 1, ["Light", "Koty"])])
    double_constraints += ([(lambda a,b: a == b, ["Zolty", "Cygaro"])])
    double_constraints += ([(lambda a,b: a == b, ["Niemiec", "Fajka"])])
    double_constraints += ([(lambda a,b: abs(a-b) == 1, ["Light", "Woda"])])
    double_constraints += ([(lambda a,b: a == b, ["BezFiltra",  "Ptaki"])])
    double_constraints += ([(lambda a,b: a == b, ["Szwed", "Psy"])])
    double_constraints += ([(lambda a,b: abs(a-b) == 1, ["Norweg", "Niebieski"])])
    double_constraints += ([(lambda a,b: abs(a-b) == 1, ["Konie", "Zolty"])])
    double_constraints += ([(lambda a,b: a == b, ["Mentolowe", "Piwo"])])
    double_constraints += ([(lambda a,b: a == b, ["Zielony", "Kawa"])])
    multi_constraints +=  ([(lambda a, b: a != b, Narodowosc)])
    multi_constraints +=  ([(lambda a, b: a != b, Kolor)])
    multi_constraints +=  ([(lambda a, b: a != b, Napoj)])
    multi_constraints +=  ([(lambda a, b: a != b, Tyton)])
    multi_constraints +=  ([(lambda a, b: a != b, Zwierze)])

    backtracking = Backtracking(Domy, [], single_constraints,double_constraints,multi_constraints)
    backtracking.addVars(Narodowosc)
    backtracking.addVars(Kolor)
    backtracking.addVars(Napoj)
    backtracking.addVars(Tyton)
    backtracking.addVars(Zwierze)
    backtracking.solutions(0)
    for x in backtracking.solution:
        print(x)

if __name__ == "__main__":
   houses()
   map()
