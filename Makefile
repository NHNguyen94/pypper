unittest:
	PYTHONPATH=. python -m unittest
test:
	PYTHONPATH=. poetry run pytest
check:
	PYTHONPATH=. flake8 pypper
