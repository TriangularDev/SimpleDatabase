from setuptools import setup, find_packages


setup(
    name='SimpleDatabase',
    version='0.15',
    license='MIT',
    author="Me",
    author_email='me@me.me',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='database',
    install_requires=[],

)