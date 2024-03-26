unittest:
	PYTHONPATH=. python -m unittest
pytest:
	PYTHONPATH=. poetry run pytest
check:
	PYTHONPATH=. flake8 pypper
