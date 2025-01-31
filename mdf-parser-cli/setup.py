from setuptools import setup, find_packages

setup(
    name='mdf_parser_cli',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.5.0',
        'rich>=12.0.0',
    ],
    entry_points={
        'console_scripts': [
            'mdf-parser=cli:main',
        ],
    },
    author='Sean Florez',
    author_email='your.email@example.com',
    description='A CLI tool for parsing MDF files and extracting molecular topology.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fl-sean03/mdf-parser-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
