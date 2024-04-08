.PHONY: run
run:
	clear && python main.py

.PHONY: setup venv source discord python-dotenv
setup:
	make venv
	make discord
	make python-dotenv

venv:
	python3 -m venv .venv && /bin/bash .venv/bin/activate

discord:
	pip install discord

python-dotenv:
	pip install python-dotenv

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