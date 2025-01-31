#!/usr/bin/env python3

import PyInstaller.__main__

PyInstaller.__main__.run([
    'mdf_parser.py',
    '--onefile',
    '--name=mdf_parser',
    '--add-data=README.md:.',
    '--collect-all=rich',
    '--collect-all=pandas',
    '--hidden-import=rich.console',
    '--hidden-import=rich.theme',
    '--hidden-import=rich.logging',
    '--hidden-import=pandas',
    '--hidden-import=pandas.core.algorithms',
    '--hidden-import=pandas.core.arrays',
    '--hidden-import=pandas.core.indexing',
    '--hidden-import=pandas.core.strings',
])
