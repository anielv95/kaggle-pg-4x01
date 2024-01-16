settings:
	pip install --upgrade pip &&\
		pip install kaggle &&\
	git config --global user.email ${GITEMAIL} &&\
	git config --global user.name ${GITNAME}

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


lint:
	pylint --disable=R,C src/*.py

format:
	black src/*.py

test:
	python -m pytest -vv -s --cov=functions src/test_functions.py