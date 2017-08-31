# ORA-Knapsack-Client
This project is a Knapsack client connected to the 
[Operational Research API](https://github.com/geoffreyp/OperationalResearchWebAPI)

## The knapsack problem
The knapsack problem is a problem in [combinatorial optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization): 
Given a set of items, each with a weight and a value, determine the number of each item to 
include in a collection so that the total weight is less than or equal to a given limit 
and the total value is as large as possible. It derives its name from the problem faced by
someone who is constrained by a fixed-size knapsack and must fill it with the most valuable items.


[From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Knapsack_problem)


## How use the client ?
### Use hillclimber algorithm :
```
python Client.py -h
```

### Use tabou search algorithm : (in the next release of the [Operational Research API](https://github.com/geoffreyp/OperationalResearchWebAPI))
```
python Client.py -t
```



## How rebuild proto files
```
python -m grpc_tools.protoc -I=./proto --python_out=./protoGenerated --grpc_python_out=./protoGenerated proto/hcfi.proto
```
