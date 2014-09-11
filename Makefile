all: test

test:
	nosetests --with-coverage --cover-package pyramid_sacrud_catalog --cover-erase --with-doctest
