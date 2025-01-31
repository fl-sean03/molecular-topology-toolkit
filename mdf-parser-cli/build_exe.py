#!/usr/bin/env python3

import PyInstaller.__main__

PyInstaller.__main__.run([
    'mdf_parser.py',
    '--onefile',
    '--name=mdf_parser',
    '--add-data=README.md:.',
    '--hidden-import=rich.console',
    '--hidden-import=rich.theme',
    '--hidden-import=pandas',
])
