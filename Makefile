all: test

test:
	nosetests --with-coverage --cover-package sacrud_catalog --cover-erase --with-doctest
