echo "Executing Pylint"
pylint --rcfile=.pylintrc app/ || pylint-exit --error-fail $?
