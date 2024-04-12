.PHONY: run
run:
	clear && .venv/bin/python main.py

.PHONY: setup
setup:
	make venv
	make discord
	make python-dotenv
	make mysql

venv:
	python3 -m venv .venv && /bin/bash .venv/bin/activate

discord:
	.venv/bin/pip install discord

python-dotenv:
	.venv/bin/pip install python-dotenv

mysql:
	.venv/bin/pip install mysql-connector-python

.PHONY: clean
clean:
	make venv-clean
	make pycache-clean

venv-clean:
	rm -rf .venv

pycache-clean:
	find . -type d -name __pycache__ -exec rm -rf {} \;

.PHONY: env
env:
	cp .env.example .env.local