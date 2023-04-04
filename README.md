# Knapsack Optimizer Service

Author: Devendra Jha, *devkjha@gmail.com*


## Introduction ##

Knapsack is a simple service offering API for solving [0/1 Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem). Knapsack problem models various practical problems including distribution of indivisible resources, choice of projects, cutting-stock problems, cryptography, financial decisions and many more.

### Implementation ###

Knapsack is a Django based application with distributed task queue Celery on the backend. There are many means how to solve Knapsack problem. Our service offers following solvers which you can feed by your Knapsak problems:

*  [**Knapsack Problem using recursion**](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/). Clearly, this code requires a recursion stack, hence the space complexity is equal to the depth of the stack. In our demonstration above, you can see that the recursion stack is N level deep where N is the number of items or the length of the item array. We can say that the space complexity is O(N).

The running time of this algorithm can be written as the following recurrence:-   
T(N) = 2T(N-1) + O(1), which is simplified to O(2^N). This is also evident from the recursion tree, which has 2^N leaves.
problem

Optimize Maximum is represented by its *class* in `/knapsack_service/app/service`. All solvers are inherited from the base *class* `IKnapsackOptimizer`. This class defines a common interface for all solvers a facilitates following:



#### Data Ingestion and Validation ####
Tasks are defined using a JSON structure. This structure is common for web and REST API interfaces. Example follows (we hope that the structure is more or less self-explanatory):

```
POST API URI:-  http://localhost:8001/knapsack
Post Json:-
{
"values": [60, 100, 120],
"weights": [10, 20, 30],
"capacities": 50
}
```
### Installation: ####
```
docker build -f Dockerfile -t knapsack_service:latest .
docker run -p 8001:8080 knapsack_service
```

### Install dependencies
```
pip3 install -r requirements.txt
pip3 install -r requirements-tests.txt
```
### Run unit test
```
export PYTHONPATH='./'
pytest tests/
```


### Run Pylint locally
```
find . -type f -name "*.py" | xargs pylint --fail-under=8 || pylint-exit $?
```
