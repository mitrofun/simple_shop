.PHONY: all help clean run qa user docker-build docker-run

# target: all - Default target. Does nothing.
all:
	@clear
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@clear
	@egrep "^# target:" [Mm]akefile

# target: clean - Delete pycache
clean:
	echo "### Cleaning *.pyc and .DS_Store files "
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '.DS_Store' -exec rm -f {} \;
	find . -name "__pycache__" -type d -exec rm -rf {} +

# target: run - Run server
run:
	python3 manage.py runserver

# target: qa - Run tests
qa:
	pytest

# target: user - create default user
user:
	python3 manage.py createdefaultuser

# target: loaddata - Load reference data
loaddata:
	python3 manage.py loaddata fixtures/category.json

# target: docker-build - Build docker image with tag simpleshop
docker-build:
	docker build . -t simpleshop

# target: docker-run - Run docker image with tag simpleshop
docker-run:
	docker run --name djshop -p 80:80 -d simpleshop
