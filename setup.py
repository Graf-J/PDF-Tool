from setuptools import setup, find_packages

setup(
    name='PDF_Tool',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'pdf=PDF_Tool.main:main'
        ]
    },
    packages=find_packages()
)