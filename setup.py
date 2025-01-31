from setuptools import setup, find_packages

setup(
    name='molecular_topology_parser',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'topology-parser=tools.cli:main',
        ],
    },
    author='Your Name',
    description='A toolkit for parsing molecular topology files in CHARMM parameter and MDF formats.',
    url='https://github.com/yourusername/molecular-topology-parser',
)
