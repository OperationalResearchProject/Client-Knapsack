import random


class KnapSack:

    def __init__(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
            self.nbObject = int(lines[0])
            self.profits = lines[1].split()
            self.weights = lines[2].split()
            self.weightMax = lines[3]
            self.solution = self.generateRandomSolution()

    def fitness(self, sol=''):
        """
        Return an evaluation of the current solution
        """

        w = self.w(sol.split("-") if sol != '' else self.solution)
        z = self.z(sol.split("-") if sol != '' else self.solution)

        if w <= int(self.weightMax):
            return 1 / z
        else:
            return 1 / (float(z - self.penality() * (w - int(self.weightMax))))

    def w(self, solution):
        """
        Return the current weigh of the solution
        """
        res = 0
        for i in range(0, len(self.weights)):
            res += int(self.weights[i]) * int(solution[i])

        return res

    def z(self, solution):
        """
        Return the current profit of the solution
        """
        res = 0
        for i in range(0, len(self.profits)):
            res += int(self.profits[i]) * int(solution[i])
        return res

    def penality(self):
        """
         Return the higher ratio Profit / weight of the solution
        """

        penMax = 0.0
        for i in range(0, int(self.nbObject)):
            penTmp = float(int(self.profits[i]) / int(self.weights[i]))
            if penTmp > penMax:
                penMax = penTmp

        return penMax

    def generateRandomSolution(self):
        """
        Return a random solution
        """

        bag = [0] * self.nbObject

        for i in range(0, int(self.nbObject)):
            bag[i] = int(bool(random.getrandbits(1)))

        return bag

    def getRandomNeighbor(self):
        """
        Return a random neighbor of the current solution
        """

        rdm1 = rdm2 = 0
        while rdm1 == rdm2:
            rdm1 = random.randint(0, int(self.nbObject) - 1)
            rdm2 = random.randint(0, int(self.nbObject) - 1)

        tmp = self.solution[rdm1]

        self.solution[rdm1] = self.solution[rdm2]
        self.solution[rdm2] = tmp

    def toString(self):
        """
        Return the solution with the OR-API format
        """

        res = ''
        for i in range(0, int(self.nbObject)):
            res += str(self.solution[i]) + '-'

        return res[:-1]
