from setuptools import setup

setup(
    name='sqlalchemy_catalog',
    version="0.0.0",
    url='http://github.com/ITCase/sqlalchemy_catalog/',
    author='Svintsov Dmitry',
    author_email='sacrud@uralbash.ru',

    packages=['sqlalchemy_catalog'],
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
)
