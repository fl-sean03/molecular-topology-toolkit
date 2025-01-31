from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='molecular_topology_parser',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.0',
        'rich>=10.0.0',
    ],
    entry_points={
        'console_scripts': [
            'topology-parser=tools.cli:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A toolkit for parsing molecular topology files in CHARMM parameter and MDF formats.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/molecular-topology-parser',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    python_requires='>=3.6',
    license='MIT',
)
