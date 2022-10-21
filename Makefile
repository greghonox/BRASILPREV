clean_pycache:
	find . -type d -name __pycache__ -exec rm -r {} \+

run:
	python3 main.py

tests:
	python3 -m unittest discover -s tests -vvv