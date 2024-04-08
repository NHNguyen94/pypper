unittest:
	PYTHONPATH=. python -m unittest
test:
	PYTHONPATH=. poetry run pytest
check:
	PYTHONPATH=. ruff check
format:
	PYTHONPATH =. ruff format