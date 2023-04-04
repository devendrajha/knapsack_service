# knapsack_service



### Install dependencies
```
pip3 install -r requirements.txt
```

### Run Pylint locally
````
find . -type f -name "*.py" | xargs pylint --fail-under=8 || pylint-exit $?
```

### Run IT (Integration Test)
```
export PYTHONPATH='./'
pytest it
```

# Test
### Install dependencies
```
pip3 install -r requirements-tests.txt
```
### Run unit test
```
export PYTHONPATH='./'
pytest tests/
```

docker build -f Dockerfile -t knapsack_service:latest .
docker run -p 8001:8080 knapsack_service
