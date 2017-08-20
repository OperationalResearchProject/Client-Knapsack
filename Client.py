import sys, getopt, urllib.request, subprocess, grpc
from KnapSack import KnapSack
from protoGenerated import hcfi_pb2_grpc
from protoGenerated import hcfi_pb2


def main(argv):

    kp = KnapSack("ks_1000.dat")

    print("Start....")
    print("eval : " + str(kp.fitness()))
    print(kp.toString())

    channel = grpc.insecure_channel('127.0.0.1:50051')
    stubHillClimber = hcfi_pb2_grpc.HillClimberServiceStub(channel)

    response = stubHillClimber.InitTransaction(hcfi_pb2.InitTransactionRequest(
        customer='Client-Knapsack-Test',
        algorithm="hillclimber_first_improvement",
        solutionSize=kp.nbObject,
        fitness=kp.fitness(),
        solution=kp.toString()
    ))

    for i in range(0, 10000):
        response = stubHillClimber.SendFitness(hcfi_pb2.FitnessRequest(
            id=response.id,
            fitness=kp.fitness(response.solution),
            solution=response.solution))

    stop = stubHillClimber.StopTransaction(hcfi_pb2.StopRequest(id=response.id, message='done'))
    print("\nEnd")
    print("eval : " + str(stop.fitness))
    print(stop.solution)

if __name__ == "__main__":
    main(sys.argv[1:])
