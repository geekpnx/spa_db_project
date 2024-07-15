from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=[
        'psycopg==3.2.1',
        'psycopg-binary==3.2.1',
        'environs==11.0.0',
        'bcrypt==4.1.3',
        'spa==0.9'      
    ]
)
