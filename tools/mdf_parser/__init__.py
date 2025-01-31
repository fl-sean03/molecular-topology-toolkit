"""
MDF Parser module for extracting molecular topology from MDF files.

This package provides functionality to:
- Parse MDF (Molecular Data Format) files
- Extract molecular topology information
- Generate structured output in CSV or JSON formats
"""

from .parser import main
from .mdf_parser import parse_mdf_file
from .topology import extract_topology
from .output_handler import save_output

__all__ = ['main', 'parse_mdf_file', 'extract_topology', 'save_output']
