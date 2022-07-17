from setuptools import setup, find_packages


setup(
    name='TriangleDB',
    version='1.0',
    license='MIT',
    author="Me",
    author_email='me@me.me',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/28klotlucas2/SimpleDatabase',
    keywords='database',
    install_requires=[],

)