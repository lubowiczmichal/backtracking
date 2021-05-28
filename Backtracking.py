class Backtracking:

    def __init__(self, dom, vars, single_constraints, double_constraints, multi_constraints):
        if vars == []:
            self.vars = []
            self.solution = []
            self.doms = {}
            self.dom = dom
        else:
            self.vars = [vars]
            self.solution = []
            self.doms = []
            self.dom = dom
            if dom != []:
                for var in vars:
                    self.doms.append([])
                for var in vars:
                    self.doms[var] = self.dom[:]
            temp = []
            for x in range(len(vars)):
                temp.append(0)
            self.solution.append(dict(zip(vars, temp)))

        self.wezlow = 0
        self.single_constraints = single_constraints
        self.double_constraints = double_constraints
        self.multi_constraints = multi_constraints
        self.allSolutions = []

    def addVars(self, vars):
        self.vars += [vars]
        temp = []
        for x in range(vars.__len__()):
            temp.append(0)
        self.solution.append(dict(zip(vars, temp)))
        for var in vars:
            self.doms[var] = self.dom[:]


    def set_doms(self,doms):
        self.doms = doms


    def solutions(self, index):
         self.wezlow += 1
         if not self.check():
            return False
         varsLen = 0
         for x in self.vars:
            varsLen += len(x)
         if index == varsLen:
            if self.check():
               return True
            else:
               return False
         v = int(index/len(self.vars[0]))
         i = self.vars[v][index%len(self.vars[0])]
         d = self.doms[i]
         for x in d:
             self.solution[v][i] = x
             if self.solutions(index + 1):
                return True
             self.solution[v][i] = 0
         return False

    def check(self):
       return (self.check_single_constraints() and self.check_double_constraints() and self.check_multi_constraints())

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
            for w1 in range(self.vars.__len__()):
                for w2 in range(self.vars.__len__()):
                    if list(self.solution[w1].keys()).__contains__(c[1][0]) and list(self.solution[w2].keys()).__contains__(c[1][1]):
                        if self.solution[w1][c[1][0]] != 0 and self.solution[w2][c[1][1]] != 0:
                            if not c[0](self.solution[w1][c[1][0]], self.solution[w2][c[1][1]]):
                                return False
        return True

    def check_multi_constraints(self):
        for w in range(self.vars.__len__()):
            for c in self.multi_constraints:
                for x1 in c[1]:
                   for x2 in c[1]:
                      if x1!=x2:
                          if list(self.solution[w].keys()).__contains__(x1) and list(self.solution[w].keys()).__contains__(x2):
                              if self.solution[w][x1] != 0 and self.solution[w][x2] != 0:
                                if not c[0](self.solution[w][x1], self.solution[w][x2]):
                                    return False
        return True

