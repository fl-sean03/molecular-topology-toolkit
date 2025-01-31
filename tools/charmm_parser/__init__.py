"""
CHARMM parameter file parser package.

This package provides functionality to:
- Parse CHARMM parameter files
- Extract molecular parameters for bonds, angles, dihedrals etc.
- Generate structured output in CSV or JSON formats
"""

from .parser import CharmmProcessor
from .parsers import parse_charmm_parameter_file

__all__ = ['CharmmProcessor', 'parse_charmm_parameter_file']
