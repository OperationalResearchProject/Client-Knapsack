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

    def eval(self):
        w = self.w()
        z = self.z()

        if w <= int(self.weightMax):
            return z
        else:
            return float(z - self.penality() * (w - int(self.weightMax)))

    def w(self):
        res = 0
        for i in range(0, len(self.weights)):
            res += int(self.weights[i]) * self.solution[i]

        return res

    def z(self):
        res = 0
        for i in range(0, len(self.profits)):
            res += int(self.profits[i]) * self.solution[i]
        return res

    def penality(self):
        penMax = 0.0
        for i in range(0, int(self.nbObject)):
            penTmp = float(int(self.profits[i]) / int(self.weights[i]))
            if penTmp > penMax:
                penMax = penTmp

        return penMax

    def generateRandomSolution(self):
        bag = [0] * self.nbObject

        for i in range(0, int(self.nbObject) - 1):
            print(i)
            bag[i] = int(bool(random.getrandbits(1)))

        return bag


kp = KnapSack("ks_1000.dat")
print("eval : "+str(kp.eval()))
