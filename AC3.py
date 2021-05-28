from Backtracking import Backtracking
import time

class AC3:
    def __init__(self, dom, vars, single_constraints, double_constraints,multi_constraints):
        if vars == []:
            self.vars = []
            self.solution = []
            self.doms = {}
        else:
            self.vars = [vars]
            self.solution = []
            self.doms = {}
            for var in vars:
                self.doms[var] = self.dom[:]
            temp = []
            for x in range(len(vars)):
                temp.append(0)
            self.solution.append(dict(zip(vars,temp)))
        self.dom = dom
        self.single_constraints = single_constraints
        self.double_constraints = double_constraints
        self.multi_constraints = multi_constraints

    def addVars(self, vars):
        self.vars += [vars]
        temp = []
        for x in range(vars.__len__()):
            temp.append(0)
        self.solution.append(dict(zip(vars,temp)))
        for var in vars:
            self.doms[var] = self.dom[:]


    def AC3(self):

        self.AC3_singe()

        for x in range(len(self.doms)):
            for y in self.doms[list(self.doms.keys())[x]][:]:
                self.AC3_check_double()



    def check(self):
       return (self.check_single_constraints() and self.check_double_constraints() and self.check_multi_constraints())

    def AC3_singe(self):
        for x in range(len(self.doms)):
            for y in self.doms[list(self.doms.keys())[x]][:]:
                self.solution[0][list(self.doms.keys())[x]] = y
                if not self.check():
                    self.doms[list(self.doms.keys())[x]].remove(y)
                self.solution[0][list(self.doms.keys())[x]] = 0
                if len(self.doms[list(self.doms.keys())[x]]) == 1:
                    self.solution[0][list(self.doms.keys())[x]] = self.doms[list(self.doms.keys())[x]][0]

    def AC3_check_double(self):
        for a in range(1):
            for c in self.double_constraints:
                if list(self.solution[0].keys()).__contains__(c[1][0]) and list(self.solution[0].keys()).__contains__(c[1][1]):
                    if self.solution[0][c[1][0]] == 0:
                        for x1 in self.doms[c[1][0]][:]:
                            dom2 = self.doms[c[1][1]][:]
                            for x2 in self.doms[c[1][1]]:
                                if not c[0](x1, x2):
                                    dom2.remove(x2)
                            if len(dom2) == 0:
                                self.doms[c[1][0]].remove(x1)
                        for x1 in self.doms[c[1][1]][:]:
                            dom1 = self.doms[c[1][0]][:]
                            for x2 in self.doms[c[1][0]]:
                                if not c[0](x2, x1):
                                    dom1.remove(x2)
                            if len(dom1) == 0:
                                self.doms[c[1][1]].remove(x1)
                        if len(self.doms[c[1][0]]) == 1:
                            self.solution[0][c[1][0]] = self.doms[c[1][0]][0]
                        if len(self.doms[c[1][1]]) == 1:
                            self.solution[0][c[1][1]] = self.doms[c[1][1]][0]
                        if len(self.doms[c[1][1]]) == 1:
                            self.solution[0][c[1][1]] = self.doms[c[1][1]][0]
                        if len(self.doms[c[1][0]]) == 1:
                            self.solution[0][c[1][0]] = self.doms[c[1][1]][0]
                        self.AC3_singe()


    def check_single_constraints(self):
        for w in range(self.vars.__len__()):
            for c in self.single_constraints:
                if list(self.solution[w].keys()).__contains__(c[1]):
                   if self.solution[w][c[1]] != 0:
                       if not c[0](self.solution[w][c[1]]):
                           return False
        return True


    def check_double_constraints(self):
        for c in self.double_constraints:
            if list(self.solution[0].keys()).__contains__(c[1][0]) and list(self.solution[0].keys()).__contains__(c[1][1]):
                if self.solution[0][c[1][0]] != 0 and self.solution[0][c[1][1]] != 0:
                    if not c[0](self.solution[0][c[1][0]], self.solution[0][c[1][1]]):
                        return False
        return True

    def check_multi_constraints(self):
        for c in self.multi_constraints:
            for x1 in c[1]:
               for x2 in c[1]:
                  if x1!=x2:
                     if list(self.solution[0].keys()).__contains__(x1) and list(self.solution[0].keys()).__contains__(x2):
                        if self.solution[0][x1] != 0 and self.solution[0][x2] != 0:
                            if not c[0](self.solution[0][x1], self.solution[0][x2]):
                                return False
        return True


Narodowosc = [ "Norweg", "Anglik", "Dunczyk", "Niemiec", "Szwed"]
Kolor =["Zolty", "Niebieski", "Czerwony", "Zielony", "Bialy"]
Napoj=["Woda", "Herbata", "Mleko", "Kawa", "Piwo"]
Tyton=["Cygaro", "Light", "BezFiltra", "Fajka", "Mentolowe"]
Zwierze=["Koty", "Konie", "Ptaki", "Rybki", "Psy"]
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


    ac3 = AC3(Domy, [], single_constraints,double_constraints,multi_constraints)
    ac3.addVars(Narodowosc)
    ac3.addVars(Kolor)
    ac3.addVars(Napoj)
    ac3.addVars(Tyton)
    ac3.addVars(Zwierze)
    start = time.time()
    ac3.AC3()
    for x in ac3.doms:
        print(x, ac3.doms[x])
    end = time.time()
    print(end - start)
    back = Backtracking([],[],single_constraints,double_constraints,multi_constraints)
    back.addVars(Narodowosc)
    back.addVars(Kolor)
    back.addVars(Napoj)
    back.addVars(Tyton)
    back.addVars(Zwierze)
    back.set_doms(ac3.doms)
    start = time.time()
    back.solutions(0)
    end = time.time()
    print(end - start)
    for x in back.solution:
        print(x)

if __name__ == "__main__":
    houses()
