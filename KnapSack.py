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

    def fitness(self):
        """
        Return an evaluation of the current solution
        """

        w = self.w()
        z = self.z()

        if w <= int(self.weightMax):
            return z
        else:
            return float(z - self.penality() * (w - int(self.weightMax)))

    def w(self):
        """
        Return the current weigh of the solution
        """
        res = 0
        for i in range(0, len(self.weights)):
            res += int(self.weights[i]) * self.solution[i]

        return res

    def z(self):
        """
        Return the current profit of the solution
        """
        res = 0
        for i in range(0, len(self.profits)):
            res += int(self.profits[i]) * self.solution[i]
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

        for i in range(0, int(self.nbObject) - 1):
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
